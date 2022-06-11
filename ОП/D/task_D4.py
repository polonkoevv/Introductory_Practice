from os import walk, makedirs, chdir, getcwd,scandir,replace, system, startfile
from time import *
import subprocess
import sys
from re import *
from time import *

chdir('C:\\Users\\polon\\Desktop\\pract\\D')
path = getcwd()
def moveTasks(path):
    makedirs(path + '\\Ознакомительная практика\\Тема A', True)
    makedirs(path + '\\Ознакомительная практика\\Тема B', True)
    for item in scandir(path + '\\allTasksD'):
        if search(r'task_([A-B]{1})(\d)+\.py',item.name) != None and item.is_file:
            replace(path + f'\\allTasksD\\{item.name}', path + f'\\Ознакомительная практика\\Тема {item.name[5]}\\{item.name}')

def startTasks(path):
    pract = walk(f'{path}\\Ознакомительная практика')
    for mainfolder in pract:
        if len(mainfolder[-2]) == 2:
            for folder in mainfolder[-2]:
                print(f'folder {folder}')
                theme_fold = walk(f'{path}\\Ознакомительная практика\\{folder}')
                for i in theme_fold:
                    tasks = i[-1]
                    for task in tasks:
                        print(f'\n>>> script {task}')
                        f = open('C:\\Users\\polon\\Desktop\\pract\\D\\Ознакомительная практика\\'+folder+'\\'+task,'r')
                        s = f.readline
                        for s in f:
                            if s[:3] == 'def':
                                func = s[4:-2]
                                break
                        f.close()
                        print(f'>>> >>> function {func}')
                        start = time()
                        with open('C:\\Users\\polon\\Desktop\\pract\\D\\Ознакомительная практика\\'+folder+'\\'+task, 'r', encoding='UTF8') as m:
                            result = subprocess.run([sys.executable, "-c", m.read()], capture_output=True, encoding='ISO-8859-1')
                        print(f'>>> >>> output {result.stdout}', end='')
                        print(f'>>> >>> time: {time() - start}')
                        

print(path)
startTasks(path)