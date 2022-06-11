from tkinter import *
from tkinter.ttk import *
from datetime import *
from matplotlib import *
import matplotlib
import matplotlib.pyplot as plt
import graph_defs as gr
from getCurrency import *
from dateutil.relativedelta import relativedelta
import locale

locale.setlocale(locale.LC_TIME, "ru_RU")
window = Tk()

# window.maxsize(1000,500)
# window.minsize(500,100)
window.title("Конвертер валют")
tab_control = Notebook(window, width=700, height=300)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab_control.add(tab1, text="Калькулятор валют")
tab_control.add(tab2, text="Динамика курса")

#Parsing xml
m = str(datetime.today())[:10].replace('-','/')
d = m[-2:]+m[4:8]+m[:4]
url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='+d
curr_list = []
curr_dict = get_currencies_dictionary(get_data(url)) 
curr_dict['Рубль'] = 1
print(curr_dict)
for key in curr_dict: curr_list.append(key)


first_curr = Combobox(tab1, width=30, values=curr_list)

first_curr.grid(column=0, row=0, padx=10, pady=10)  #First combobox
first_curr.set(first_curr['value'][0])

second_curr = Combobox(tab1, values=curr_list, width=30)
second_curr.grid(column=0, row=1, padx=10, pady=10) #Second combobox
second_curr.set(second_curr['value'][0])

quant_entry = Entry(tab1)
quant_entry.grid(column=1, row=0, padx=10, pady=10) #Entry fill

fin_curr = Label(tab1,width=17)
fin_curr.grid(column=1,row=1, padx=10, pady=10)     #Currency fin

#Button
def cha():
    fin_curr.config(text=curr_dict[first_curr.get()] / curr_dict[second_curr.get()] * float(quant_entry.get().replace(',','.')))
btn_curr = Button(tab1, text="Конвертировать", command=cha)
btn_curr.grid(column=2,row=0)

#PART II - Currency dynamic 

Label(tab2, text="Валюта").grid(column=0,row=0,padx=10)        #Valute Label
Label(tab2, text="Период").grid(column=1,row=0,padx=10)        #Period Label
Label(tab2, text="Выбор периода").grid(column=2,row=0,padx=10) #Period choice Label

#Curr combobox
curr_combo = Combobox(tab2, width=30, values=curr_list)
curr_combo.grid(column=0, row=1)
curr_combo.set(curr_combo['value'][0])


## WEEK COMBOBOX
m = datetime.today()-timedelta(days=datetime.today().weekday()) #Week`s Monday
s = m+timedelta(days=6)                                         #Week`s Sunday
w_args = []
for i in range(4):
    m1=str(m-timedelta(days=i*7))[:10].replace('-','.')
    s1=str(s-timedelta(days=i*7))[:10].replace('-','.')
    m1=m1[-2:]+m1[4:8]+m1[:4]
    s1=s1[-2:]+s1[4:8]+s1[:4]
    w_args.append(m1+'-'+s1)
week_combo = Combobox(tab2, values=w_args)
week_combo.set(week_combo['value'][0])

############################################


## MONTH COMBOBOX
m_args = []
for i in range(4):m_args.append((datetime.today()-relativedelta(months=i)).strftime('%B %Y'))
global month_combo
month_combo = Combobox(tab2, values=m_args)
month_combo.set(month_combo['value'][0])

############################################


## QUARTER COMBOBOX
quarter_list=[]
for i in range(4):
    m = int(str(datetime.today() - relativedelta(months=3*i))[5:7])%12//3 
    if m == 0:
        quarter_list.append("Зима "+(datetime.today() - relativedelta(months=3*i)).strftime("%Y"))
    elif m == 1:
        quarter_list.append("Весна "+(datetime.today() - relativedelta(months=3*i)).strftime("%Y"))
    elif m == 2:
        quarter_list.append("Лето "+(datetime.today() - relativedelta(months=3*i)).strftime("%Y"))
    elif m == 3:
        quarter_list.append("Осень "+(datetime.today() - relativedelta(months=3*i)).strftime("%Y"))

quarter_combo = Combobox(tab2, values=quarter_list)
quarter_combo.set(quarter_combo['value'][0])

## YEAR COMBOBOX

year_list = []
for i in range(4):
    year_list.append(int((datetime.today()).strftime("%Y"))-i)
year_combo = Combobox(tab2, values=year_list)
year_combo.set(year_combo['value'][0])


#Radiobuttons
period = StringVar()
period.set("week")

def perCombo(value):
    week_combo.grid_forget()
    month_combo.grid_forget()
    quarter_combo.grid_forget()
    year_combo.grid_forget()
    if value == 1:
        week_combo.grid(column=2,row=1,padx=15,pady=5,sticky="WE")
    elif value == 2:
        month_combo.grid(column=2,row=2,padx=15,pady=5,sticky="WE")
    elif value == 3:
        quarter_combo.grid(column=2,row=3,padx=15,pady=5,sticky="WE")
    else:
        year_combo.grid(column=2,row=4,padx=15,pady=5,sticky="WE")


week_radio = Radiobutton(tab2,text="Неделя",variable=period,value="week",command= lambda: perCombo(1))
week_radio.grid(column=1,row=1,padx=15,pady=5)

month_radio = Radiobutton(tab2,text="Месяц",variable=period,value="month",command= lambda: perCombo(2))
month_radio.grid(column=1,row=2,padx=15,pady=5)

quarter_radio = Radiobutton(tab2,text="Квартал",variable=period,value="quarter",command= lambda: perCombo(3))
quarter_radio.grid(column=1,row=3,padx=15,pady=5)

year_radio = Radiobutton(tab2,text="Год",variable=period,value="year",command= lambda: perCombo(4))
year_radio.grid(column=1,row=4,padx=15,pady=5)


#Buid a graphic button
def build():
    matplotlib.use('TkAgg')
    fig = plt.figure()
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=tab2)
    plot_widget = canvas.get_tk_widget()
    fig.clear()

    curr = curr_combo.get()
    if period.get() == "week": 
        date_str = str(week_combo.get())
        gr.week_graph(date_str, curr)
    elif period.get() == "month": 
        date_str = str(month_combo.get())
        gr.month_graph(date_str, curr)
    elif period.get() == "quarter": 
        date_str = str(quarter_combo.get())
        gr.quarter_graph(date_str, curr)
    elif period.get() == "year": 
        date_str = str(year_combo.get())
        gr.year_graph(date_str, curr)   

    plt.grid()
    plot_widget.grid(column=3, row = 5)
    
graph_btn = Button(tab2,text="Построить график",command=build)
graph_btn.grid(column=0,row=4,sticky="WE")

tab_control.pack(expand=1, fill='both')
window.mainloop()

