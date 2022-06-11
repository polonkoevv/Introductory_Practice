import datetime
import json
import math
import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardButton,VkKeyboardColor
from translate import Translator
import PIL.Image as Image
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from bs4 import BeautifulSoup
# import GetRaspisanie
# from GetRaspisanie import raspisanie1,raspisanie2

my_file=open("raspisanie1.json",'r')
my_file2=open('raspisanie2.json','r')
raspisanie1=my_file.read()
raspisanie1=json.loads(raspisanie1)
raspisanie2=my_file2.read()
raspisanie2=jo=json.loads(raspisanie2)
my_file=open("raspisanie_for_teacher1.json",'r')

raspisanie_for_teacher1=my_file.read()
raspisanie_for_teacher1=json.loads(raspisanie_for_teacher1)
my_file=open("raspisanie_for_teacher2.json",'r')

raspisanie_for_teacher2=my_file.read()
raspisanie_for_teacher2=json.loads(raspisanie_for_teacher2)
import re
group={}
num={}
group_current={}
teacher_current={}
regtire=r"([0-9]+)-([0-9]+)"
def deriction_def(x):

    deriction = ['северный', 'северо-восточный', "восточный", "юго-восточный", "южный", "юго-западный",
                 "западный", 'cеверо-западный']
    if x> (360 - 22.5):
        derictionC = deriction[0]
    else:
        derictionC = deriction[math.ceil((x + 22.5) / 45) - 1]
    return derictionC
def sspeed_def(speed):

    sspeed = ""
    if speed < 0.2:
        sspeed = "Штиль"
    elif speed < 1.5:
        sspeed = "Тихий"
    elif speed < 3.3:
        sspeed = "Легкий"
    elif speed < 5.4:
        sspeed = "Слабый"
    elif speed < 7.9:
        sspeed = "Умеренный"
    elif speed < 10.7:
        sspeed = "Свежий"
    elif speed < 13.8:
        sspeed = "Сильный"
    elif speed < 17.1:
        sspeed = "Крепкий"
    elif speed < 20.7:
        sspeed = "Очень крепкий"
    elif speed < 24.4:
        sspeed = "Шторм"
    elif speed < 28.4:
        sspeed = "Сильный шторм"
    elif speed < 32.6:
        sspeed = "Жестокий шторм"
    elif speed > 33:
        sspeed = "Умеренный"
    return sspeed
def translate(words):


    traslator = Translator(from_lang='en', to_lang="ru")
    description = traslator.translate(words)

    sss = re.findall("[А-Яа-яеЁ]+", description)
    ss = ""
    for i in sss:
        ss += i + " "

    # if len(ss)==0:
    #     ss=translate(description)

    return ss[:len(ss) - 1]
def check(s,parity):
    print("Получили",s)
    n=get_week()
    if n%2!=parity%2:
        n+=1

    if s.find(" н.")==-1:
        print("Отдали1", s)
        return s
    else:
        ss=s+'\n '
        s=""
        while(True):

            if ss.find(" н.")==-1:
                s+=ss[:ss.find("\n")]+'\n'
                ss=ss[(ss.find("\n") + 1):]
                if len(ss)<3:
                    break
                continue
            if ss.find("\n")==-1:
                break
            if ss[:ss.find("\n")].find("кр.")!=-1:

                if ss[ss.find("кр."):ss.find(" н.")].find("-")!=-1:
                    a1=int(re.search(regtire, ss).group()[:re.search(regtire, ss).group().find("-")])
                    a2=int(re.search(regtire, ss).group()[re.search(regtire, ss).group().find("-")+1:])
                    if n<=a2 and n>=a1:
                        ss=ss[ss.find("\n")+1:]
                        continue
                a3 = re.findall('[0-9]+', ss)
                for i in a3:
                    if int(i) == n:
                        ss = ss[ss.find("\n")+1:]
                        continue
                s+=ss[:ss.find("\n")]+'\n'
                ss=ss[ss.find("\n")+1:]
            else:
                if ss[:ss.find("\n")][:ss.find(" н.")].find("-") != -1:

                    a1 = int(re.search(regtire, ss).group()[:re.search(regtire, ss).group().find("-")])
                    a2 = int(re.search(regtire, ss).group()[re.search(regtire, ss).group().find("-") + 1:])
                    if n<=a2 and n>=a1:
                        s+=ss[:ss.find("\n")]+'\n'
                        ss = ss[ss.find("\n") + 1:]
                        continue
                    else:
                        ss=ss[ss.find("\n")+1:]
                        continue
                print(ss)

                a3 = re.findall('[0-9]+', ss)
                for i in a3:
                    if int(i) == n:
                        s += ss[:ss.find("\n")] + '\n'
                ss=ss[ss.find("\n") + 1:]
                print(ss)
    print("Отдали",s)
    return s


def GetStrRaspisanie(raspisanie,dayweek=-1, parity=1):
    k=1
    s=''
    if dayweek==-1:
        for i in raspisanie:
            s+=i+"\n"
            for i1 in raspisanie[i]:

                s+=str(k)+")"+check(i1,parity)+"\n"
                k+=1
            k=1
        return s
    elif dayweek==6:

        for i in raspisanie:

            s+=i+"\n"
            for i1 in raspisanie[i]:

                s+=str(k)+") "+check(i1, parity)+"\n"
                k+=1
            return s
    else:

        s += list(raspisanie.keys())[dayweek] + "\n"
        for i in list(raspisanie.values())[dayweek]:

            s+=str(k)+") "+check(i,parity)+"\n"
            k+=1
        return s


def get_week():
    daynow=datetime.datetime.today()
    daystart=datetime.datetime(day=6,month=2,year=datetime.datetime.today().year)
    timedelta=daynow-daystart

    return math.ceil(timedelta.days/7)
