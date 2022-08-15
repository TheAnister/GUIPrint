import tkinter as tk
from tkinter.ttk import Label

## Regular
def guiprint(text):
  root = tk.Tk()
  root.geometry('1000x50')
  root.resizable(False, False)
  root.title("GUIPrint")


  label = Label(root, text=text)
  label.pack(ipadx=10, ipady=10)

  root.mainloop()
 
## Customise dimensions
def guiprintd(text, dimensions):
  root = tk.Tk()
  root.geometry(str(dimensions))
  root.resizable(False, False)
  root.title("GUIPrint")


  label = Label(root, text=text)
  label.pack(ipadx=10, ipady=10)

  root.mainloop()
  
## Customise name
def guiprintn(text, name):
  root = tk.Tk()
  root.geometry("1000x50")
  root.resizable(False, False)
  root.title(name)


  label = Label(root, text=text)
  label.pack(ipadx=10, ipady=10)

  root.mainloop()

## Customise dimensions & name
def guiprintdn(text, dimensions, name):
  root = tk.Tk()
  root.geometry(str(dimensions))
  root.resizable(False, False)
  root.title(name)


  label = Label(root, text=text)
  label.pack(ipadx=10, ipady=10)

  root.mainloop()
  