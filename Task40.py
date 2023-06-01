#Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import pandas as pd

pdf = pd.read_csv("california_housing_train.csv")
mean_value = pdf[(pdf['population'] < 500) & (pdf['population'] > 0)]['median_house_value'].mean()

print(f'Средняя стоимость дома, где кол-во людей от 0 до 500: {"%.3f" % mean_value}')