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
# Автомобіль має наступні характеристики:
#     price - значення типу float. Всі ціни за дефолтом в одній валюті.
#     type - одне з перечисленних значеннь з CARS_TYPES в docs.
#     producer - одне з перечисленних значеннь в CARS_PRODUCER.
#     number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
#     mileage - значення типу float. Пробіг автомобіля в кілометрах.

def to_json_car(obj):
    '''
        default method to serialize an instance of class Car to json
    '''
    data = {"price": obj.price,
            "type": obj.type,
            "producer": obj.producer,
            "number": obj.number,
            "mileage": obj.mileage}
    return data

def from_json_car(data):
    '''
        hook method to deserialized from json to an instance of class Car
    '''
    price = data["price"]
    mileage = data["mileage"]
    car_instance = classes.Car(price, mileage)
    car_instance.type = data.get("type", random.choice(constants.CARS_TYPES))
    car_instance.producer = data.get("producer", random.choice(constants.CARS_PRODUCER))
    car_instance.number = data.get("number", str(uuid.uuid4()))
    return car_instance


test_car = classes.Car(50000, 10000)

# Conversion test_car to string:
car_str_json = json.dumps(test_car, default=to_json_car)
print(car_str_json)

# Create Car object from string:

car_from_string = json.loads(car_str_json, object_hook=from_json_car)
print(f"Type of restored Car: {type(car_from_string)}")
print(car_from_string)


# Save condition of test_car in json file:

with open("car.json", "w") as file:
    json.dump(test_car, file, default=to_json_car)

# Create Car object from file:
with open("car.json") as file:
    car_from_file = json.load(file, object_hook=from_json_car)
print(f"Type of restored Car: {type(car_from_file)}")
print(car_from_file)


# 1.2. Class Garage

# Гараж має наступні характеристики:
#
#     town - одне з перечислениз значеннь в TOWNS
#     cars - список з усіх автомобілів які знаходяться в гаражі
#     places - значення типу int. Максимально допустима кількість автомобілів в гаражі
#     owner - значення типу UUID. За дефолтом None.

# class Garage:
#
#     def __init__(self, places:int):
#         self.places = places
#         self.town = random.choice(constants.TOWNS)
#         self.cars = []
#         self.owner = None



def to_json_garage(obj):
    '''
        default method to serialize an instance of class Garage to json
    '''
    data = {"places": obj.places,
            "town": obj.town,
            "cars": obj.cars,
            "owner": obj.owner}
    if obj.cars:
        serialized_cars = [json.dumps(car, default=to_json_car) for car in obj.cars]
        data["cars"] = serialized_cars
    return data

def from_json_garage(data):
    '''
        hook method to deserialized from json to an instance of class Garage
    '''
    places = data["places"]
    garage_instance = classes.Garage(places)
    garage_instance.town = data.get("town", random.choice(constants.TOWNS))
    garage_instance.owner = data.get("owner", None)
    if data["cars"]:
        restored_cars = [json.loads(car, object_hook=from_json_car) for car in data["cars"]]
        garage_instance.cars = restored_cars
    else:
        garage_instance.cars = []
    return garage_instance


test_garage = classes.Garage(500)
test_garage.cars = [classes.Car(1000, 900000), classes.Car(10000, 50)]
# Conversion test_garage to string:
garage_str_json = json.dumps(test_garage, default=to_json_garage)
print(garage_str_json)

# Create garage object from string:

garage_from_string = json.loads(garage_str_json, object_hook=from_json_garage)
print(f"Type of restored Garage: {type(garage_from_string)}")
print(garage_from_string)
for car in garage_from_string.cars:
    print(type(car), car)

# Save condition of test_garage in json file:

with open("garage.json", "w") as file:
    json.dump(test_garage, file, default=to_json_garage)

# Create Garage object from file:
with open("garage.json") as file:
    garage_from_file = json.load(file, object_hook=from_json_garage)
print(f"Type of restored garage: {type(garage_from_file)}")
print(garage_from_file)


# 1.3. class Cesar:

# Колекціонер має наступні характеристики
#     name - значення типу str. Його ім'я
#     garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
#     register_id - UUID; Унікальна айдішка Колекціонера.

def to_json_cesar(obj):
    '''
        default method to serialize an instance of class Cesar to json
    '''
    data = {"name": obj.name, "garages": obj.garages, "register_id": obj.register_id}
    if obj.garages:
        serialized_garages = [json.dumps(garage, default=to_json_garage) for garage in obj.garages]
        data["garages"] = serialized_garages
    return data

