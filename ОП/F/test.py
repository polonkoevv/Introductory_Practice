from datetime import datetime as dt


a = open("F/schedule.txt", 'r+', encoding='UTF8')
s = a.readline()

f = dt.today().weekday()
print(f)