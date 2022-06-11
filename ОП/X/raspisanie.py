import requests
from bs4 import BeautifulSoup
page=requests.get("https://www.mirea.ru/schedule/")
soup=BeautifulSoup(page.text,"html.parser")

result=soup.find("div",{"class":"rasspisanie"}).find(string="Институт информационных технологий")\
   .find_parent("div").find_parent("div").findAll("a")

for x in result:


    if "ИИТ_1" in x['href']:

        f=open("file.xlsx","wb")
        resp=requests.get(x['href'])
        f.write(resp.content)
    if "ИИТ_2" in x['href']:

        f=open("file2.xlsx","wb")
        resp=requests.get(x['href'])
        f.write(resp.content)
    if "ИИТ_3" in x['href']:

        f=open("file3.xlsx","wb")
        resp=requests.get(x['href'])
        f.write(resp.content)
