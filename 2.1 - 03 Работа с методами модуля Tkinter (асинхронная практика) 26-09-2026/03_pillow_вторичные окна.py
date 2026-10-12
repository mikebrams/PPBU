from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image, ImageTk

def quit():
    root.destroy()

def open():
    try:
        file = fd.askopenfilename()
        if file:
            img = Image.open(file)
            imgconv = img
            width = 500
            height = 500
            img.thumbnail((width, height))
            imgtk = ImageTk.PhotoImage(img)

            img_window = Toplevel(root)     # создаем окно над нашим основным окном root
            img_window.title('Просмотр изображения')
            l = Label(img_window, image=imgtk)
            l.pack()

            l.image = imgtk
    except FileNotFoundError:
        mb.showerror('Ошибка', 'Файл не найден')
    except OSError:
        mb.showerror('Ошибка', 'Не удалось открыть файл, возможно это не изображение')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка {e}')


root = Tk()
root.title('Photo')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'500x500+{w//4}+{h//3}')

l = Label()
l.pack()

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Открыть...', command=open)
filemenu.add_separator()
filemenu.add_command(label='Выход', command=quit)
mainmenu.add_cascade(label='Файл', menu=filemenu)

root.mainloop()