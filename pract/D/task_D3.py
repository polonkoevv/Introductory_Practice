import re

f = open('C:\\Users\\polon\\Desktop\\pract\D\\email_adresses.txt')

regArr = []

for s in f:
    regArr.append(re.split(r'(\.)*\.|@', s))
print(regArr)