import tkinter as tk
from PIL import Image, ImageTk  # Для работы с изображениями

# Создаём основное окно
root = tk.Tk()
root.title("Пример с иконкой и надписью")

# Путь к файлу с изображением (иконка)
icon_path = "bitcoin.png"  # Убедитесь, что файл в той же папке или укажите полный путь

# Загружаем изображение и создаем объект PhotoImage
icon = ImageTk.PhotoImage(Image.open(icon_path))

# Создаём метку с текстом и иконкой
label1 = tk.Label(root, text="Привет, мир!", font=("Arial", 16), padx=10)
label1.pack(pady=20)  # Отступ для лучшего расположения
label = tk.Label(root, text="Привет, мир!", image=icon, font=("Arial", 16), padx=10)
label.pack(pady=20)  # Отступ для лучшего расположения

root.mainloop()
