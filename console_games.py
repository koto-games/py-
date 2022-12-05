# запуск библиотек
import requests

# подготовка
F = '1.0'
QA = '>>>'

# создание функций
def parsing(w):
    re = str(requests.get(w).text)
    print('\n'+re+'\n')

def information(w):
    return str(requests.get(w).text)
    
# запуск программы
while True:
    try:
        www = input(QA)
        ii = www.split(' ')

        if www == 'h':
            # новости
            parsing('https://koto-games.github.io/py-/h.txt')
        elif ii[0] == 'la':
            # запуск
            print('https://koto-games.github.io/py-/ds/'+ii[1]+'.py')
            print(information('https://koto-games.github.io/py-/ds/'+ii[1]+'.py'))

    except:
        print(QA+'ошибка')