def from_json_cesar(data):
    '''
        hook method to deserialized from json to an instance of class Cesar
    '''
    name = data["name"]
    cesar_instance = classes.Cesar(name)
    cesar_instance.register_id = data.get("register_id", str(uuid.uuid4()))
    if data["garages"]:
        restored_garages = [json.loads(garage, object_hook=from_json_garage) for garage in data["garages"]]
        cesar_instance.garages = restored_garages
    else:
        cesar_instance.garages = []
    return cesar_instance


test_cesar = classes.Cesar("Vladislav")
print(type(test_cesar))
test_cesar.garages = [classes.Garage(50), test_garage]

# Conversion test_cesar to string:
cesar_str_json = json.dumps(test_cesar, default=to_json_cesar)
print(cesar_str_json)

# Create cesar object from string:

cesar_from_string = json.loads(cesar_str_json, object_hook=from_json_cesar)
print(f"Type of restored Cesar: {type(cesar_from_string)}")
print(cesar_from_string)
for garage in cesar_from_string.garages:
    print(garage.cars)                      # restored even cars from a Cesar's garage!!!


# Save condition of test_cesar in json file:

with open("cesar.json", "w") as file:
    json.dump(test_cesar, file, default=to_json_cesar)

# Create Cesar object from file:
with open("cesar.json") as file:
    cesar_from_file = json.load(file, object_hook=from_json_cesar)
print(f"Type of restored cesar: {type(cesar_from_file)}")
print(cesar_from_file)



# 2. Pickle serialization.

import pickle

# 2.1. Class Car


test_car_pickle = classes.Car(45000, 2000)

# Conversion test_car_pickle to pickle:
car_str_pickle = pickle.dumps(test_car_pickle)


# Create Car object from pickle:

car_from_pickle = pickle.loads(car_str_pickle)
print(f"Type of restored Car: {type(car_from_pickle)}")
print(car_from_pickle)


# Save condition of test_car_pickle in file car_pickle.txt:

with open("car_pickle.txt", "wb") as file:
    pickle.dump(test_car_pickle, file)

# Create Car object from file:
with open("car_pickle.txt", "rb") as file:
    car_from_pickle_file = pickle.load(file)
print(f"Type of restored Car: {type(car_from_pickle_file)}")
print(car_from_pickle_file)


# 2.2. Class Garage


test_garage_pickle = classes.Garage(90)
test_garage.cars = [classes.Car(1000, 900000), classes.Car(10000, 50)]
# Conversion test_garage to pickle:
garage_str_pickle = pickle.dumps(test_garage_pickle)


# Create garage object from pickle:

garage_from_pickle = pickle.loads(garage_str_pickle)
print(f"Type of restored Garage: {type(garage_from_pickle)}")
print(garage_from_pickle)
for car in garage_from_pickle.cars:
    print(type(car), car)

# Save condition of test_garage in file garage_pickle.txt:

with open("garage_pickle.txt", "wb") as file:
    pickle.dump(test_garage_pickle, file)

# Create Garage object from file:
with open("garage_pickle.txt", "rb") as file:
    garage_from_pickle_file = pickle.load(file)
print(f"Type of restored garage: {type(garage_from_pickle_file)}")
print(garage_from_pickle_file)


# 2.3. class Cesar:


test_cesar_pickle = classes.Cesar("Olga")
print(type(test_cesar_pickle))
test_cesar_pickle.garages = [classes.Garage(80), test_garage]

# Conversion test_cesar_pickle to pickle:
cesar_str_pickle = pickle.dumps(test_cesar_pickle)
print(cesar_str_pickle)

# Create cesar object from pickle:

cesar_from_pickle = pickle.loads(cesar_str_pickle)
print(f"Type of restored Cesar: {type(cesar_from_pickle)}")
print(cesar_from_pickle)
for garage in cesar_from_pickle.garages:
    print(garage.cars)                      # restored even cars from a Cesar's garage!!!


# Save condition of test_cesar in json file:

with open("cesar_pickle.txt", "wb") as file:
    pickle.dump(test_cesar_pickle, file)

# Create Cesar object from file:
with open("cesar_pickle.txt", "rb") as file:
    cesar_from_pickle_file = pickle.load(file)
print(f"Type of restored cesar: {type(cesar_from_pickle_file)}")
print(cesar_from_pickle_file)