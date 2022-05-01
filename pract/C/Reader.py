"""Создать производный от Person класс Reader. Новые поля: номер читательского билета, читательский билет
    (словарь вида номер книжки: дата взятия книжки из библиотеки). Определить конструктор, с вызовом родительского
    конструктора. Определить функции добавления новой книги в читательский билет, получения даты по номеру книги,
    форматированной печати всего читательского билета. Переопределить метод преобразования в строку для печати
    основной информации (ФИ, возраст, номер читательского билета)."""

from Person import Person

class Reader(Person):

    def __init__(self, first_name = "Арсений", last_name = "Гаврилов", age = 45, ticket_num = 173, ticket = {'12': '12.12.12', '123123': '13.13.13', \
        '213434': '21.21.21', '213423': '34.34.34', '131231': '54.54.54'}):
        super().__init__(first_name, last_name, age)
        self.ticket_num = ticket_num
        self.ticket = ticket
    
    def add_book(self,book_num,date):
        
        self.ticket.update({book_num:date})
        return self

    def get_date_by_num(self, book_num):
        return(f"Дата получения книги № {book_num}: {self.ticket.get(str(book_num))}")
    
    def show_ticket(self):
        print("Номер книги: \t\t Дата получения:")
        items = self.ticket.items()
        for per_item in items:
            print(per_item[0],'\t\t\t', per_item[1])
    
    def __str__(self):
        a = f"ФИ {self.last_name} {self.first_name};\nВозраст: {self.age};\nНомер читательского билета: {self.ticket_num};\n"
        return(a)
            
a = Reader()

print(a.get_date_by_num(12))