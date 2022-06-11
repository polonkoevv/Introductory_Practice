from getCurrency import *
from datetime import *
from dateutil.relativedelta import relativedelta
import locale
locale.setlocale(locale.LC_TIME, "ru_RU")
import matplotlib.pyplot as plt

def week_graph(date_str, curr_name):
        
    nowDate = date(int(date_str[6:10]), int(date_str[3:5]), int(date_str[:2]))
    x_list = []
    y_list = []
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
    for i in range(7):
        x_list.append((nowDate + timedelta(days=i)).strftime("%d.%m"))   
        y_list.append(get_ex_currency(curr_name, get_data(url + (nowDate + timedelta(days=i)).strftime("%d/%m/%Y"))))
    # print(x_list)
    # print(y_list)
    # print(url + (nowDate + timedelta(days=i)).strftime("%d/%m/%Y"))
    plt.plot(x_list,y_list)



def month_graph(date_str, curr_name):

    month_number = {#Словарь месяцев
        "Январь" : 1,
        "Февраль" : 2,
        "Март" : 3,
        "Апрель" : 4,
        "Май" : 5,
        "Июнь" : 6,
        "Июль" : 7,
        "Август" : 8,
        "Сентябрь" : 9,
        "Октябрь" : 10,
        "Ноябрь" : 11,
        "Декабрь" : 12}

    s = date_str.split(' ')
    month = month_number[s[0]]
    year = int(s[1])
    # print(month)
    # print(year)

    start_date = date(year,month,1)
    
    # print(start_date)
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
    x_list = []
    y_list = []

    while int(str(start_date)[5:7]) < (month+1)%12 and start_date <= datetime.today().date():
        # print(start_date.strftime("%d/%m/%Y"))
        x_list.append(start_date.strftime("%d %b"))
        y_list.append(get_ex_currency(curr_name, get_data(url + start_date.strftime("%d/%m/%Y"))))
        start_date += timedelta(days = 4)
    # print(x_list)
    # print(y_list)
    plt.plot(x_list,y_list)



def quarter_graph(date_str, curr_name):

    month_number = {
        "Осень" : 9,
        "Зима" : 12,
        "Весна" : 3,
        "Лето" : 6
    }

    x_list = []
    y_list = []
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
    
    s = date_str.split(' ')
    month = month_number[s[0]]
    year = int(s[1])
    # print(month)
    # print(year)

    start_date = date(year,month,1)

    for i in range(3):
        x_list.append(start_date.strftime("%d %b"))
        x_list.append((start_date + timedelta(days = 14)).strftime("%d %b"))

        y_list.append(get_ex_currency(curr_name, get_data(url + start_date.strftime("%d/%m/%Y"))))
        y_list.append(get_ex_currency(curr_name, get_data(url + (start_date + timedelta(days = 14)).strftime("%d/%m/%Y"))))
        start_date+= relativedelta(months=1)
    # print(x_list)
    # print(y_list)
    plt.plot(x_list,y_list)



def year_graph(date_str, curr_name):
    start_date = date(int(date_str),1,1)

    x_list = []
    y_list = []
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='

    while start_date.year <= int(date_str) and start_date <= datetime.today().date():
        x_list.append(start_date.strftime("%b"))
        y_list.append(get_ex_currency(curr_name, get_data(url + start_date.strftime("%d/%m/%Y"))))    
        start_date+= relativedelta(months=1)
    plt.plot(x_list,y_list)