# def send_message_if_command_bot(groupe):
#     for event in VkLongPoll(vk_session).listen():
#         if event.type==VkEventType.MESSAGE_NEW and event.to_me:
#             if event.text=="Какая группа?":
#                 vk.messages.send(
#
#                     user_id=event.user_id,
#                     random_id=get_random_id(),
#
#                     message=groupe)
#                 break
#             elif event.text=="Какая неделя?":
#
#                 vk.messages.send(
#
#                     user_id=event.user_id,
#                     random_id=get_random_id(),
#
#                     message=get_week())
#                 break
#             elif event.text=="На сегодня":
#                 if get_week()>17:
#                     vk.messages.send(
#
#                         user_id=event.user_id,
#                         random_id=get_random_id(),
#
#                         message="Сейчас нет пар")
#                     break
#                 elif get_week()%2==0:
#                     raspisanie=raspisanie2
#                     parity=2
#                 else:
#                     raspisanie=raspisanie1
#                     parity=1
#
#
#                 if datetime.datetime.today().weekday()==6:
#                     if get_week() % 2 == 0:
#                         vk.messages.send(
#
#                             user_id=event.user_id,
#                             random_id=get_random_id(),
#
#                             message="Сейч
# 
# 
# 
# ас воскресение, пар нет, вот  расписание на понедельник:\n"\
#                                     +GetStrRaspisanie(raspisanie1[groupe], 6,1))
#                         break
#                     else:
#
#                         vk.messages.send(
#
#                             user_id=event.user_id,
#                             random_id=get_random_id(),
#
#                             message="Сейчас воскресение, пар нет, вот  расписание на понедельник:\n" \
#
#                                     + GetStrRaspisanie(raspisanie2[groupe], 6,2))
#                         break
#                 else:
#
#                     vk.messages.send(
#
#                         user_id=event.user_id,
#                         random_id=get_random_id(),
#
#                         message= GetStrRaspisanie(raspisanie[groupe],datetime.datetime.today().weekday(),parity))
#                     break
#
#             elif event.text=="На завтра":
#                 if get_week()>17:
#                     vk.messages.send(
#
#                         user_id=event.user_id,
#                         random_id=get_random_id(),
#
#                         message="Сейчас нет пар")
#                     break
#                 elif get_week()%2==0:
#                     raspisanie=raspisanie2
#                     parity=2
#                 else:
#                     raspisanie=raspisanie1
#                     parity=1
#
#
#                 if datetime.datetime.today().weekday()==5:
#                     if get_week() % 2 == 0:
#                         vk.messages.send(
#
#                             user_id=event.user_id,
#                             random_id=get_random_id(),
#
#                             message="Завтра воскресение, пар нет, вот  расписание на понедельник:\n"\
#                                     +GetStrRaspisanie(raspisanie1[groupe], 6, 1))
#                         break
#                     else:
#
#                         vk.messages.send(
#
#                             user_id=event.user_id,
#                             random_id=get_random_id(),
#
#                             message="Завтра воскресение, пар нет, вот  расписание на понедельник:\n" \
#
#                                             + GetStrRaspisanie(raspisanie2[groupe], 6, 2))
#                         break
#                 else:
#                     if datetime.datetime.today().weekday()==6:
#                         weekd=0
#                         if get_week()%2==0:
#                             raspisanie=raspisanie1
#                             parity=1
#                         else:
#                             raspisanie=raspisanie2
#                             parity=2
#                     else:
#                             weekd=datetime.datetime.today().weekday()
#
#                             vk.messages.send(
#
#                                 user_id=event.user_id,
#                                 random_id=get_random_id(),
#
#                                 message= GetStrRaspisanie(raspisanie[groupe],weekd+1,parity))
#                     break
#
#
#             elif event.text=="На эту неделю":
#                 if get_week()>17:
#                     vk.messages.send(
#
#                         user_id=event.user_id,
#                         random_id=get_random_id(),
#
#                         message="Сейчас нет пар")
#                     break
#                 elif get_week()%2==0:
#                     raspisanie=raspisanie2
#                     parity=2
#                 else:
#                     raspisanie=raspisanie1
#                     parity=1
#                 vk.messages.send(
#
#                     user_id=event.user_id,
#                     random_id=get_random_id(),
#
#                     message=GetStrRaspisanie(raspisanie[groupe],parity=parity))
#                 break
#
#             elif event.text=="На следующую неделю":
#                 if get_week()>16:
#                     vk.messages.send(
#
#                         user_id=event.user_id,
#                         random_id=get_random_id(),
#
#                         message="Сейчас нет пар")
#                     break
#                 elif get_week()%2==0:
#                     raspisanie=raspisanie1
#                     parity=1
#                 else:
#                     raspisanie=raspisanie2
#                     parity=2
#                 vk.messages.send(
#
#                     user_id=event.user_id,
#                     random_id=get_random_id(),
#
#                     message=GetStrRaspisanie(raspisanie[groupe],parity=parity))
#                 break
#

def StrWeekDay(raspisanie1,raspisanie2):
    s="Расписание на нечетную неделю\n"
    k=1
    for i in raspisanie1:
        s+=str(k)+') '+i+'\n'
        k+=1
    s += "\n\n\nРасписание на четную неделю\n"
    k = 1
    for i in raspisanie2:
        s+=str(k)+') '+i+'\n'
        k+=1
    return s
# def command_bot(user_id,random_id,groupe=''):
#
#
#     keyboard=VkKeyboard(one_time=True)
#     keyboard.add_button('На сегодня', VkKeyboardColor.POSITIVE)
#     keyboard.add_button('На завтра',VkKeyboardColor.NEGATIVE)
#     keyboard.add_line()
#     keyboard.add_button('На эту неделю', VkKeyboardColor.PRIMARY)
#     keyboard.add_button('На следующую неделю', VkKeyboardColor.PRIMARY)
#     keyboard.add_line()
#     keyboard.add_button('Какая неделя?', VkKeyboardColor.SECONDARY)
#     keyboard.add_button('Какая группа?', VkKeyboardColor.SECONDARY)
#
#     vk.messages.send(
#
#         user_id=user_id,
#         random_id=random_id,
#         keyboard=keyboard.get_keyboard(),
#         message="Показать расписание")
#     if groupe=='':
#
#         send_message_if_command_bot(group[user_id])
#     else:
#         send_message_if_command_bot(groupe)
#                 # +str(list(raspisanie1[group[user_id]].items())[datetime.date.today().weekday()]))
#


