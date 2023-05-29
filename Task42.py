# Задача 42: Узнать какая максимальная households (index = 6)
# в зоне минимального значения population (index = 5) .

import pandas as pd

data = pd.read_csv('california_housing_train.csv', sep=',')
min_pop = data["population"].min()  # ищем минимум по столбцу population
# в слевой части условие прописываем а в правой название столбцов которые надо отображать
print(data[data["population"] == min_pop][["households", "population"]])
