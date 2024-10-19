
from pprint import pprint
import requests
import pandas as pd
#1
'''
функция для получения информации о животных. необходимо ввести название животного и выбрать информацию

при нескольких совпадениях(например fox может означать gray fox или red fox) 
вариант будет выбран случайно

#также API находит животное при частичном совпадении, как если бы искал в 
поисковой строке и выдает случайное (be=Ambrosia Beetle), а ошибка только при полном отсутствии
совпадений(например afsdgfhjg) 
c этим я ничего не успела придумать:)
'''

def get_animal(name):

    #функции для выбора конкретных данных из всего набора
    def tax_info(data):
        mydict = data[0]['taxonomy']
        print('Taxonomyy:')
        pprint(mydict)

    def loc_info(data):
        mydict = data[0]['locations']
        print('Location:')
        for i in mydict:
            print(i)

    def char_info(data):
        mydict = data[0]['characteristics']
        print('Characteristics:')
        pprint(mydict)

    my_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    my_key='HObsNBTW7HBALEa36V1ZoA==QWIKXK2WXGTsOtLZ'

    response = requests.get(my_url, headers={'X-Api-Key': f'{my_key}'})
    if response.status_code == 200:
        data=response.json()

        #провека нашлось ли животное, так как этот API возвращает данные даже при неверном вводе
        try:
            print(data[0]['name'])
        except IndexError:
            print('animal not found')
            return 0

        try:
            #выбор информации для вывода
            choice=input(f'what information about {name} you want to get(you can input several numbers divided by space):\n'
                     '1-taxonomy\n'
                     '2-location\n'
                     '3-characteristics\n')
            #трансформация ввода в список чисел
            options=[int(i) for i in choice.split()]
            #обработка ввода не из указанного списка чисел
            if 1 not in options and 2 not in options and 3 not in options:
                raise ValueError

            if 1 in options:
                tax_info(data)
            if 2 in options:
                loc_info(data)
            if 3 in options:
                char_info(data)
        except ValueError:
            print('incorrect input, numbers should be 1,2 or 3!')
    else:
        print("Error:", response.status_code, response.text)

get_animal(input('input a name of animal: '))
get_animal('polar bear')

#2
"""
объединение 3 файлов с данными о ментальном здоровье сотрудников

в результате получаем файл с информацией о сотрудниках возрастом от 40 лет, 
которые работают больше 40 часов в неделю и у которых снижается продуктивность
"""
try:
    first=pd.read_csv('Files/health1.csv')
    second=pd.read_csv('Files/health2.csv')
    third=pd.read_csv('Files/health3.csv')
    files = [first, second, third]
except FileNotFoundError:
    print('file not found')
else:
    # проверка на пустые файлы
    for i in files:
        if i.empty:
            print(f'Warning:{i} file is empty')
    combined = pd.concat(files, ignore_index=True)
    filt = combined[(combined['Age'] >= 40) & (combined['Productivity_Change'] == 'Decrease') & (combined['Hours_Worked_Per_Week'] > 40)]
    filt.to_csv('Files/healthfiltered.csv', index=False)


