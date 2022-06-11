# Написать функцию numEnum, на вход которой приходит список строк (числа). Необходимо объединить
# строки в одну таким образом, чтобы получаемое числовое значение было максимальным.
#
# Пример:
# numEnum(['1', '2', '3']) ==> '321'
# numEnum(['3', '30', '34', '5', '9']) ==> '9534330'



import traceback



def numEnum(numList, ):
    #Проверять каждое число на определенный индекс и собирать в массив 
    #макс число. Если их несколько то с этим же массивом запускать по новой
    
    # digList = []

    # for i in range(len(numList)):
    #     if len(numList[i]) < ind+1:
    #         digList.append(numList[i])
    #     digList.append(numList[i][ind])
    #     maxdig = max(digList)
    #     if len()
    #     for digCount in range(digList.count(maxdig)):

    maxLen = 0

    for i in range(len(numList)):
        maxLen = max(maxLen, len(numList[i]))
    print(maxLen)

    numCopy = []
    for i in range(len(numList)):
        numCopy.append(numList[i] + '0'*(maxLen-len(numList[i])))

    
    print(numCopy)

    finstr = ''

    while len(numCopy) != 0:
        print(numCopy.index(max(numCopy)))
        finstr += numList[numCopy.index(max(numCopy))]
        numList.pop(numCopy.index(max(numCopy)))
        numCopy.pop(numCopy.index(max(numCopy)))
    finstr = str(int(finstr))
    return(finstr)


# Тесты
try:
    assert numEnum(['0', '0', '0']) == '0'
    assert numEnum(['12', '121']) == '12121'
    assert numEnum(['12', '128']) == '12812'
    assert numEnum(['5051', '50']) == '505150'
    assert numEnum(['3', '30', '34', '5', '9']) == '9534330'
    assert numEnum(['824', '938', '1399', '5607', '6973', '5703', '9609', '4398', '8247']) \
           == '9609938824824769735703560743981399'
    assert numEnum(['3803', '38', '380']) == '383803803'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")