#Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import csv

with open('california_housing_train.csv', encoding='utf-8') as csv_file:
    # считываем содержимое файла
    text = csv.DictReader(csv_file, delimiter=',') #csv перегоняю в список словарей
    count = 0 # счетчик для определения количества домов с кол-вом жильцов меньше 500
    medial_value = 0 # общая стоимость всех домов с кол-вом жильцов меньше 500
    for row in text:
        if int(row['population'].split(".")[0]) < 500:
            count += 1
            medial_value += int(row['population'].split(".")[0])
print(f"Средняя стоимиость дома: {medial_value/count}")