# send_message_if_command_search(teacher)
vk_session=vk_api.VkApi(token="0a4fe5d3a71e49be0237d1ad5eb9ee7ae555306ed317a6b381327c50ebc854142fe2b82121f649dfe79a3")
vk=vk_session.get_api()

prov=0
def main():
    reg = r"^([а-яА-Я])([а-яА-Я])(б|Б)(о|О)-([0-9])([0-9])-(19|20|21)"
    longpoll=VkLongPoll(vk_session)
    for event in longpoll.listen():
        # все
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.user_id not in num:

            num.setdefault(event.user_id, 0)
            print(num)
        if event.type==VkEventType.MESSAGE_NEW and event.to_me and (event.text.lower()=="привет" or event.text.lower()=="начать")\
                 and num[event.user_id]==0:
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Привет, ' + vk.users.get(user_id=event.user_id)[0]['first_name']+'. \n\
Команды, который воспринимает бот:\n\n\n\
Номер группы в формате ****-**-**  ---- Бот запоминает группу\
(например, при вводе "ИКБО-08-21" бот запоминает группу ИКБО-08-21).\n\n\n\
"Бот"---- выводит расписание.\n\n\n\
Бот понедельник (или любой другой день недели) ---- выводит расписание запомненной группы на введенный день недели\
(Например, при вводе "Бот вторник" бот выводит расписание запомненной группы на понедельник).\n\n\n\
Бот и Номер группы в формате ****-**-**  ---- выводит расписание введенной группы\
(например, при вводе "Бот ИКБО-08-21" бот выводит рассписание группы  ИКБО-08-21).\n\n\n\
Бот день недели и группа(например:"Бот понедельник Икбо-08-21") ---- бот выводит расписание введенной группы на введенный день.\
(Например, при вводе "Бот вторник ИВБО-01-20" бот выведет расписание ИВБО-01-20 на вторник).\n\n\n\
При команде найти ищет расписание введенного преподавателя\n\n\n\
При команде погода вывод погоду на выбранный период\n\n\n\nПри вводе корона выводит статистику по короновирусу'

            )
        # все
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and  re.search(reg,event.text)!=None and num[event.user_id]==0:
            if (event.text[:4].upper()+event.text[4:]) in raspisanie1:
                group[event.user_id]=event.text[:4].upper()+event.text[4:]


                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message="Я запомнил, что ты из группы "+event.text

                )
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message="Такой группы нет, укажите группу заново"

                )
                continue
            group[event.user_id] = event.text[:4].upper() + event.text[4:]
        elif event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text.lower()=="бот" and num[event.user_id]==0:
            if event.user_id in group:
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('На сегодня', VkKeyboardColor.POSITIVE)
                keyboard.add_button('На завтра', VkKeyboardColor.NEGATIVE)
                keyboard.add_line()
                keyboard.add_button('На эту неделю', VkKeyboardColor.PRIMARY)
                keyboard.add_button('На следующую неделю', VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button('Какая неделя?', VkKeyboardColor.SECONDARY)
                keyboard.add_button('Какая группа?', VkKeyboardColor.SECONDARY)

                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message="Показать расписание")
                num[event.user_id]=1
            else:
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message="Вы не указали группу")
                continue

        elif event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text[:3].lower()=="бот" \
                and re.search(reg,event.text[4:])!=None and num[event.user_id]==0:
            if str(event.text[4:8]).upper() + str(event.text[8:]) in raspisanie1:
                group_current[event.user_id]=str(event.text[4:8]).upper() + str(event.text[8:])
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('На сегодня', VkKeyboardColor.POSITIVE)
                keyboard.add_button('На завтра', VkKeyboardColor.NEGATIVE)
                keyboard.add_line()
                keyboard.add_button('На эту неделю', VkKeyboardColor.PRIMARY)
                keyboard.add_button('На следующую неделю', VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button('Какая неделя?', VkKeyboardColor.SECONDARY)
                keyboard.add_button('Какая группа?', VkKeyboardColor.SECONDARY)

                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message="Показать расписание")
                num[event.user_id]=2
                # command_bot(event.user_id,get_random_id(),str(event.text[4:8]).upper()+str(event.text[8:]))
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message="Такой группы нет, укажите группу заново"

                )
        # все
        elif event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text[:3].lower()=="бот"\
            and re.search(reg,event.text[len(event.text)-10:])!=None and num[event.user_id]==0:

            if str(event.text[len(event.text)-10:len(event.text)-6]).upper() + str(event.text[len(event.text)-6:]) in raspisanie1 and\
                    event.text[4:len(event.text)-11].upper() in raspisanie1["ИВБО-01-21"]:
                s=StrWeekDay(raspisanie1[event.text[len(event.text)-10:len(event.text)-6].upper() + str(event.text[len(event.text)-6:])]\
                      [event.text[4:len(event.text)-11].upper()],raspisanie2[event.text[len(event.text)-10:len(event.text)-6].upper() + str(event.text[len(event.text)-6:])]\
                      [event.text[4:len(event.text)-11].upper()])
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=s

                )
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message="Неверно указана группа или день недели"

                )
        # все
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text[:3].lower() == "бот" \
             and len(event.text)>=9 and num[event.user_id]==0:

            if event.user_id in group and event.text[4:].upper() in raspisanie1["ИВБО-01-21"]:
                s = StrWeekDay(raspisanie1[group[event.user_id]][event.text[4:].upper()], raspisanie2[group[event.user_id]] \
                                   [event.text[4:].upper()])
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=s

                )
            elif event.user_id not in group :
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message="Для начала укажите группу")
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message="Неверно указан день недели"

                )
        # все
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text[:5].lower() == "найти" and num[event.user_id]==0:
            teachers=[]
            print("Препод")
            for i in raspisanie_for_teacher1:


                if event.text[6:].lower() in i.lower():
                    teachers.append(i)
            if len(teachers)==1:
                print("1")
                teacher_current[event.user_id]=teachers[0]
                num[event.user_id]=3
                print(num)
                keyboard=VkKeyboard(one_time=True)
                keyboard.add_button('На сегодня', VkKeyboardColor.POSITIVE)
                keyboard.add_button('На завтра',VkKeyboardColor.NEGATIVE)
                keyboard.add_line()
                keyboard.add_button('На эту неделю', VkKeyboardColor.PRIMARY)
                keyboard.add_button('На следующую неделю', VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button('Какая неделя?', VkKeyboardColor.SECONDARY)

                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message="Показать расписание")
                continue
            elif len(teachers)>1:

                keyboard = VkKeyboard(one_time=True)
                for i1 in range(len(teachers)):
                    keyboard.add_button(teachers[i1], color= VkKeyboardColor.POSITIVE)
                    if i1!=len(teachers)-1:
                        keyboard.add_line()

                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message="Выберите преподавтеля")
                num[event.user_id]=5

            else:
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message="Преподаватель не найден")

        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text.lower() == "погода" and num[event.user_id]==0:
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Сейчас', VkKeyboardColor.POSITIVE)
            keyboard.add_button('Сегодня', VkKeyboardColor.POSITIVE)
            keyboard.add_button('На завтра', VkKeyboardColor.POSITIVE)
            keyboard.add_line()

            keyboard.add_button('На 5 дней', VkKeyboardColor.PRIMARY)



            vk.messages.send(

                user_id=event.user_id,
                random_id=get_random_id(),
                keyboard=keyboard.get_keyboard(),
                message="Показать погоду в Москве")
            num[event.user_id]=4
        # все
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and num[event.user_id]==3:
            print("2")
            groupe=teacher_current[event.user_id]
            parity=0
            if event.text=="Какая неделя?":

                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message=get_week())

            elif event.text=="На сегодня":
                if get_week()>17:
                    vk.messages.send(

                        user_id=event.user_id,
                        random_id=get_random_id(),

                        message="Сейчас нет пар")

                elif get_week()%2==0:
                    raspisanie=raspisanie_for_teacher2
                    parity=2
                else:
                    raspisanie=raspisanie_for_teacher1
                    parity=1


                if datetime.datetime.today().weekday()==6:
                    if get_week() % 2 == 0:
                        vk.messages.send(

                            user_id=event.user_id,
                            random_id=get_random_id(),

                            message="Сейчас воскресение, пар нет, вот  расписание на понедельник:\n"\
                                    +GetStrRaspisanie(raspisanie_for_teacher1[groupe], 6,1))

                    else:

                        vk.messages.send(

                            user_id=event.user_id,
                            random_id=get_random_id(),

                            message="Сейчас воскресение, пар нет, вот  расписание на понедельник:\n" \

                                    + GetStrRaspisanie(raspisanie_for_teacher2[groupe], 6,2))

                else:

                    vk.messages.send(

                        user_id=event.user_id,
                        random_id=get_random_id(),

                        message= GetStrRaspisanie(raspisanie[groupe],datetime.datetime.today().weekday(),parity))


            elif event.text=="На завтра":

                if get_week()>17:
                    vk.messages.send(

                        user_id=event.user_id,
                        random_id=get_random_id(),

                        message="Сейчас нет пар")

                elif get_week()%2==0:
                    raspisanie=raspisanie_for_teacher2
                    parity=2
                else:
                    raspisanie=raspisanie_for_teacher1
                    parity=1


                if datetime.datetime.today().weekday()==5:
                    if get_week() % 2 == 0:
                        vk.messages.send(

                            user_id=event.user_id,
                            random_id=get_random_id(),

                            message="Завтра воскресение, пар нет, вот  расписание на понедельник:\n"\
                                    +GetStrRaspisanie(raspisanie_for_teacher1[groupe], 6, 1))

                    else:

                        vk.messages.send(

                            user_id=event.user_id,
                            random_id=get_random_id(),

                            message="Завтра воскресение, пар нет, вот  расписание на понедельник:\n" \

                                            + GetStrRaspisanie(raspisanie_for_teacher2[groupe], 6, 2))

                else:
                    if datetime.datetime.today().weekday()==6:
                        weekd=0
                        if get_week()%2==0:
                            raspisanie=raspisanie_for_teacher1
                            parity=1
                        else:
                            raspisanie=raspisanie_for_teacher2
                            parity=2


                    weekd=datetime.datetime.today().weekday()

                    vk.messages.send(

                            user_id=event.user_id,
                            random_id=get_random_id(),

                            message= GetStrRaspisanie(raspisanie[groupe],weekd+1,parity))



            elif event.text=="На эту неделю":
                if get_week()>17:
                    vk.messages.send(

                        user_id=event.user_id,
                        random_id=get_random_id(),

                        message="Сейчас нет пар")

                elif get_week()%2==0:
                    raspisanie=raspisanie_for_teacher2
                    parity=2
                else:
                    raspisanie=raspisanie_for_teacher1
                    parity=1
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message=GetStrRaspisanie(raspisanie[groupe],parity=parity))


            elif event.text=="На следующую неделю":
                if get_week()>16:
                    vk.messages.send(

                        user_id=event.user_id,
                        random_id=get_random_id(),

                        message="Сейчас нет пар")

                elif get_week()%2==0:
                    raspisanie=raspisanie_for_teacher1
                    parity=1
                else:
                    raspisanie=raspisanie_for_teacher2
                    parity=2
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message=GetStrRaspisanie(raspisanie[groupe],parity=parity))

            else:
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message="Неизвестная команда")
            num[event.user_id]=0
       # все
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and num[event.user_id]==5:
            if event.text in raspisanie_for_teacher1 or raspisanie_for_teacher2:
                teacher_current[event.user_id]=event.text
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('На сегодня', VkKeyboardColor.POSITIVE)
                keyboard.add_button('На завтра', VkKeyboardColor.NEGATIVE)
                keyboard.add_line()
                keyboard.add_button('На эту неделю', VkKeyboardColor.PRIMARY)
                keyboard.add_button('На следующую неделю', VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button('Какая неделя?', VkKeyboardColor.SECONDARY)

                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message="Показать расписание")
                num[event.user_id]=3
            else:
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message="Неизвестная команда")
        elif event.type==VkEventType.MESSAGE_NEW and event.to_me and (num[event.user_id]==2 or num[event.user_id]==1):
            if num[event.user_id]==1:
                groupe=group[event.user_id]
            else:
                groupe=group_current[event.user_id]
            if event.text=="Какая группа?":
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message=groupe)

            elif event.text=="Какая неделя?":

                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message=get_week())

            elif event.text=="На сегодня":
                if get_week()>17:
                    vk.messages.send(

                        user_id=event.user_id,
                        random_id=get_random_id(),

                        message="Сейчас нет пар")

                elif get_week()%2==0:
                    raspisanie=raspisanie2
                    parity=2
                else:
                    raspisanie=raspisanie1
                    parity=1


                if datetime.datetime.today().weekday()==6:
                    if get_week() % 2 == 0:
                        vk.messages.send(

                            user_id=event.user_id,
                            random_id=get_random_id(),

                            message="Сейчас воскресение, пар нет, вот  расписание на понедельник:\n"\
                                    +GetStrRaspisanie(raspisanie1[groupe], 6,1))

                    else:

                        vk.messages.send(

                            user_id=event.user_id,
                            random_id=get_random_id(),

                            message="Сейчас воскресение, пар нет, вот  расписание на понедельник:\n" \

                                    + GetStrRaspisanie(raspisanie2[groupe], 6,2))

                else:

                    vk.messages.send(

                        user_id=event.user_id,
                        random_id=get_random_id(),

                        message= GetStrRaspisanie(raspisanie[groupe],datetime.datetime.today().weekday(),parity))


            elif event.text=="На завтра":
                if get_week()>17:
                    vk.messages.send(

                        user_id=event.user_id,
                        random_id=get_random_id(),

                        message="Сейчас нет пар")

                elif get_week()%2==0:
                    raspisanie=raspisanie2
                    parity=2
                else:
                    raspisanie=raspisanie1
                    parity=1


                if datetime.datetime.today().weekday()==5:
                    if get_week() % 2 == 0:
                        vk.messages.send(

                            user_id=event.user_id,
                            random_id=get_random_id(),

                            message="Завтра воскресение, пар нет, вот  расписание на понедельник:\n"\
                                    +GetStrRaspisanie(raspisanie1[groupe], 6, 1))

                    else:

                        vk.messages.send(

                            user_id=event.user_id,
                            random_id=get_random_id(),

                            message="Завтра воскресение, пар нет, вот  расписание на понедельник:\n" \

                                            + GetStrRaspisanie(raspisanie2[groupe], 6, 2))

                else:
                    if datetime.datetime.today().weekday()==6:
                        weekd=0
                        if get_week()%2==0:
                            raspisanie=raspisanie1
                            parity=1
                        else:
                            raspisanie=raspisanie2
                            parity=2
                    else:
                            weekd=datetime.datetime.today().weekday()

                            vk.messages.send(

                                user_id=event.user_id,
                                random_id=get_random_id(),

                                message= GetStrRaspisanie(raspisanie[groupe],weekd+1,parity))



            elif event.text=="На эту неделю":
                if get_week()>17:
                    vk.messages.send(

                        user_id=event.user_id,
                        random_id=get_random_id(),

                        message="Сейчас нет пар")

                elif get_week()%2==0:
                    raspisanie=raspisanie2
                    parity=2
                else:
                    raspisanie=raspisanie1
                    parity=1
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message=GetStrRaspisanie(raspisanie[groupe],parity=parity))


            elif event.text=="На следующую неделю":
                if get_week()>16:
                    vk.messages.send(

                        user_id=event.user_id,
                        random_id=get_random_id(),

                        message="Сейчас нет пар")

                elif get_week()%2==0:
                    raspisanie=raspisanie1
                    parity=1
                else:
                    raspisanie=raspisanie2
                    parity=2
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message=GetStrRaspisanie(raspisanie[groupe],parity=parity))
            else:
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message='Неизвестная команда')

            num[event.user_id]=0
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and num[event.user_id]==4:
            respons = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=moscow&appid=93e83956c91b2e00ebbabe0672230693&units=metric")
            respons = respons.json()
            responses = requests.get(
                "http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=93e83956c91b2e00ebbabe0672230693&units=metric")
            responses = responses.json()
            print(event.text.lower())
            vk.messages.send(

                user_id=event.user_id,
                random_id=get_random_id(),

                message="Ожидайте...")
            if event.text.lower()=="сейчас":

                upload=VkUpload(vk_session)
                attachemens=[]
                image=requests.get("http://openweathermap.org/img/wn/{}@2x.png".format(responses['weather'][0]['icon']), stream=True)
                print("http://openweathermap.org/img/wn/{}@2x.png".format(responses['weather'][0]['icon']))
                photo=upload.photo_messages(photos=image.raw)[0]
                attachemens.append("photo{}_{}".format(photo["owner_id"],photo['id']))
                derictionC = deriction_def(responses['wind']['deg'])
                print(derictionC)
                traslator = Translator(from_lang='en', to_lang="ru")
                print(attachemens)
                sspeed = sspeed_def(responses['wind']['speed'])

                ss = translate(responses['weather'][0]['description'])
                s = "{0} , температура: {1}-{2} °С\nОщущается: {8}\nДавление: {3} мм рт. ст., влажность: {4}%\nВетер: {5}, {6} м/с, {7}". \
                    format(ss, round(responses["main"]["temp_min"]), round(responses["main"] \
                                                                              ["temp_max"]),
                           round(responses['main']['pressure'] / 1.33), responses['main'] \
                               ['humidity'], sspeed, responses['wind']['speed'], derictionC,
                           responses['main']['feels_like'])

                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),
                    attachment=attachemens[0],
                    message="Погода сейчас:\n"+s)
            elif event.text.lower()=="сегодня":
                print(13)
                for i in range(len(respons["list"])):
                    if str(datetime.date.today()) in respons["list"][i]["dt_txt"]:

                        if "03:00:00" in respons["list"][i]["dt_txt"]:
                            response = respons["list"][i]
                            upload = VkUpload(vk_session)
                            attachemens = []
                            image = requests.get(
                                "http://openweathermap.org/img/wn/{}@2x.png".format(response['weather'][0]['icon']),
                                stream=True)

                            photo = upload.photo_messages(photos=image.raw)[0]
                            print(photo)
                            attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
                            derictionC = deriction_def(response['wind']['deg'])

                            traslator = Translator(from_lang='en', to_lang="ru")

                            sspeed = sspeed_def(response['wind']['speed'])

                            ss = translate(response['weather'][0]['description'])
                            s = "{0} , температура: {1} °С\nОщущается: {7}\nДавление: {2} мм рт. ст., влажность: {3}%\nВетер: {4}, {5} м/с, {6}". \
                                format(ss, round(response["main"]["temp"]),
                                       round(response['main']['pressure'] / 1.33), response['main'] \
                                           ['humidity'], sspeed, response['wind']['speed'], derictionC,
                                       response['main']['feels_like'])
                            vk.messages.send(

                                user_id=event.user_id,
                                random_id=get_random_id(),
                                attachment=attachemens[0],
                                message="ночь:\n" + s)

                        if "09:00:00" in respons["list"][i]["dt_txt"]:
                            response = respons["list"][i]
                            upload = VkUpload(vk_session)
                            attachemens = []
                            image = requests.get(
                                "http://openweathermap.org/img/wn/{}@2x.png".format(response['weather'][0]['icon']),
                                stream=True)
                            photo = upload.photo_messages(photos=image.raw)[0]
                            attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
                            derictionC = deriction_def(response['wind']['deg'])

                            traslator = Translator(from_lang='en', to_lang="ru")

                            sspeed = sspeed_def(response['wind']['speed'])

                            ss = translate(response['weather'][0]['description'])
                            s = "{0} , температура: {1} °С\nОщущается: {7}\nДавление: {2} мм рт. ст., влажность: {3}%\nВетер: {4}, {5} м/с, {6}". \
                                format(ss, round(response["main"]["temp"]),
                                       round(response['main']['pressure'] / 1.33), response['main'] \
                                           ['humidity'], sspeed, response['wind']['speed'], derictionC,
                                       response['main']['feels_like'])
                            vk.messages.send(

                                user_id=event.user_id,
                                random_id=get_random_id(),
                                attachment=attachemens[0],
                                message="УТро:\n" + s)
                        if "15:00:00" in respons["list"][i]["dt_txt"]:
                            response = respons["list"][i]
                            upload = VkUpload(vk_session)
                            attachemens = []
                            image = requests.get(
                                "http://openweathermap.org/img/wn/{}@2x.png".format(response['weather'][0]['icon']),
                                stream=True)
                            photo = upload.photo_messages(photos=image.raw)[0]
                            attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
                            derictionC = deriction_def(response['wind']['deg'])

                            traslator = Translator(from_lang='en', to_lang="ru")

                            sspeed = sspeed_def(response['wind']['speed'])

                            ss = translate(response['weather'][0]['description'])
                            s = "{0} , температура: {1} °С\nОщущается: {7}\nДавление: {2} мм рт. ст., влажность: {3}%\nВетер: {4}, {5} м/с, {6}". \
                                format(ss, round(response["main"]["temp"]),
                                       round(response['main']['pressure'] / 1.33), response['main'] \
                                           ['humidity'], sspeed, response['wind']['speed'], derictionC,
                                       response['main']['feels_like'])
                            vk.messages.send(

                                user_id=event.user_id,
                                random_id=get_random_id(),
                                attachment=attachemens[0],
                                message="день:\n" + s)
                        if "21:00:00" in respons["list"][i]["dt_txt"]:
                            response = respons["list"][i]
                            upload = VkUpload(vk_session)
                            attachemens = []
                            image = requests.get(
                                "http://openweathermap.org/img/wn/{}@2x.png".format(response['weather'][0]['icon']),
                                stream=True)
                            photo = upload.photo_messages(photos=image.raw)[0]
                            print(photo)
                            attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
                            derictionC = deriction_def(response['wind']['deg'])

                            traslator = Translator(from_lang='en', to_lang="ru")

                            sspeed = sspeed_def(response['wind']['speed'])

                            ss = translate(response['weather'][0]['description'])
                            s = "{0} , температура: {1} °С\nОщущается: {7}\nДавление: {2} мм рт. ст., влажность: {3}%\nВетер: {4}, {5} м/с, {6}". \
                                format(ss, round(response["main"]["temp"]),
                                       round(response['main']['pressure'] / 1.33), response['main'] \
                                           ['humidity'], sspeed, response['wind']['speed'], derictionC,
                                       response['main']['feels_like'])
                            vk.messages.send(

                                user_id=event.user_id,
                                random_id=get_random_id(),
                                attachment=attachemens[0],
                                message="Вечер:\n" + s)

            elif event.text.lower()=="на завтра":
                for i in range(len(respons["list"])):
                    if str(datetime.date.today()+datetime.timedelta(days=1)) in respons["list"][i]["dt_txt"]:

                        if "03:00:00" in respons["list"][i]["dt_txt"]:
                            response = respons["list"][i]
                            upload = VkUpload(vk_session)
                            attachemens = []
                            image = requests.get(
                                "http://openweathermap.org/img/wn/{}@2x.png".format(response['weather'][0]['icon']),
                                stream=True)
                            photo = upload.photo_messages(photos=image.raw)[0]
                            attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
                            derictionC = deriction_def(response['wind']['deg'])
                            print(photo)
                            traslator = Translator(from_lang='en', to_lang="ru")

                            sspeed = sspeed_def(response['wind']['speed'])

                            ss = translate(response['weather'][0]['description'])
                            s = "{0} , температура: {1} °С\nОщущается: {7}\nДавление: {2} мм рт. ст., влажность: {3}%\nВетер: {4}, {5} м/с, {6}". \
                                format(ss, round(response["main"]["temp"]),
                                       round(response['main']['pressure'] / 1.33), response['main'] \
                                           ['humidity'], sspeed, response['wind']['speed'], derictionC,
                                       response['main']['feels_like'])
                            vk.messages.send(

                                user_id=event.user_id,
                                random_id=get_random_id(),
                                attachment=attachemens[0],
                                message="Ночь :\n" + s)

                        if "09:00:00" in respons["list"][i]["dt_txt"]:
                            response = respons["list"][i]
                            upload = VkUpload(vk_session)
                            attachemens = []
                            image = requests.get(
                                "http://openweathermap.org/img/wn/{}@2x.png".format(response['weather'][0]['icon']),
                                stream=True)
                            photo = upload.photo_messages(photos=image.raw)[0]
                            attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
                            print(photo)
                            derictionC = deriction_def(response['wind']['deg'])

                            traslator = Translator(from_lang='en', to_lang="ru")

                            sspeed = sspeed_def(response['wind']['speed'])

                            ss = translate(response['weather'][0]['description'])
                            s = "{0} , температура: {1} °С\nОщущается: {7}\nДавление: {2} мм рт. ст., влажность: {3}%\nВетер: {4}, {5} м/с, {6}". \
                                format(ss, round(response["main"]["temp"]),
                                       round(response['main']['pressure'] / 1.33), response['main'] \
                                           ['humidity'], sspeed, response['wind']['speed'], derictionC,
                                       response['main']['feels_like'])
                            vk.messages.send(

                                user_id=event.user_id,
                                random_id=get_random_id(),
                                attachment=attachemens[0],
                                message="Утро:\n" + s)
                        if "15:00:00" in respons["list"][i]["dt_txt"]:
                            response = respons["list"][i]
                            upload = VkUpload(vk_session)
                            attachemens = []
                            image = requests.get(
                                "http://openweathermap.org/img/wn/{}@2x.png".format(response['weather'][0]['icon']),
                                stream=True)
                            photo = upload.photo_messages(photos=image.raw)[0]
                            attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
                            derictionC = deriction_def(response['wind']['deg'])

                            traslator = Translator(from_lang='en', to_lang="ru")

                            sspeed = sspeed_def(response['wind']['speed'])

                            ss = translate(response['weather'][0]['description'])
                            s = "{0} , температура: {1} °С\nОщущается: {7}\nДавление: {2} мм рт. ст., влажность: {3}%\nВетер: {4}, {5} м/с, {6}". \
                                format(ss, round(response["main"]["temp"]),
                                       round(response['main']['pressure'] / 1.33), response['main'] \
                                           ['humidity'], sspeed, response['wind']['speed'], derictionC,
                                       response['main']['feels_like'])
                            vk.messages.send(

                                user_id=event.user_id,
                                random_id=get_random_id(),
                                attachment=attachemens[0],
                                message="День:\n" + s)
                        if "21:00:00" in respons["list"][i]["dt_txt"]:
                            response = respons["list"][i]

                            derictionC = deriction_def(response['wind']['deg'])
                            upload = VkUpload(vk_session)
                            attachemens = []
                            image = requests.get(
                                "http://openweathermap.org/img/wn/{}@2x.png".format(response['weather'][0]['icon']),
                                stream=True)
                            print("http://openweathermap.org/img/wn/{}@2x.png".format(response['weather'][0]['icon']))
                            photo = upload.photo_messages(photos=image.raw)[0]
                            attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
                            traslator = Translator(from_lang='en', to_lang="ru")
                            print(attachemens)
                            sspeed = sspeed_def(response['wind']['speed'])

                            ss = translate(response['weather'][0]['description'])
                            s = "{0} , температура: {1} °С\nОщущается: {7}\nДавление: {2} мм рт. ст., влажность: {3}%\nВетер: {4}, {5} м/с, {6}". \
                                format(ss, round(response["main"]["temp"]),
                                       round(response['main']['pressure'] / 1.33), response['main'] \
                                           ['humidity'], sspeed, response['wind']['speed'], derictionC,
                                       response['main']['feels_like'])
                            vk.messages.send(

                                user_id=event.user_id,
                                random_id=get_random_id(),
                                attachment=attachemens[0],
                                message="Вечер :\n" + s)

            elif event.text.lower()=="на 5 дней":
                tempnight=[]
                tempday=[]
                iconday=[]
                for i in range(len(respons["list"])):

                    if "03:00:00" in respons["list"][i]["dt_txt"] and str(datetime.date.today()) not in respons["list"][i]["dt_txt"]:
                        tempnight.append(str(round(respons["list"][i]["main"]["temp"]))+"°С")
                    if "15:00:00" in respons["list"][i]["dt_txt"]  and str(datetime.date.today()) not in respons["list"][i]["dt_txt"]:
                        tempday.append(str(round(respons["list"][i]["main"]["temp"]))+"°С")
                        iconday.append(respons["list"][i]["weather"][0]["icon"])
                images=[]
                i1=0
                for i in iconday:
                    i1+=1
                    image=requests.get("http://openweathermap.org/img/wn/{}@2x.png".format(i),
                                stream=True)
                    with open("file{}.png".format(i1),"wb") as f:
                        f.write(image.content)
                img=Image.new("RGBA",size=(500, 100))
                img1=Image.open("file1.png")
                img2=Image.open("file2.png")
                img3=Image.open("file3.png")
                img4=Image.open("file4.png")
                img5=Image.open("file5.png")
                img.paste(img1,(0, 0))
                img.paste(img2,(100, 0))
                img.paste(img3,(200,0))
                img.paste(img4, (300, 0))
                img.paste(img5, (400, 0))
                img=img.save("img.png")
                s="Погода в Москве с {} по {}".format(str((datetime.date.today()+datetime.timedelta(days=1)).strftime('%d/%m/%Y'))\
                    ,str((datetime.date.today()+datetime.timedelta(days=6)).strftime('%d/%m/%Y')))+\
                "\nДень /"+"//".join(tempday)+"/\n"+"Ночь /"+"//".join(tempnight)+"/"
                upload=VkUpload(vk_session)
                photo=upload.photo_messages(photos="img.png")[0]
                attachemens=[]
                attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),
                    attachment=attachemens[0],
                    message=s)

            else:
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message="Неизвестная команда")

            num[event.user_id]=0
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text.lower()=="корона" and num[event.user_id]==0:
            response = requests.get("https://coronavirusstat.ru/country/russia/")
            soup = BeautifulSoup(response.text, "html.parser")
            result = soup.findAll('table')[0].find("tbody").findAll("td")
            # for i in result:
            #     print(i)
            s = soup.findAll('body')[0].find("h6").find('strong').text + '\n'
            k = 0
            for i in result[0]:
                if k == 0:
                    s += "Активных: " + i.text
