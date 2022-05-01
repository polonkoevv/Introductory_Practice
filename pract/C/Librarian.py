from Person import Person

'''Создать производный от Person класс Librarian. Новые поля: номер удостоверения, должность, график работы
    (словарь вида день недели: часы работы). Определить конструктор, с вызовом родительского конструктора.
    Определить функции изменения должности, добавления, удаления и изменения графика работы. Переопределить
    метод преобразования в строку для печати основной информации (ФИ, возраст, номер удостоверения, должность).'''

class Librarian(Person):

    def __init__(self, first_name = "Андрей", last_name = "Лавров", age = 27, ident_num = 123, post = "Директор",schedule = {"Пн" :"9-21","Вт":"", "Ср":"9-21", "Чт":"","Пт":"9-21", "Сб":"", "Вс":"9-19"}):
        super().__init__(first_name, last_name, age)
        self.ident_num = ident_num
        self.post = post
        self.schedule = schedule
    
    def change_post(self,new_post):
        self.post = new_post
        return self
    
    def set_schedule(self):

        a = list(map(str, input("Введите сокращения дней недели, расписание которых хотите поменять. Пн, Вт, Ср и т.д\n\n").title().split()))
 
        print("Введите часы работы в формате (час начала)-(час окончания) 9-21, для удаления оставьте поле пустым.\n\n")
        for i in a:
            self.schedule[i] = input(str(i)+": ")

        for i in self.schedule:
            print(i,self.schedule[i])

    def __str__(self):
        a = f"ФИ: {self.last_name} {self.first_name};\nВозраст: {self.age};\nНомер удостоверения: {self.ident_num};\nДолжность: {self.post};\n"
        return(a)

