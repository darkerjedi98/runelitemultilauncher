import tkinter as tk
import os
import keyboard
from tkinter import *

def open():
    os.startfile(r'notepad.exe')
def open2():
    os.startfile(r'code1.py')
def open3():
    os.startfile(r'calc')
def open4():
    os.startfile(r'RuneLite.exe')
def open5():
    os.startfile(r'RuneLite.exe')
    os.startfile(r'RuneLite.exe')

HEIGHT = 220
WIDTH = 270

root = tk.Tk()
root.title("Darkerjedi's Launcher")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,)
canvas.pack()

background_image = tk.PhotoImage(file='image.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


button = tk.Button(root, text="classic multi launcher", bg='green', fg='black', height=3, width=17, command=open2)

button.pack(side='left')

button = tk.Button(root, text="Runelite", bg='green', fg='black', height=3, width=17, command=open4)

button.pack(side='left')


button = tk.Button(root, text="notepad", bg='green', fg='black', height=3, width=7, command=open)

button.pack(side='right')

button = tk.Button(root, text="calc", bg='green', fg='black', height=3, width=5, command=open3)

button.pack(side='right')

button = tk.Button(root, text="launch 2 runelite's", bg='green', fg='black', height=3, width=17, command=open5)

button.pack(side='left')

root.mainloop()