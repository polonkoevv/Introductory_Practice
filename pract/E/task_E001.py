from tkinter import *
import tkinter.ttk as ttk

window = Tk()

window.title("Title")
window.geometry("100x100")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Калькулятор валют")
tab_control.add(tab2, text="Динамика курса")

combo = ttk.Combobox(tab1)
combo["values"] = ["раз", "два", "три"]
combo.grid(column=0, row=0)

txt = Entry(tab1)
btn = Button(tab1, text="Действие")
lbl = Label(tab1, text="")

tab_control.pack(expand=1, fill='both')
window.mainloop()