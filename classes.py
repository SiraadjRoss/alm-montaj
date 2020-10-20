from tkinter import *
from tkinter.filedialog import askopenfilename

# Класс виждета таблицы
class Table(Frame):
    def __init__(self, parent=None, numrow=5, titletable=[]):
        Frame.__init__(self, parent)
        self.numrow = numrow
        self.titletable = titletable
        self.makeTable(numrow, titletable)

    def makeTable(self, numrow, titletable):
        numcol = len(titletable)
        j=0
        for t in titletable:
            title = Label(self, text=t, relief=RIDGE)
            title.grid(row=0, column=j, sticky=NSEW)
            j+=1
            
        self.rows = []
        for i in range(numrow):
            cols = []
            for j in range(numcol):
                ent = Entry(self, relief=RIDGE)
                ent.config(width=15)
                ent.grid(row=i+1, column=j, sticky=NSEW)
                ent.insert(END, '%d.%d' % (i, j))
                ent.config(state='disabled')
                cols.append(ent)
            self.rows.append(cols)
            
            
