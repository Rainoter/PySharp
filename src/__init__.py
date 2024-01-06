import tkinter
from tkinter import ttk

def write(data):
    print(data)

def form(data):
    input(data)

def integar(data):
    int(data)

def string(data):
    str(data)
#function
def boolean(data):
    bool(data)


def helloworld_app():
    import tkinter
    from tkinter import Tk
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    root.mainloop()