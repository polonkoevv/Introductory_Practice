# Создать список (каталог мобильных приложений), состоящий из словарей (приложение). Словари должны содержать как минимум 5 полей
# (например, номер, название, рейтинг...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# apps = [{"id" : 123456, "title" : "Google Play", "rating" : 4.9,...} , {...}, {...}, ...]
# Реализовать функции:
# – вывода информации о всех приложениях;
# – вывода информации о приложении по введенному с клавиатуры номеру;
# – вывода количества приложений, с оценкой выше введённого;
# – обновлении всей информации о приложении по введенному номеру;
# – удалении приложения по номеру.
# Провести тестирование функций.

apps = [
{"id" : 156433, "author" : "Rovio","name": "Angry Birds", "rating": 5, "price": 0},

{"id" : 254738, "author" : "Apple","name": "Apple Music", "rating": 6.5, "price": 100},

{"id" : 193567, "author" : "Desmos","name": "Calculator" , "rating": 10, "price": 179},

{"id" : 294926, "author" : "Tinkoff","name": "Tinkoff", "rating": 9.6, "price": 349},

{"id" : 254296, "author" : "Facebook","name": "WhatsApp", "rating": 8 , "price": 0 },

{"id" : 907394, "author" : "Yandex","name": "Maps", "rating": 7.5, "price": 15},

{"id" : 154926, "author" : "Yandex","name": "Music", "rating": 6.3, "price": 0},

{"id" : 265836, "author" : "Google","name": "Chrome", "rating": 4.2, "price": 167},

{"id" : 272946, "author" : "MailGroup","name": "Mail", "rating": 3, "price": 200},

{"id" : 295737, "author" : "Lichess.org","name": "Lichess", "rating": 10, "price": 199}]


def infoOutput(apps):
    for perDict in apps:
        for key in perDict:
            print(key,":",perDict[key],";", end = " ")
        print()

def infoOutput_byNum(apps):
    
    for i in range(len(apps)):
    	print(i+1,"\t",(apps[i]["id"]),'\t',apps[i]["name"])

    appNum = int(input("Введите id приложения, информацию о котором нужно вывести.\n"))

    for i in range(len(apps)):
        if apps[i]["id"] == appNum:
            for key in apps[i]: print(key + " -- " + str(apps[i][key]))
            return 0
    print("Нет приложения с подхдящим номером")

def quantByRate(apps):
    quant = 0
    minRate = int(input("Введите минимальный рейтинг"))
    for perDict in apps:
        if perDict["rating"] > minRate:
            quant+=1
    print(quant)

def changeInfo(apps):
    for i in range(len(apps)):
        print(i+1,"\t",(apps[i]["id"]),'\t',apps[i]["name"])

    appNum = int(input("Введите id приложения, информацию о котором нужно поменять.\n")) 

    for i in range(len(apps)): 
        if apps[i]["id"] == appNum: 
            for key in apps[i]:
                print("Старый",key,"--",apps[i][key])
                apps[i][key] = input("Введите новое значение для " + str(key) + "\t")
            print(apps[i])
            return 0
    print("Нет приложения с таким id")

def delByNum(apps):
    
    for i in range(len(apps)):
        print(i+1,"\t",apps[i]["id"],"\t",apps[i]["name"])

    appNum = int(input("Введите id приложения, которое нужно удалить "))
    for i in range(len(apps)): 
        if apps[i]["id"] == appNum: 
            print("Удаление программы", apps[i]["name"])
            apps.pop(i)
            for i in range(len(apps)):
                print(i+1,"\t",(apps[i]["name"]))
            return 0
    print("Нет приложения с таким id")

    

def numChoice():
    num = int(input("\nВведите номер функции: "))
    if   num == 0:    return 0
    elif num == 1:    infoOutput(apps)
    elif num == 2:    infoOutput_byNum(apps)
    elif num == 3:    quantByRate(apps)
    elif num == 4:    changeInfo(apps)
    elif num == 5:    delByNum(apps)
    else:             print("Неверное значение номера. Попробуйте еще раз \n\n")
    numChoice()

print(" 0.Завершение работы программы \n 1. Вывод информации о всех приложениях \n 2. Вывод информации о приложении по введенному с клавиатуры номеру \n 3. Вывод количества приложений, с оценкой выше введённого \n 4. Обновление всей информации о приложении по введенному номеру \n 5. Удаление приложения по номеру\n")

numChoice()


