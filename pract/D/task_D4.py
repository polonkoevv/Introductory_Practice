from base64 import encode
from os import *
from time import *
from re import *

chdir('C:\\Users\\polon\\Desktop\\pract\\D')
path = getcwd()
def moveTasks(path):
    makedirs(path + '\\Ознакомительная практика\\Тема A', True)
    makedirs(path + '\\Ознакомительная практика\\Тема B', True)
    for item in scandir(path + '\\allTasksD'):
        if search(r'task_([A-B]{1})(\d)+\.py',item.name) != None and item.is_file:
            replace(path + f'\\allTasksD\\{item.name}', path + f'\\Ознакомительная практика\\Тема {item.name[5]}\\{item.name}')

def startTasks(path):
    files = walk(f'{path}\\Ознакомительная практика')
    for i in files:
        if len(i[2]) != 0:
            tasks = i[2]

            if tasks[0][5] == 'A':
                print("Тема A")
                path1 = 'C:/Users/polon/Desktop/pract/D/Ознакомительная практика/Тема A'
            else:
                print("Тема B")
                path1 = 'C:/Users/polon/Desktop/pract/D/Ознакомительная практика/Тема B'   
            for task in tasks:
                path1 = f'{i[0]}\\{task}'
                print(path1)
                with open(path1, 'r') as f:
                    f = f.read()

                # for s in f:
                #   if f[0:3] == 'def':
                #     print(s)
                print('\t','script ', task)
                # funcs = []
                # start = time.time()
                # f = open(files[0]+task).read()
                # exec(f)
                # print()
        

#moveTasks(path)
#startTasks(path)

path1 = "C:\\Users\\polon\\Desktop\\pract\\D\\Ознакомительная практика\\Тема B\\task_A393.py"
with open(path1, 'r') as f:
    f = f.read()
print(f)

