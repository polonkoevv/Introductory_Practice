# Написать функцию sum_of_fractions, которая получает вещественное число и возвращает строку - сумму слагаемых числа в виде дробей. 
# Между слагаемыми поставить символ +, все отделить пробелами 
#
# Примеры:
# sum_of_fractions(1.24) ==> '1 + 2/10 + 4/100'

import traceback


def sum_of_fractions(num):
    a=""
    ss=""

    num=str(num)
    for i in range(0,len(num)):
        if num[i]==".":
            c=i
            if num[:c]!="0":
                a=a+num[:c]+" + "
            for i1 in range(c+1,len(num)):
                if num[i1]=="0":
                    continue
                b=10**(i1-c)
                if (len(num)-1)!=i1:
                    ss=num[i1]+"/"+str(b)+" + "
                else:
                    ss = num[i1] + "/" + str(b)
                a=a+ss
            break
    return a



# Тесты
try:
    assert sum_of_fractions(1.24) == '1 + 2/10 + 4/100'
    assert sum_of_fractions(7.304) == '7 + 3/10 + 4/1000'
    assert sum_of_fractions(0.04) == '4/100'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")