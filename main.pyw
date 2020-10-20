from tkinter import *
from classes import Table
from functions import menu
#Создаем переменную для корневого окна
root = Tk()
#Задаем титульную надпись окна
root.title('АЛМ-Монтаж. *Диспетчерская*')
labelfont = ('helvetica', 12, 'normal') #Семейство размер стиль шрифта Меток
#Создаем меню
menu(root)
#Создаем 4е сновных фрейма интерфейса
frameTitle = Frame(root, bd = 3, relief = GROOVE, borderwidth = 3)
frameTitle.pack(side = TOP, expand = NO, fill = X)
Label(frameTitle, font = labelfont, text = 'Журнал заявок').pack(side = LEFT, expand = NO, fill = X)

frameIndikators = Frame(root)
frameIndikators.pack(side = TOP, expand = NO, fill = X)

frameButtons = Frame(root)
frameButtons.pack(side = TOP, expand = NO, fill = X)

frameTable = Frame(root)
frameTable.pack(side = LEFT, expand = NO, fill = BOTH)
#Конструируем фрейм который содержит фреймы с индикаторами

#Фрейм индикатора New (отображает новые заявки)
frameNew = Frame(frameIndikators, bg = 'white', bd = 3, relief = GROOVE, borderwidth = 3)
frameNew.pack(side = LEFT)
Label(frameNew, text = 'НОВЫЕ', bg = 'white', width = 20).pack(side = TOP)
qNew = Label(frameNew, text = '2 шт. (22%)', bg = 'white')
qNew.pack(side = TOP)
# Добавить чекбокс или радто буттон
chkNew = IntVar()
Checkbutton(frameNew, variable = chkNew, bg = 'white').pack()

#Фрейм индикатора Work (Отображает заявки в работе)
frameWork = Frame(frameIndikators, bg = '#fffaac', bd = 3, relief = GROOVE, borderwidth = 3)
frameWork.pack(side = LEFT)
Label(frameWork, text = 'В РАБОТЕ', bg = '#fffaac', width = 20).pack(side = TOP)
qWork = Label(frameWork, text = '5 шт. (25%)', bg = '#fffaac')
qWork.pack(side = TOP)
# Добавить чекбокс или радто буттон
chkWork = IntVar()
Checkbutton(frameWork, variable = chkWork, bg = '#fffaac').pack()

#Фрейм индикатора Hold (Отложенные заявки)
frameHold = Frame(frameIndikators, bd = 3, relief = GROOVE, borderwidth = 3)
frameHold.pack(side = LEFT)
Label(frameHold, text = 'ОТЛОЖЕНЫ', width = 20).pack(side = TOP)
qHold = Label(frameHold, text = '1 шт. (5%)')
qHold.pack(side = TOP)
# Добавить чекбокс или радто буттон
chkHold = IntVar()
Checkbutton(frameHold, variable = chkHold).pack()

#Фрейм индикатора Complet (Завершенные заявки)
frameComplet = Frame(frameIndikators, bg = '#87ffac', bd = 3, relief = GROOVE, borderwidth = 3)
frameComplet.pack(side = LEFT)
Label(frameComplet, text = 'ЗАВЕРШЕНЫ', bg = '#87ffac', width = 20).pack(side = TOP)
qComplet = Label(frameComplet, text = '45 шт. (85%)', bg = '#87ffac')
qComplet.pack(side = TOP)
# Добавить чекбокс или радто буттон
chkComplet = IntVar()
Checkbutton(frameComplet, variable = chkComplet, bg = '#87ffac').pack()

#Фрейм индикатора Denial (Отказ от заявки)
frameDenial = Frame(frameIndikators, bg = '#ff947e', bd = 3, relief = GROOVE, borderwidth = 3)
frameDenial.pack(side = LEFT)
Label(frameDenial, text = 'ОТКАЗ', bg = '#ff947e', width = 20).pack(side = TOP)
qDenial = Label(frameDenial, text = '3 шт. (10%)', bg = '#ff947e' )
qDenial.pack(side = TOP)
# Добавить чекбокс или радто буттон
chkDenial = IntVar()
Checkbutton(frameDenial, variable = chkDenial, bg = '#ff947e').pack()

#Добавляем кнопки управления в фрейм кнопок
createButton = Button(frameButtons, text = 'Создать заявку')
createButton.pack(side = LEFT)

changeButton = Button(frameButtons, text = 'Изменить заявку')
changeButton.pack(side = LEFT)

findButton = Button(frameButtons, text = 'Найти заявку')
findButton.pack(side = LEFT)

findEntry = Entry(frameButtons)
findEntry.pack(side = LEFT)

title = ['НР', 'Магазин', 'Город', 'Дата заказа', 'Отдел' ,'Бюджет' ,'Номер заказа', 'Дата выполнения', 'Работы', 'Статус', 'Примечания']
table = Table(frameTable, 20, title)
table.pack()
mainloop()
