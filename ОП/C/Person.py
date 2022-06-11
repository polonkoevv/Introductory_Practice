class Person:
    
    def __init__(self, first_name , last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def show_info(self):
        a = "ФИ: "+ self.last_name + ' ' + self.first_name + ";\nВозраст: " + str(self.age) + ";"
        print(a)
