
"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""

import classes
import json
import pickle
import ruamel.yaml as yaml


# Для попереднього домашнього завдання.
# Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
# з (yaml, json, pickle) файлу відповідно

# Cesar from file
with open("cesar.yaml") as file:
    cesar_from_file_yaml = classes.Cesar.from_dict(yaml.load((file), Loader=yaml.Loader))

with open("cesar.json") as file:
    cesar_from_file_json = classes.Cesar.from_dict(json.load(file))

with open("cesar_pickle.txt", "rb") as file:
    cesar_from_file_pickle = pickle.load(file)

# Car from file
with open("car.yaml") as file:
    car_from_file_yaml = classes.Car.from_dict(yaml.load(file, Loader=yaml.Loader))

with open("car.json") as file:
    car_from_file_json = json.load(file, object_hook=classes.Car.from_dict)

with open("car_pickle.txt", "rb") as file:
    car_from_file_pickle = pickle.load(file)

# Garage from file
with open("garage.yaml") as file:
    garage_from_file_yaml = classes.Garage.from_dict(yaml.load((file), Loader=yaml.Loader))

with open("garage.json") as file:
    garage_from_file_json = classes.Garage.from_dict(json.load(file))

with open("garage_pickle.txt", "rb") as file:
    garage_from_file_pickle = pickle.load(file)

# Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли
# формату yaml, json, pickle відповідно.

# Class Cesar:

cesar = cesar_from_file_yaml   # берем любой экземпляр Cesar из восстановленных из файлов.


