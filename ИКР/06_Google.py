import tkinter as tk
from tkinter import messagebox
import requests

# Список ID криптовалют в системе CoinGecko
COIN_IDS = "bitcoin,ethereum,solana,binancecoin,ripple"
# Соответствие ID их читаемым названиям и тикерам
COIN_MAPPING = {
    "bitcoin": ("Bitcoin", "BTC"),
    "ethereum": ("Ethereum", "ETH"),
    "solana": ("Solana", "SOL"),
    "binancecoin": ("BNB", "BNB"),
    "ripple": ("Ripple", "XRP"),
}


class CryptoTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Price Tracker")
        self.root.geometry("450x400")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        # Заголовок
        self.header_label = tk.Label(
            root,
            text="Курсы криптовалют (USD)",
            font=("Arial", 16, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        self.header_label.pack(pady=15)

        # Контейнер для вывода карточек валют
        self.prices_frame = tk.Frame(root, bg="#1e1e2e")
        self.prices_frame.pack(pady=10, fill="x", padx=20)

        # Словарь для хранения текстовых виджетов под каждую монету
        self.price_labels = {}

        # Создаем строки для каждой криптовалюты
        for coin_id, (name, ticker) in COIN_MAPPING.items():
            row_frame = tk.Frame(self.prices_frame, bg="#313244", bd=1, relief="groove")
            row_frame.pack(fill="x", pady=5, ipady=8, padx=10)

            name_label = tk.Label(
                row_frame,
                text=f"{name} ({ticker})",
                font=("Arial", 12, "bold"),
                bg="#313244",
                fg="#cdd6f4"
            )
            name_label.pack(side="left", padx=10)

            price_label = tk.Label(
                row_frame,
                text="Загрузка...",
                font=("Arial", 12, "bold"),
                bg="#313244",
                fg="#a6e3a1"
            )
            price_label.pack(side="right", padx=10)

            self.price_labels[coin_id] = price_label

        # Кнопка обновления
        self.refresh_button = tk.Button(
            root,
            text="Обновить вручную",
            font=("Arial", 11, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#b4befe",
            command=self.fetch_prices,
            relief="flat",
            cursor="hand2"
        )
        self.refresh_button.pack(pady=20, ipadx=10, ipady=5)

        # Статус-бар (время последнего обновления)
        self.status_label = tk.Label(
            root,
            text="Инициализация...",
            font=("Arial", 9),
            bg="#1e1e2e",
            fg="#7f849c"
        )
        self.status_label.pack(side="bottom", fill="x", pady=5)

        # Первый запуск получения данных
        self.fetch_prices()

        # Запуск цикла автообновления (каждые 30 секунд)
        self.auto_refresh()

    def fetch_prices(self):
        """Получает актуальные курсы через Public Keyless API CoinGecko"""
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": COIN_IDS,
            "vs_currencies": "usd"
        }

        try:
            # Отправляем запрос к API
            response = requests.get(url, params=params, timeout=10)

            # Обработка лимитов запросов (ошибка 429)
            if response.status_code == 429:
                self.status_label.config(text="Превышен лимит запросов API. Ожидайте...")
                return

            response.raise_for_status()
            data = response.json()

            # Обновляем интерфейс полученными данными
            for coin_id, price_label in self.price_labels.items():
                if coin_id in data:
                    price = data[coin_id]["usd"]
                    # Форматируем вывод (красивое отображение тысяч и копеек)
                    formatted_price = f"${price:,.2f}" if price >= 1 else f"${price:.4f}"
                    price_label.config(text=formatted_price)

            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            self.status_label.config(text=f"Последнее обновление: {current_time}")

        except requests.exceptions.RequestException as e:
            self.status_label.config(text="Ошибка сети")
            messagebox.showerror("Ошибка", f"Не удалось получить данные:\n{e}")

    def auto_refresh(self):
        """Метод для циклического обновления данных в фоновом режиме Tkinter"""
        self.fetch_prices()
        # 30000 миллисекунд = 30 секунд
        self.root.after(30000, self.auto_refresh)


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoTrackerApp(root)
    root.mainloop()