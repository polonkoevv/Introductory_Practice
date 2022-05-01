"""Создать класс Library. Поля: название библиотеки, адрес, список читателей (список экземпляров класса Reader),
    список библиотекарей (список экземпляров класса Librarian). Определить конструктор. 
    1)Переопределить метод преобразования в строку для печати всей информации 
        о библиотеке (с использованием переопределения в классах Reader и Librarian). 
    2)Переопределить методы получения количества читателей функцией len, получения читателя по индексу, 
        изменения по индексу, удаления по индексу (пусть номера читателей считаются с 1,а индекс 0 – список всех библиотекарей). 
    3)Переопределить операции + и - для добавления или удаления читателя.
    4)Добавить функцию создания txt-файла и записи всей информации в него (в том числе читательского билета
        читателей и рабочих часов библиотекарей)."""


from Librarian import Librarian
from Reader import Reader

class Library:
    def __init__(self, name = "Boston", adress = "25 avenue", readers_list = [Reader(),Reader()], librarians_list = [Librarian(), Librarian()]):
        self.name = name
        self.adress = adress
        self.readers_list = readers_list
        self.librarians_list = librarians_list
    
    def __str__(self):
        a = f"Название библиотеки: {self.name}\nАдрес библиотеки: {self.adress} \n\n\nЧитатели"
        for per_read in self.readers_list:
             a += f"{str(per_read)}\n\n"
        a += f"\n\nБиблиотекари:\n"
        for per_lib in self.librarians_list:
            a += f"{str(per_lib)}\n\n"
        return self

    def __getitem__(self, key):
        if key == 0:
            for per_lib in range(len(self.librarians_list)):
                print(per_lib+1, str(per_lib))
        else:
            print(str(self.readers_list[key-1]))
        return self

    def __delitem__(self,key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")
        if key == 0:
            self.librarians_list.clear()
        else:
            self.readers_list.pop(key-1)
        return self
    
    def __setitem__(self,key,value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        if key == 0:
            self.librarians_list = value
        else:
            self.readers_list[key-1].first_name = value[0]
            self.readers_list[key-1].last_name = value[1]
            self.readers_list[key-1].age = value[2]
            self.readers_list[key-1].ticket_num = value[3]
            self.readers_list[key-1].ticket = value[4]
        return self

    def __add__(self,other):
        if not isinstance(other,Reader):
            raise ArithmeticError("Правый операнд должен быть класса Reader")
        self.readers_list.append(other)
        return self
        
    def __sub__(self,other):
        if not isinstance(other,Reader):
            raise ArithmeticError("Правый операнд должен быть класса Reader")
        a = self.readers_list.index(other)
        self.readers_list.pop(a)
        return self
        
    def info_to_txt(self):
        file = open('C\\LibraryTXT.txt', 'w', encoding = 'UTF-8')

        file.write("Название библиотеки: "  + self.name + "\nАдрес библиотеки: " + self.adress + "\n\n\nЧитатели:\n\n")

        for per_read in self.readers_list:
            file.write(per_read.show_info())
            file.write("Читательский билет: ")
            for tick in per_read.ticket:
                file.write("№" + tick + ': ' + per_read.ticket[tick] + '; ')
            file.write('\n\n')

        file.write("\n\nБиблиотекари:\n\n")

        for per_lib in self.librarians_list:
            file.write(per_lib.show_info())
            file.write("График работы: ")
            for sch in per_lib.schedule:
                file.write(sch + ': ' + per_lib.schedule[sch]+'; ')
            file.write('\n\n')

