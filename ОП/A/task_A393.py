# Написать функцию strong_enough(earthquake, age), которая вычисляет достаточно ли безопасное здание,
# чтобы выдержать землетрясение.  Здание рухнет, если сила землетрясения будет больше, чем сила здания.
# Earthquake – список, состоящий из спсика ударных волн.
# Вычисление силы землетрясения для [[5,3,7], [3,3,1], [4,1,2]]
# -> ((5 + 3 + 7) * (3 + 3 + 1) * (4+ 1 + 2)) = 735.
# Прочность нового здания 1000, при этом это значение уменьшается на 1% каждый год


import traceback


def strong_enough(earthquake, age):
    # Тело функции
    s = sum(earthquake[0]) * sum(earthquake[1]) * sum(earthquake[2])
    a = True
    n = 1000
    for i in range(age):
        n *= 0.99
        if s >= n:
            a = False
            break
        
    return a

#ГОТОВО

# Тесты
try:
    assert strong_enough([[2,3,1],[3,1,1],[1,1,2]], 2) == True
    assert strong_enough([[5,8,7],[3,3,1],[4,1,2]], 2) == True
    assert strong_enough([[5,8,7],[3,3,1],[4,1,2]], 3) == False
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")


