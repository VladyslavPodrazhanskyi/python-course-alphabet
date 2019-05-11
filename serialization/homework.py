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

# 1. JSON serialization.
import random
import json
import classes
import constants
import uuid



# 1.1. Class Car


def to_json(obj):
    '''
        default method to serialize an instance of class Car to json
    '''
    data = {"price": obj.price,
            "type": obj.type,
            "producer": obj.producer,
            "number": obj.number,
            "mileage": obj.mileage}
    return data

def from_json(data):
    '''
        hook method to deserialized from json to an instance of class Car
    '''
    price = data["price"]  # обязательные параметры, кот. вводятся при создании объекта
    mileage = data["mileage"]  # обязательный объект, кот. вводится при создании объекта.
    car_instance = classes.Car(price, mileage) # воссоздание экземпляра класса по обязательным атрибутам
    car_instance.type = data.get("type", random.choice(constants.CARS_TYPES)) # прописываем необязат. атрибуты
    car_instance.producer = data.get("producer", random.choice(constants.CARS_PRODUCER))
    car_instance.number = data.get("number", str(uuid.uuid4()))
    return car_instance


test_car = classes.Car(50000, 10000)

# Conversion test_car to string:
car_str_json = json.dumps(test_car, default=to_json)
print(car_str_json)

# Create Car object from string:

car_from_string = json.loads(car_str_json, object_hook=from_json)
print(f"Type of restored Car: {type(car_from_string)}")
print(car_from_string)


# Save condition of test_car in json file:

with open("car.json", "w") as file:
    json.dump(test_car, file, default=to_json)

# Create Car object from file:
with open("car.json") as file:
    car_from_file = json.load(file, object_hook=from_json)
print(f"Type of restored Car: {type(car_from_file)}")
print(car_from_file)


# 1.2. Class Garage

