import os
import tkinter as tkr
from tkinter import Button
from tkinter import END
from tkinter import filedialog

curdir = os.getcwd()


"""Create Window"""
screen = tkr.Tk()
screen.geometry("1366x768")
screen.configure(bg="#49A")
screen.title("Uz3d1t0r")


"""Define the OPEN TEXT function"""
def open_file():
	textbox1.delete('1.0', END)
	text_file = filedialog.askopenfilename()
	text_file = open(text_file, 'r')
	text = text_file.read()
	textbox1.insert(END, text)
	text_file.close()
"""Define the SAVE FILE button"""
def save_file():
	text_file = filedialog.askopenfilename()
	text_file = open(text_file, 'w')
	text_file.write(textbox1.get(1.0, END))

"""Make the text box"""
textbox1 = tkr.Text(screen, bd=2, insertborderwidth=3, width=135,height=40)


"""Make the OPEN FILE button"""
open_button = Button(screen, text="Open File", command=open_file)
open_button.grid(pady=20)

"""Make the SAVE FILE button"""
save_button = Button(screen, text="Save File", command=save_file)
save_button.place(x=45,y=20)


"""GUI LAYOUT"""
textbox1.grid(row=1,columnspan=4)


"""Activate App"""
tkr.mainloop()