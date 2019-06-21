
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

cesar = cesar_from_file_yaml   # берем любой экземпляр Cesar из восстановленных из файлов, например из cesar.yaml

with open("new_cesar.yaml", "w") as file:
    yaml.dump(classes.Cesar.to_dict(cesar), file)

with open("new_cesar.json", "w") as file:
    json.dump(cesar, file, default=classes.Cesar.to_dict)

with open("new_cesar_pickle.txt", "wb") as file:
    pickle.dump(cesar, file)


# Class Car

car = car_from_file_pickle   # берем любой экземпляр Car из восстановленных из файлов, например из car_picle.txt

with open("new_car.yaml", "w") as file:
    yaml.dump(classes.Car.to_dict(car), file)

with open("new_car.json", "w") as file:
    json.dump(car, file, default=classes.Car.to_dict)

with open("new_car_pickle.txt", "wb") as file:
    pickle.dump(car, file)

# Class Garage:

garage = garage_from_file_json   # берем любой экземпляр Garage из восстановленных из файлов, например из garage.json

with open("new_garage.yaml", "w") as file:
    yaml.dump(classes.Garage.to_dict(garage), file)

with open("new_garage.json", "w") as file:
    json.dump(garage, file, default=classes.Garage.to_dict)

with open("new_garage_pickle.txt", "wb") as file:
    pickle.dump(garage, file)


# Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
# yaml, json, pickle відповідно.


# Class Cesar:

str_cesar_yaml = yaml.dump(classes.Cesar.to_dict(cesar))
str_cesar_json = json.dumps(cesar, default=classes.Cesar.to_dict)
str_cesar_pickle = pickle.dumps(cesar)

# Class Car:

str_car_yaml = yaml.dump(classes.Car.to_dict(car))
str_car_json = json.dumps(car, default=classes.Car.to_dict)
str_car_pickle = pickle.dumps(car)

# Clacc Garage

str_garage_yaml = yaml.dump(classes.Garage.to_dict(garage))
str_garage_json = json.dumps(garage, default=classes.Garage.to_dict)
str_garage_pickle = pickle.dumps(garage)



# Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
# з (yaml, json, pickle) строки відповідно


# Class Cesar:

restored_cesar_yaml = classes.Cesar.from_dict(yaml.load(str_cesar_yaml, Loader=yaml.Loader))
restored_cesar_json = classes.Cesar.from_dict(json.loads(str_cesar_json))
restored_cesar_pickle = pickle.loads(str_cesar_pickle)


# Class Car:

restored_car_yaml = classes.Car.from_dict(yaml.load(str_car_yaml, Loader=yaml.Loader))
restored_car_json = json.loads(str_car_json, object_hook=classes.Car.from_dict)
restored_car_pickle = pickle.loads(str_car_pickle)


# Clacc Garage

restored_garage_yaml = classes.Garage.from_dict(yaml.load(str_garage_yaml, Loader=yaml.Loader))
restored_garage_json = classes.Garage.from_dict(json.loads(str_garage_json))
restored_garage_pickle = pickle.loads(str_garage_pickle)

