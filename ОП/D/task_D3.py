import re
f = open('C:\\Users\\polon\\Desktop\\pract\D\\email_adresses.txt')
regArr = []
for s in f:
    a = list(re.split(r'([a-z0-9_\.-]+)@([a-z0-9_\.-]+)\.([a-z\.]{2,6})',s))
    a.remove('')
    if a.count('\n') > 0: a.remove('\n')
    print(a)
    regArr.append(a)
