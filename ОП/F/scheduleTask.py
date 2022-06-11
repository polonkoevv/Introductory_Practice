import openpyxl
import requests
import datetime

from bs4 import BeautifulSoup
from datetime import datetime as dt
import locale

locale.setlocale(locale.LC_TIME, "ru_RU")

def get_schedule_xlsx():
    #Getting links 
    soup = BeautifulSoup((requests.get('https://www.mirea.ru/schedule/')).text, "html.parser") 
    link_dom = soup.find(string = "Институт информационных технологий")\
        .find_parent("div")\
            .find_parent("div")\
                .find_all("a", class_='uk-link-toggle')
    links = []
    for link in link_dom:
        links.append(link['href'])
    #Getting xlsx with links and writing into files
    for x in links: 
        if x.find('ИИТ_1') > 0:
            f = open("F\\first_course.xlsx", "wb")  # открываем файл для записи, в режиме wb 
            resp = requests.get(x)  # запрос по ссылке 
            f.write(resp.content)
        elif x.find('ИИТ_2') > 0:
            f = open("F\\second_course.xlsx", "wb")  # открываем файл для записи, в режиме wb 
            resp = requests.get(x)  # запрос по ссылке 
            f.write(resp.content)
        elif x.find('ИИТ_3') > 0:
            f = open("F\\third_course.xlsx", "wb")  # открываем файл для записи, в режиме wb 
            resp = requests.get(x)  # запрос по ссылке 
            f.write(resp.content)
    
book = openpyxl.open('F\\second_course.xlsx', read_only = False)

sheet = book.active

parity = 1
group_name = "ИКБО-01-20"

def check_group(group_name):
    year = 22-int(group_name[-2:])
    if year == 1:
        book = openpyxl.open('F\\first_course.xlsx', read_only = False)
    elif year == 2:
        book = openpyxl.open('F\\second_course.xlsx', read_only = False)
    elif year == 3:
        book = openpyxl.open('F\\third_course.xlsx', read_only = False)
    sheet = book.active
    for col in range(0,sheet.max_column):
        if sheet[2][col].value == group_name:
            print (col)
            return col
    return 0

def check_week_number():
    
    return ((dt.today().date()-datetime.date(2022,2,9))).days//7+1

def week_schedule_print(group_name,parity, col):
    year = 22-int(group_name[-2:])
    if year == 1:
        book = openpyxl.open('F\\first_course.xlsx', read_only = False)
    elif year == 2:
        book = openpyxl.open('F\\second_course.xlsx', read_only = False)
    elif year == 3:
        book = openpyxl.open('F\\third_course.xlsx', read_only = False)
    sheet = book.active
    sch = open('F\\schedule.txt', 'w',encoding='utf-8')
    a = dt.today() - datetime.timedelta(days = dt.today().weekday())
    parity = 4 + (parity//2)
    print(group_name)
    schedule = {}
    if sheet[2][col].value == group_name:
        for row in range(parity,75+1,2):
            #{str(sheet[row-row%2][0].value).lower()}
            if sheet[row-row%2][1].value == 1:
                sch.write(
                    '\n' + f'Расписание на {a.strftime("%A %d %B").lower()}' + '\n'
                )
                
                
            s = str(sheet[row-row%2][1].value) + ' ' + \
                str(sheet[row][col].value).replace('\n',' ').replace('None','-') + ' ' + \
                str(sheet[row][col+1].value).replace('\n',' ').replace('None','') + ' ' + \
                str(sheet[row][col+2].value).replace('\n',' ').replace('None','') + ' ' + \
                str(sheet[row][col+3].value).replace('\n',' ').replace('None','') + '\n'
            if sheet[row-row%2][1].value == 1:
               schedule[f'Расписание на {a.strftime("%A %d %B").lower()}'] = s
               a+=datetime.timedelta(days=1)
            sch.write(s)

    return schedule
# col = check_group(group_name)


# a = week_schedule_print(group_name, check_week_number()%2, sheet, col)


def get_today_schedule(group_name,parity,col,this=0):
    week_schedule_print(group_name,parity, col)
    a_file = open("F/schedule.txt", 'r+', encoding='UTF8')
    s = a_file.readline()
    f = dt.today().weekday() + this
    string = ''
    start = f*8
    end = start+7
    counter = 0
    for s in a_file:
        if counter >= start and counter <= end:
            string += s
        counter+=1
    return string

def get_day_shedule(group_name, col,day):
    daynum = {
        "понедельник" : 0,
        "вторник" : 1,
        "среда" : 2,
        "четверг" : 3,
        "пятница" : 4,
        "суббота" : 5
    }
    parity = 1
    week_schedule_print(group_name,parity, col)
    a_file = open("F/schedule.txt", 'r+', encoding='UTF8')
    s = a_file.readline()
    f = daynum[day]
    string = ''
    start = f*8
    end = start+7
    counter = 0
    for s in a_file:
        if counter >= start and counter <= end:
            string += s
        counter+=1
    a_file.close()

    parity = 2
    counter = 0
    week_schedule_print(group_name,parity, col)
    b_file = open("F/schedule.txt", 'r+', encoding='UTF8')
    s1 = b_file.readline()
    for s1 in b_file:
        if counter >= start and counter <= end:
            string += s1
        counter+=1
    b_file.close()
    return string
