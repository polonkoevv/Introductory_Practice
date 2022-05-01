# Написать функцию break_camel_case, которая разбивает слова написанные CamelCase,
# используя в качестве разделителя пробел
#
# Примеры:
# break_camel_case("BreakCamelCase") ==> "Break Camel Case"

#ГОТОВО

import traceback


def break_camel_case(s):
    s1 = s[0]
    for i in range(1,len(s)):
            if s[i].istitle() and s[i-1] != " ":
                s1 += " " + s[i]
            else:
                s1 += s[i]
    return s1


# Тесты
try:
    assert break_camel_case("BreakCamelCase") == "Break Camel Case"
    assert break_camel_case("helloWorld") ==  "hello World"
    assert break_camel_case("helloWorld BreakCamelCase") == "hello World Break Camel Case"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
