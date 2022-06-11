from cProfile import label
import openpyxl
import requests
from datetime import *
from bs4 import BeautifulSoup
import locale
import re
import numpy as np
import matplotlib.pyplot as plt

def corona_reg(region_row):
    link =  BeautifulSoup((requests.get('https://coronavirusstat.ru//')).text, "html.parser").find_all("span", class_='small')
    for i in link:
        if region_row.lower() in i.text.lower():
            region_corr = i.text
            reg_link = i.find_parent().find_parent().find_parent()

    ill_block = reg_link.find('div', class_='p-1 col-7 row m-0')


    all = ill_block.find_all('div', class_='p-1 col-4 col-sm-2')
    good = ill_block.find_all('div', class_='p-1 col-4 col-sm-3')
    dead = ill_block.find_all('div', class_='p-1 col-3 col-sm-2 d-none d-sm-block')
    abs = []
    for i in all:
        abs.append(i.text.replace('\n',' ').replace('\t',' ').split())
    for j in good:
        abs.append(j.text.replace('\n',' ').replace('\t',' ').split())
    for k in dead:
        abs.append(k.text.replace('\n',' ').replace('\t',' ').split())
    mes = f"Регион: {region_corr}\n"
    for per in abs:
        s = f"{per[0]}: {per[1]} "
        if len(per) > 2:
            s+=f"Сегодня({per[2]})"
        mes+=s+'\n'
    return mes

def corona_russia():
    link =  BeautifulSoup((requests.get('https://coronavirusstat.ru/country/russia/')).text, "html.parser").find("tbody").find_all("tr")
    a = []
    x_list=[]
    cured = []
    active = []
    dead = []
    for i in link:
        a.append(i.text.split())
    #print(a[0])
    k = a[0]
    s = 'По состоянию на ' + k[0] + '\n'
    s += 'Случаев: ' + k[-3] + ' ('+ k[-2] +  ' за сегодня)\n'
    s += 'Активных: ' + k[1] + ' ('+ k[2]+ ' за сегодня)\n'
    s += 'Вылечено: ' + k[4] + ' (' + k[5] + ' за сегодня)\n'
    s += 'Умерло: ' + k[7] + '('+k[8] + ' за сегодня)'
    a = a[1:11]
    for i in a:
        active.append(int(i[1]))
        cured.append(int(i[4]))
        dead.append(int(i[7]))
        x_list.append(i[0][:-5])
    barWidth = 1
    plt.title("Корона в России")
    plt.bar(x_list,cured, color='blue', width=barWidth,label='Выздоровевшие')
    plt.bar(x_list,dead, color='red', width=barWidth,label='Умершие')
    plt.bar(x_list,active, color='green', width=barWidth,label='Заболевшие')
    y_list = []
    for i in range(0,max(cured)+2500000,2500000):y_list.append(i)
    #print(y_list)
    plt.xlabel('', fontsize=15)
    plt.ylabel('Кол-во', fontweight='bold', fontsize=15)
    plt.yticks(y_list)
    plt.legend()
    plt.savefig("graph.png")
    return s
    