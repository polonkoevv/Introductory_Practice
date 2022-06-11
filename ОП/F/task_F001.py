import datetime
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
from distutils.command.upload import upload
from email import message
from requests import session
from translate import Translator
import PIL.Image as Image
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.figure import Figure
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from corona import *
import scheduleTask as sch
from scheduleTask import get_schedule_xlsx,check_week_number,week_schedule_print,get_today_schedule,get_day_shedule
import json
import re


def send_message(id =346598810, message = ''):
    vk.messages.send(
                user_id = id,
                random_id = get_random_id(),
                message = message
            )


def upload_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key


def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=peer_id,
        attachment=attachment
    )

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
def deriction_def(x):

    deriction = ['северный', 'северо-восточный', "восточный", "юго-восточный", "южный", "юго-западный",
                 "западный", 'cеверо-западный']
    if x> (360 - 22.5):
        derictionC = deriction[0]
    else:
        derictionC = deriction[math.ceil((x + 22.5) / 45) - 1]
    return derictionC

vk_session = vk_api.VkApi(token='0a4fe5d3a71e49be0237d1ad5eb9ee7ae555306ed317a6b381327c50ebc854142fe2b82121f649dfe79a3')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
upload = VkUpload(vk)
group_choice = 1
group = 'ИКБО-08-21'

