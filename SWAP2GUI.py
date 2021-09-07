from tkinter import scrolledtext as scrtxt
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import subprocess


# Function
def enter():
    time_in = 0
    if txbox.get() == '':
        messagebox.showerror(title='Error', message='Opening can not be blank!', default='ok', icon='error')
        return

    if txbox1.get() == '':
        time_in = 60
    elif txbox1.get().isnumeric() and int(txbox1.get()) < 0:
        messagebox.showerror(title='Error', message='Time must be > 0!', default='ok', icon='error')
        return
    elif txbox1.get().isnumeric():
        time_in = int(txbox1.get())
    else:
        messagebox.showerror(title='Error', message='Not valid!', default='ok', icon='error')
        return

    pass


# Variable
program = subprocess.run('dir Engine\\*.exe /b', shell=True,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE).stdout.decode().split()
version = '1.0'

# Window Setting
win = Tk()
win.geometry("")
win.resizable(0, 0)
win.title(f'Swap2 Tool for Gomoku ver {version}')

# GUI
lb1 = Label(win, text='Opening:', font=('Times New Roman', 11))
lb2 = Label(win, text='Time (sec):', font=('Times New Roman', 11))
lb3 = Label(win, text='Engine:', font=('Times New Roman', 11))
lb4 = Label(win, text='(Default is 60 seconds)', font=('Times New Roman', 10, 'italic'))
lb5 = Label(win, text='Protocol:', font=('Times New Roman', 11))

txbox = Entry(win, width=23)
txbox1 = Entry(win, width=23)

combo = Combobox(win, width=20)
combo['values'] = program
combo.current(0)

combo1 = Combobox(win, width=20)
combo1['values'] = ['Gomocup protocol', 'Yixin protocol']
combo1.current(0)

scrt = scrtxt.ScrolledText(win, width=60, height=10)

button = Button(win, text='Enter', command=enter)

# Grid
lb1.grid(column=0, row=0, sticky='W', padx=5, pady=5)
lb2.grid(column=0, row=1, sticky='W', padx=5, pady=5)
lb3.grid(column=0, row=2, sticky='W', padx=5, pady=5)
lb4.grid(column=2, row=1, sticky='W', padx=5, pady=5)
lb5.grid(column=0, row=3, sticky='W', padx=5, pady=5)


txbox.grid(column=1, row=0, sticky='W', padx=5, pady=5)
txbox1.grid(column=1, row=1, sticky='W', padx=5, pady=5)

combo.grid(column=1, row=2, sticky='W', padx=5, pady=5)
combo1.grid(column=1, row=3, sticky='W', padx=5, pady=5)

scrt.grid(column=0, columnspan=10, row=4, sticky='WE', padx=5, pady=5)

button.grid(column=9, row=5, sticky='E', padx=5, pady=5)

win.mainloop()
