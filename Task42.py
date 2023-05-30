# Задача 42: Узнать какая максимальная households (index = 6)
# в зоне минимального значения population (index = 5) .

import pandas as pd

data = pd.read_csv('california_housing_train.csv', sep=',')

# в слевой части условие прописываем (ищем строку с минимальным population)
# а в правой название столбцов которые надо отображать в найденой строке
print("Значение households при минимальноем population")
print(data[data["population"] == data["population"].min()][["households", "population"]])
print()
print("Значение households в области минимальной population")
print(data[(data["population"] <= (data["population"].min() + 10)) &
      (data["population"] >= (data["population"].min() - 10))][["households", "population"]])
print()
# Поиск максимума среди всех минимумов
dl = data[(data["population"] <= (data["population"].min() + 10)) &
      (data["population"] >= (data["population"].min() - 10))][["households"]].max()
dl1 = dl["households"]
print(f"Максимальная households в области минимальной population: {dl1}")

