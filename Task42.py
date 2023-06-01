# Задача 42: Узнать какая максимальная households
# в зоне минимального значения population

import pandas as pd

data = pd.read_csv('california_housing_train.csv', sep=',')
min_value_population = data["population"].min() #нахожу минимальное значение в столбце population

# провожу выборку по столбцу population и ищу все строки с минимальным значением в колонке population
# нахожу максимальное значение по households из всех минимальных population
max_value = data[data['population'] == min_value_population]['households'].max()
print(f"Максимальная households в зоне минимального значения population: {max_value}")
