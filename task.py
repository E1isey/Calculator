import tkinter as tk
from tkinter import *
from tkinter.ttk import  *


def f1():
    global lol, loli
    if not lolka:
        lol += '1'
    else:
        loli +='1'

def f2():
    global lol, loli
    if not lolka:
        lol += '1'
    else:
        loli += '1'

def f3():
    global lol, loli
    if not lolka:
        lol += '1'
    else:
        loli += '1'

def f4():
    global lol, loli
    if not lolka:
        lol += '1'
    else:
        loli += '1'

def f5():
    global lol, loli
    if not lolka:
        lol += '1'
    else:
        loli += '1'

def f6():
    global lol, loli
    if not lolka:
        lol += '1'
    else:
        loli += '1'

def f7():
    global lol, loli
    if not lolka:
        lol += '1'
    else:
        loli += '1'

def f8():
    global lol, loli
    if not lolka:
        lol += '1'
    else:
        loli += '1'

def f9():
    global lol, loli
    if not lolka:
        lol += '1'
    else:
        loli += '1'

def f_pl():
    global lolka
    lolka = '+'
def f_mn():
    global lolka
    lolka = '-'
def f_eq():
    global lolka
    lolka = '='

root = Tk()
label = Label(root, text="_________________________________________________________________")
label.grid(row=0, column=0, columnspan=4)
lol = ""
loli = ""
lolka = ""
matrix = [
    [Button(text="7", command=f7), Button(text="8", command=f8), Button(text="9", command=f9), Button(text="+", command=f_pl)],
[Button(text="4", command=f4), Button(text="5", command=f5), Button(text="6", command=f6), Button(text="-", command=f_mn)],
[Button(text="1", command=f1), Button(text="2", command=f2), Button(text="3", command=f3), Button(text="=", command=f_eq)],
]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        widget = matrix[i][j]
        widget.grid(row=i+1, column=j)
root.mainloop()


