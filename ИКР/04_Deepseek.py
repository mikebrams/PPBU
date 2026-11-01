import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading

# Популярные криптовалюты (ID CoinGecko)
COINS = {
    "bitcoin": "Bitcoin (BTC)",
    "ethereum": "Ethereum (ETH)",
    "binancecoin": "BNB (BNB)",
    "solana": "Solana (SOL)",
    "ripple": "XRP (XRP)",
    "cardano": "Cardano (ADA)",
    "dogecoin": "Dogecoin (DOGE)",
    "polkadot": "Polkadot (DOT)"
}


class CryptoTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Курсы криптовалют к USD (CoinGecko)")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Заголовок
        title_label = tk.Label(root, text="Актуальные курсы криптовалют", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Таблица
        columns = ("name", "price", "change")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
        self.tree.heading("name", text="Валюта")
        self.tree.heading("price", text="Цена (USD)")
        self.tree.heading("change", text="Изм. за 24ч (%)")

        self.tree.column("name", width=200, anchor="w")
        self.tree.column("price", width=150, anchor="e")
        self.tree.column("change", width=120, anchor="e")

        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        # Кнопка обновления
        self.refresh_btn = tk.Button(root, text="Обновить данные", command=self.fetch_data_threaded, bg="#4CAF50",
                                     fg="white", font=("Arial", 12))
        self.refresh_btn.pack(pady=10)

        # Статус
        self.status_label = tk.Label(root, text="Нажмите «Обновить данные» для загрузки курсов.", fg="gray")
        self.status_label.pack(pady=5)

        # Автоматическая загрузка при старте
        self.fetch_data_threaded()

    def fetch_data_threaded(self):
        """Запуск загрузки данных в отдельном потоке, чтобы не блокировать интерфейс."""
        self.refresh_btn.config(state="disabled", text="Загрузка...")
        self.status_label.config(text="Запрос к CoinGecko API...")
        thread = threading.Thread(target=self.fetch_data)
        thread.daemon = True
        thread.start()

    def fetch_data(self):
        """Запрос к API CoinGecko."""
        ids = ",".join(COINS.keys())
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Обновление интерфейса в основном потоке
            self.root.after(0, self.update_table, data)

        except requests.exceptions.RequestException as e:
            self.root.after(0, self.show_error, f"Ошибка сети или API: {e}")
        except Exception as e:
            self.root.after(0, self.show_error, f"Неизвестная ошибка: {e}")

    def update_table(self, data):
        """Заполнение таблицы полученными данными."""
        # Очистка старых данных
        for item in self.tree.get_children():
            self.tree.delete(item)

        for coin_id, coin_name in COINS.items():
            if coin_id in data:
                info = data[coin_id]
                price = info.get("usd", "N/A")
                change = info.get("usd_24h_change")

                price_str = f"${price:,.2f}" if isinstance(price, (int, float)) else "N/A"
                change_str = f"{change:+.2f}%" if isinstance(change, (int, float)) else "N/A"

                # Цвет для изменения
                tag = "positive" if isinstance(change, (int, float)) and change >= 0 else "negative"
                self.tree.insert("", "end", values=(coin_name, price_str, change_str), tags=(tag,))

        # Настройка цветов
        self.tree.tag_configure("positive", foreground="green")
        self.tree.tag_configure("negative", foreground="red")

        self.status_label.config(text="Данные успешно обновлены.", fg="green")
        self.refresh_btn.config(state="normal", text="Обновить данные")

    def show_error(self, message):
        """Отображение ошибки."""
        self.status_label.config(text=message, fg="red")
        self.refresh_btn.config(state="normal", text="Обновить данные")
        messagebox.showerror("Ошибка", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoTrackerApp(root)
    root.mainloop()

"""
Как это работает
API-запрос: Приложение отправляет GET-запрос к https://api.coingecko.com/api/v3/simple/price.
Параметр ids содержит список идентификаторов криптовалют (например, bitcoin, ethereum),
а vs_currencies=usd указывает, что курс нужен в долларах. Параметр include_24hr_change=true
добавляет процент изменения за сутки .

Асинхронность: Запрос выполняется в отдельном потоке (threading), 
чтобы интерфейс не «зависал» во время ожидания ответа от сервера.

Отображение: Данные помещаются в виджет Treeview (таблицу).
Положительное изменение курса подсвечивается зелёным, отрицательное — красным.

Примечание по использованию API
Приведённый код использует бесплатный Demo-эндпоинт CoinGecko.
У него есть ограничения по частоте запросов (rate limit), 
поэтому не стоит нажимать кнопку «Обновить» слишком часто. 
Для большинства задач личного мониторинга этого вполне достаточно.
"""
