# Написать функцию goldbach(n) для иллюстрации гипотезы Гольдбаха: каждое четное целое число больше 2 
# может быть записано как сумма двух простых чисел. 
# Если аргумент нечетный, верните пустой список.
# Для четных аргументов необходимо вернуть список с двумя простыми числами, сумма которых равна n. 
# Два простых числа должны быть самыми дальними (с наибольшей разницей). Первое простое число должно быть наименьшим.
#
# Пример:
# goldbach(5) ==> []
# goldbach(4) ==> [2, 2]
# goldbach(14) ==> [3, 11]

#ГОТОВО

import traceback

def IsSimple(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True
 


def goldbach(n):
    # Тело функции
    if n % 2 == 0:
        for k in range(2, n):
            if IsSimple(k) and IsSimple(n-k):
                return [k,n-k]
    return []


# Тесты
try:
    assert goldbach(15) == []
    assert goldbach(4) == [2, 2]
    assert goldbach(10) == [3, 7]
    assert goldbach(24) == [5, 19]
    assert goldbach(100) == [3, 97]    
    assert goldbach(1234) == [3, 1231]          
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

