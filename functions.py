from tkinter import *
def menu(win):
    top = Menu(win)
    win.config(menu=top)

    mainMenu = Menu(top)
    mainMenu.add_command(label='Подключиться к базе данных', command=None, underline=0)
    top.add_cascade(label='Меню', menu=mainMenu)
