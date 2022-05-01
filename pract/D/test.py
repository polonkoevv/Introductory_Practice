from os import *

from re import *

#makedirs('D\\Ознакомительная практика\\Тема A')
#makedirs('D\\Ознакомительная практика\\Тема B')

chdir('C:\\Users\\polon\\Desktop\\pract\\D')
path = getcwd()

# replace(path+'/tts/task_A150.py', \
#     path+'/Ознакомительная практика/task_A150.py')


def a():
    #makedirs(path+'\\Ознакомительная практика\\Тема A')
    #makedirs(path+'\\Ознакомительная практика\\Тема B')
    for item in scandir(path + '\\allTasksD'):
        if search(r'task_([A-B]{1})(\d)+\.py',item.name) != None and item.is_file:
            replace(path + f'\\allTasksD\\{item.name}', path + f'\\Ознакомительная практика\\Тема {item.name[5]}\\{item.name}')

b = walk('C:\\Users\\polon\\Desktop\\pract\\D', topdown = False)

for i in b:
    print(i)