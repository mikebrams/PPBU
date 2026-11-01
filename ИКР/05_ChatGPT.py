import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime
import threading

API_URL = "https://api.coingecko.com/api/v3/simple/price"

COINS = {
    "bitcoin": ("Bitcoin", "BTC"),
    "ethereum": ("Ethereum", "ETH"),
    "tether": ("Tether", "USDT"),
    "binancecoin": ("BNB", "BNB"),
    "solana": ("Solana", "SOL"),
    "dogecoin": ("Dogecoin", "DOGE"),
}


def update_prices():
    refresh_button.config(state="disabled")
    status_label.config(text="Загрузка курсов...")

    def fetch():
        try:
            response = requests.get(
                API_URL,
                params={
                    "ids": ",".join(COINS.keys()),
                    "vs_currencies": "usd",
                    "include_24hr_change": "true",
                },
                timeout=15,
            )
            response.raise_for_status()
            data = response.json()

            root.after(0, lambda: show_prices(data))

        except Exception as error:
            root.after(
                0,
                lambda err=str(error): show_error(err)
            )

    threading.Thread(target=fetch, daemon=True).start()


def show_prices(data):
    for item in tree.get_children():
        tree.delete(item)

    for coin_id, (name, symbol) in COINS.items():
        coin_data = data.get(coin_id, {})
        price = coin_data.get("usd")
        change = coin_data.get("usd_24h_change")

        if price is None:
            price_text = "Нет данных"
        else:
            price_text = f"${price:,.8f}".rstrip("0").rstrip(".")

        if change is None:
            change_text = "—"
        else:
            change_text = f"{change:+.2f}%"

        tree.insert(
            "",
            "end",
            values=(name, symbol, price_text, change_text)
        )

    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    status_label.config(text=f"Обновлено: {now}")
    refresh_button.config(state="normal")


def show_error(error):
    status_label.config(text="Не удалось загрузить курсы")
    refresh_button.config(state="normal")
    messagebox.showerror(
        "Ошибка",
        f"Не удалось получить данные CoinGecko.\n\n{error}"
    )


root = tk.Tk()
root.title("Курсы криптовалют")
root.geometry("680x360")
root.minsize(600, 300)

title_label = ttk.Label(
    root,
    text="Курсы криптовалют к доллару США",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=12)

columns = ("name", "symbol", "price", "change")

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=8
)

tree.heading("name", text="Криптовалюта")
tree.heading("symbol", text="Тикер")
tree.heading("price", text="Цена (USD)")
tree.heading("change", text="Изменение за 24 ч.")

tree.column("name", width=180, anchor="w")
tree.column("symbol", width=80, anchor="center")
tree.column("price", width=170, anchor="e")
tree.column("change", width=150, anchor="e")

tree.pack(fill="both", expand=True, padx=12, pady=5)

refresh_button = ttk.Button(
    root,
    text="Обновить курсы",
    command=update_prices
)
refresh_button.pack(pady=8)

status_label = ttk.Label(root, text="Готово к загрузке")
status_label.pack(pady=(0, 10))

update_prices()

root.mainloop()