# ike.gabrielyan@yandex.ru
                elif k == 1:
                    s += "({} за сегодня)".format(i.text) + '\n'
                else:
                    break
                k += 1
            k = 0
            for i in result[1]:
                if k == 0:
                    s += "Вылечено: " + i.text

                elif k == 1:
                    s += "({} за сегодня)\n".format(i.text)
                else:
                    break
                k += 1
            k = 0
            for i in result[2]:
                if k == 0:
                    s += "Умерло: " + i.text
                elif k == 1:
                    s += "({} за сегодня)\n".format(i.text)
                else:
                    break
                k += 1
            k = 0
            for i in result[3]:
                if k == 0:
                    s += "Случаев: " + i.text

                elif k == 1:
                    s += "({} за сегодня)".format(i.text)
                else:
                    break
                k += 1
            result = soup.findAll('table')[0].find("tbody").findAll("td", {"class": "d-none d-sm-block"})
            print(result)
            #
            # result.findAll("span",{"class":"badge badge-danger"})
            infected = []
            k = 0
            for i in result:
                if k < 10:
                    if i.find("span", {"class": "badge badge-danger"}):
                        infected.append(int(i.find("span", {"class": "badge badge-danger"}).text))
                        k += 1
                else:
                    break

            result = soup.findAll('table')[0].find("tbody").findAll("span", {"class": "badge badge-success"})
            print(result)

            cured = []
            k = 0
            for i in result:
                if k < 20 and k % 2 == 1:
                    print(i.text)
                    cured.append(int(i.text))
                elif k > 20:
                    break
                k += 1
            result = soup.findAll('table')[0].find("tbody").findAll("th")
            data = []
            k = 0
            for i in result:
                if k < 10:
                    print(i.text)
                    data.append(i.text[:5])
                else:
                    break
                k += 1
            print(data)
            print(s)
            print(infected)
            print(cured)
            a = np.array([cured, infected])
            # df=DataFrame(a, columns=['Заболевшие',"Выздоровевшие"], index=data)
            barWidth = 0.25
            fig = plt.subplots()

            # Set position of bar on X axis
            br1 = np.arange(len(cured))
            br2 = [x + barWidth for x in br1]

            # Make the plot
            plt.bar(br1, cured, color='r', width=barWidth,
                    edgecolor='grey', label='Выздоровевшие')
            plt.bar(br2, infected, color='g', width=barWidth,
                    edgecolor='grey', label='Заболевшие')

            # Adding Xticks
            plt.xlabel('', fontweight='bold', fontsize=15)
            plt.ylabel('Кол-во', fontweight='bold', fontsize=15)
            plt.xticks([r + barWidth for r in range(len(cured))],
                       data)

            plt.legend()
            plt.savefig("grafic.png")


            upload = VkUpload(vk_session)
            photo = upload.photo_messages(photos="grafic.png")[0]
            attachemens = []
            attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
            vk.messages.send(

                user_id=event.user_id,
                random_id=get_random_id(),
                attachment=attachemens[0],
                message=s)
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text.lower()[:6] == "корона" and num[
            event.user_id] == 0:
            response = requests.get("https://coronavirusstat.ru/country/russia/")
            soup = BeautifulSoup(response.text, "html.parser")
            result = soup.findAll('div', {'class': "row border border-bottom-0 c_search_row"})
            city=event.text[7:].capitalize()
            print(result)
            a=''
            for i in range(len(result)):
                if city in result[i].find('a').text:
                    s = result[i].findAll("span", {"class": "dline"})

                    a+="Активных: "+s[0].text+"\n"
                    a+="Вылеченно: "+s[1].text+"\n"
                    a+="Умерло: "+s[2].text+"\n"
                    s = result[i].findAll("div", {"class": "h6 m-0"})
                    print(s)
                    a+="Заразилось: "+s[0].text
                    break
            if a=="":
                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message="Город не найден")
            else:

                vk.messages.send(

                    user_id=event.user_id,
                    random_id=get_random_id(),

                    message=a[:len(a)-3])

        elif event.type == VkEventType.MESSAGE_NEW and event.to_me:
            num[event.user_id]=0
            vk.messages.send(

                user_id=event.user_id,
                random_id=get_random_id(),

                message="Неизвестная команда")


main()
