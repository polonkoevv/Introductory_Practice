# Написать функцию palindrome, которая для заданного числа num возвращает список всех числовых палиндромов,
# содержащихся в каждом номере. Массив должен быть отсортирован в порядке возрастания,
# а любые дубликаты должны быть удалены.
#
# Пример:
# palindrome(34322122)  =>  [22, 212, 343, 22122]


import traceback


def palindrome(a):
    a = str(a)
    pall = list()
    for i in range(len(a)-1):
        for n in range(len(a)):
            number = a[i:n+1]
            nlen = len(number)
            if nlen % 2 == 0 and nlen > 1 and int(number)!= 0 and (number[:int(nlen/2)] == number[int(nlen/2):][::-1]):
                pall.append(int(number))        
            elif nlen > 1 and int(number)!=0 and (number[:int(nlen/2)] == number[int(nlen/2)+1:][::-1]):
                pall.append(int(number))
    return sorted(set(pall))


# Тесты
try:
    assert palindrome(1551) == [55, 1551]
    assert palindrome(221122) == [11, 22, 2112, 221122]
    assert palindrome(10015885) == [88, 1001, 5885]
    assert palindrome(13598) == []
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")



    