for event in longpoll.listen():

    if event.type==VkEventType.MESSAGE_NEW and event.to_me and (event.text.lower()=="привет" or event.text.lower()=="начать"):
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
Корона Инг для короны в ингушетии Корона для короны в мск'

            )
    elif event.type == VkEventType.MESSAGE_NEW and event.text.lower().strip() == "корона":
        send_message(event.user_id, corona_russia())
        send_photo(vk, event.user_id, *upload_photo(upload, 'C:/Users/polon/Desktop/pract/graph.png'))
    elif event.type == VkEventType.MESSAGE_NEW and event.text.lower().strip()[:6] == "корона" and len(event.text.lower().strip())>7:
        reg = event.text.lower().strip()[7:]
        print(reg)
        send_message(event.user_id, corona_reg(reg))

    elif event.type == VkEventType.MESSAGE_NEW and re.match(r"[а-яА-Я]{4}-(\d){2}-(\d){2}",event.text.upper().strip()):
        s = sch.check_group(event.text.upper().strip())
        if s:
            group_choice = 1
            group = event.text.upper().strip()
            print("Groupe choosed")
            send_message(event.user_id, f"Отлично! Группа {event.text.upper().strip()} выбрана")
    elif event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text.lower()=="бот":
        if group_choice == 1:
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
        else:
            send_message(event.user_id, "Выбери группу")
    elif event.type==VkEventType.MESSAGE_NEW and event.to_me and(re.match(r"[а-яА-Я]{4}-(\d){2}-(\d){2}",event.text.upper().strip()) or re.match(r"БОТ [а-яА-Я]{4}-(\d){2}-(\d){2}",event.text.upper().strip())):
        group = event.text.split()[-1].upper()
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
                message=f"Показать расписание {group}")
    elif event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text.lower()=="какая неделя?" and group_choice == 1:
        send_message(event.user_id, f'Идет {check_week_number()} неделя')
    elif event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text.lower()=="на эту неделю" and group_choice == 1:
        col = sch.check_group(group)
        a = week_schedule_print(group, check_week_number()%2,col)
        f = open("F/schedule.txt", 'r+', encoding='UTF8')
        s = f.readline()
        m = ''
        for s in f:
            m+=s
        send_message(event.user_id, m)
    elif event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text.lower()=="на следующую неделю" and group_choice == 1:
        col = sch.check_group(group)
        if check_week_number()%2 == 1: num = 2
        else: num = 1
        a = week_schedule_print(group,num ,col)
        f = open("F/schedule.txt", 'r+', encoding='UTF8')
        s = f.readline()
        m = ''
        for s in f:
            m+=s
        send_message(event.user_id, m)
    elif event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text.lower()=="на сегодня" and group_choice == 1:
        send_message(event.user_id, get_today_schedule(group,check_week_number()%2,sch.check_group(group),0))
    elif event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text.lower()=="на завтра" and group_choice == 1:
        send_message(event.user_id, get_today_schedule(group,check_week_number()%2,sch.check_group(group),1))
    elif event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text.lower()=="какая группа?" and group_choice == 1:
        send_message(event.user_id, f"Показываю расписание группы {group}")
    elif event.type==VkEventType.MESSAGE_NEW and event.to_me and re.match(r"БОТ [а-яА-Я]+ [а-яА-Я]{4}-(\d){2}-(\d){2}",event.text.upper().strip()):
        curr_group = event.text.split()[2].upper()
        week_day = event.text.split()[1].lower()
        send_message(event.user_id, get_day_shedule(curr_group,sch.check_group(curr_group),week_day))


    elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text.lower() == "погода":
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Погода сейчас', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Погода сегодня', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Погода на завтра', VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        keyboard.add_button('Погода на 5 дней', VkKeyboardColor.PRIMARY)
        vk.messages.send(

            user_id=event.user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard(),
            message="Показать погоду в Москве")

    elif event.type == VkEventType.MESSAGE_NEW and event.to_me:
        respons = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=moscow&appid=93e83956c91b2e00ebbabe0672230693&units=metric")
        respons = respons.json()
        responses = requests.get("http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=93e83956c91b2e00ebbabe0672230693&units=metric")
        responses = responses.json()
        print(event.text.lower())
        vk.messages.send(

            user_id=event.user_id,
            random_id=get_random_id(),

            message="Ожидайте...")
        if event.text.lower()=="погода сейчас":

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
        elif event.text.lower()=="погода сегодня":
            print(13)
            for i in range(len(respons["list"])):
                if str(date.today()) in respons["list"][i]["dt_txt"]:

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

        elif event.text.lower()=="погода на завтра":
            for i in range(len(respons["list"])):
                if str(date.today()+timedelta(days=1)) in respons["list"][i]["dt_txt"]:

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
                                        ['humidity'], sspeed, response['wind']['speed'], derictionC,response['main']['feels_like'])
                        vk.messages.send(
                            user_id=event.user_id,
                            random_id=get_random_id(),
                            attachment=attachemens[0],
                            message="Вечер :\n" + s)

        elif  event.text.lower()=="погода на 5 дней":
            tempnight=[]
            tempday=[]
            iconday=[]
            for i in range(len(respons["list"])):

                if "03:00:00" in respons["list"][i]["dt_txt"] and str(date.today()) not in respons["list"][i]["dt_txt"]:
                    tempnight.append(str(round(respons["list"][i]["main"]["temp"]))+"°С")
                if "15:00:00" in respons["list"][i]["dt_txt"]  and str(date.today()) not in respons["list"][i]["dt_txt"]:
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
            img1=Image.open("C:/Users/polon/Desktop/pract/file1.png")
            img2=Image.open("C:/Users/polon/Desktop/pract/file2.png")
            img3=Image.open("C:/Users/polon/Desktop/pract/file3.png")
            img4=Image.open("C:/Users/polon/Desktop/pract/file4.png")
            img5=Image.open("C:/Users/polon/Desktop/pract/file5.png")
            img.paste(img1,(0, 0))
            img.paste(img2,(100, 0))
            img.paste(img3,(200,0))
            img.paste(img4, (300, 0))
            img.paste(img5, (400, 0))
            img=img.save("img.png")
            s="Погода в Москве с {} по {}".format(str((date.today()+timedelta(days=1)).strftime('%d/%m/%Y'))\
                ,str((date.today()+timedelta(days=6)).strftime('%d/%m/%Y')))+\
            "\nДень /"+"//".join(tempday)+"/\n"+"Ночь /"+"//".join(tempnight)+"/"
            upload=VkUpload(vk_session)
            photo=upload.photo_messages(photos="C:/Users/polon/Desktop/pract/img.png")[0]
            attachemens=[]
            attachemens.append("photo{}_{}".format(photo["owner_id"], photo['id']))
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                attachment=attachemens[0],
                message=s)
