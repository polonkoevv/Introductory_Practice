# Написать функцию strong_number(number), которая определяет является ли число сильным.
# Число сильное, если сумма факториалов цифр числа равна самому числу.
#
# Примеры:
# strong_number(145) => True -> 1! + 4! + 5! = 1 + 24 + 120 = 145

import traceback


#ГОТОВО
def strong_number(number):
    def fact(n):
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return(factorial)
    # Тело функции
    number = str(number)
    s = 0
    for i in number:
        s += fact(int(i))
    if s == int(number):
        return True
    return False


# Тесты
try:
    assert strong_number(1) == True
    assert strong_number(2) == True
    assert strong_number(7) == False
    assert strong_number(93) == False
    assert strong_number(145) ==  True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")