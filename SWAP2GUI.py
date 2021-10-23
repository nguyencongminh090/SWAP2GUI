from tkinter import scrolledtext as scrtxt
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import subprocess
from control import Control
from threading import Thread


# Function
def clear():
    scrt.delete('0.0', END)


def enter():
    # Check opening field
    if txbox.get() == '':
        messagebox.showerror(title='Error', message='Opening can not be blank!', default='ok', icon='error')
        return

    # Check time field
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

    # Check Max_memory field
    if txbox2.get() != '' and not txbox2.get().isnumeric():
        messagebox.showerror(title='Error', message='Max_memory must be a number!', default='ok', icon='error')
        print(f'Memory: [{txbox2.get()}]')
        return
    scrt.delete('0.0', END)
    scrt.insert('insert', f'[User] Openning: {txbox.get()}\n')
    scrt.insert('insert', f'[User] Time: {time_in} sec\n')
    scrt.insert('insert', f'[User] Engine: {combo.get()}.exe\n')
    scrt.insert('insert', f'[User] Protocol: {combo1.get()}\n')
    if txbox2.get() == '':
        scrt.insert('insert', '[User] Max memory: 2 GB\n')
        ctrl = Control(txbox.get(), time_in * 1000, combo.get(), combo1.get(), scrt)
    else:
        scrt.insert('insert', f'[User] Max memory: {txbox2.get()} GB\n')
        ctrl = Control(txbox.get(), time_in * 1000, combo.get(), combo1.get(), scrt, txbox2.get())
    scrt.insert('insert', '-' * 60 + '\n')
    thread = Thread(target=ctrl.execute)
    thread.start()

    pass


# Variable
program = subprocess.run('dir Engine\\*.exe /b', shell=True,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE).stdout.decode().split()
program = [i.split('.exe')[0] for i in program]
version = '1.0'

# Window Setting
win = Tk()
win.geometry("")
win.resizable(0, 0)
win.iconbitmap('icon.ico')
win.title(f'Swap2 Tool for Gomoku ver {version}')

# GUI
lb1 = Label(win, text='Opening:', font=('Times New Roman', 11))
lb2 = Label(win, text='Time (sec):', font=('Times New Roman', 11))
lb3 = Label(win, text='Engine:', font=('Times New Roman', 11))
lb4 = Label(win, text='(Default is 60 seconds)', font=('Times New Roman', 10, 'italic'))
lb5 = Label(win, text='Protocol:', font=('Times New Roman', 11))
lb6 = Label(win, text='Max memory:', font=('Times New Roman', 11))
lb7 = Label(win, text='(GB) Default is 2 GB ', font=('Times New Roman', 10, 'italic'))

txbox = Entry(win, width=23)
txbox1 = Entry(win, width=23)
txbox2 = Entry(win, width=23)

combo = Combobox(win, width=20)
combo['values'] = program
combo.current(0)

combo1 = Combobox(win, width=20)
combo1['values'] = ['Gomocup protocol', 'Yixin protocol']
combo1.current(0)

scrt = scrtxt.ScrolledText(win, width=60, height=10)

button = Button(win, text='Enter', command=enter)
button1 = Button(win, text='Clear', command=clear)

# Grid
lb1.grid(column=0, row=0, sticky='W', padx=5, pady=5)
lb2.grid(column=0, row=1, sticky='W', padx=5, pady=5)
lb3.grid(column=0, row=2, sticky='W', padx=5, pady=5)
lb4.grid(column=2, row=1, sticky='W', padx=5, pady=5)
lb5.grid(column=0, row=3, sticky='W', padx=5, pady=5)
lb6.grid(column=0, row=4, sticky='W', padx=5, pady=5)
lb7.grid(column=2, row=4, sticky='W', padx=5, pady=5)

txbox.grid(column=1, row=0, sticky='W', padx=5, pady=5)
txbox1.grid(column=1, row=1, sticky='W', padx=5, pady=5)
txbox2.grid(column=1, row=4, sticky='W', padx=5, pady=5)

combo.grid(column=1, row=2, sticky='W', padx=5, pady=5)
combo1.grid(column=1, row=3, sticky='W', padx=5, pady=5)

scrt.grid(column=0, columnspan=10, row=5, sticky='WE', padx=5, pady=5)

button.grid(column=9, row=6, sticky='E', padx=5, pady=5)
button1.grid(column=8, row=6, sticky='E', padx=5, pady=5)

win.mainloop()
