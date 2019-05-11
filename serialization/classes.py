"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""



import random
import uuid
import constants

class Car:
    def __init__(self, price:float, mileage:float ):
        self.price = price
        self.type = random.choice(constants.CARS_TYPES)
        self.producer = random.choice(constants.CARS_PRODUCER)
        self.number = str(uuid.uuid4())
        self.mileage = mileage


    # Автомобілі можна перівнювати між собою за ціною.
    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price

    # При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути
    def __str__(self):
        return f"This car: {self.price} USD, {self.type}, {self.producer}, {self.number}, {self.mileage} km."

    #Автомобіль має метод заміни номеру. Номер повинен відповідати UUID
    def change_num(self):
        self.number = str(uuid.uuid4())




class Garage:

    def __init__(self, places:int):
        self.places = places
        self.town = random.choice(constants.TOWNS)
        self.cars = []
        self.owner = None

    def free_places(self):
        '''Additional method - returns number of free places in the garage.'''
        free_places = self.places - len(self.cars)
        if free_places >= 0:
            return free_places
        else:
            print("Attention, you added manually more cars in the garage than it has place. Please remove extra cars")

    # Добавляє машину в гараж, якщо є вільні місця
    def add_car(self, new_car):
        if self.free_places() > 0:
            self.cars.append(new_car)
        else:
            print("Sorry, but there is no free places in the garage. Please choose other one.")

    # Забирає машину з гаражу.
    def remove_car(self, car_to_remove):
        if car_to_remove in self.cars:
            self.cars.remove(car_to_remove)
        else:
            print("Sorry, but this car is not available in the garage and cannot be removed.")

    # Вертає сумарну вартість всіх машин в гаражі.
    def hit_hat(self):
        total_cost = 0
        for car in self.cars:
            total_cost += car.price
        return total_cost


class Cesar:
    def __init__(self, name:str):
        self.name = name
        self.garages = []
        self.register_id = str(uuid.uuid4())


    def max_garages(self):
        """ Additional method:
        Return list of garages with maximum free places"""
        free_places = [garage.free_places() for garage in self.garages]
        max_garages = [garage for garage in self.garages if garage.free_places() == max(free_places)]
        return max_garages

    # Повертає ціну всіх його автомобілів.
    def hit_hat(self):
        total_cost = 0
        for garage in self.garages:
            for car in garage.cars:
                total_cost += car.price
        return total_cost

    # Вертає кількість гаріжів.
    def garages_count(self):
        return len(self.garages)

    # Вертає кількість машин.
    def сars_count(self):
        cars_count = 0
        for garage in self.garages:
            cars_count += len(garage.cars)


    # Додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    # Якщо вільних місць немає повинне вивести повідомлення про це.
    def add_car(self, new_car, garage=None):
        if garage:
            if garage in self.garages:
                if garage.free_places() > 0:
                    garage.cars.append(new_car)
                else:
                    print("Sorry, but this garage is full and has no free places. Please choose other garage.")
            else:
                print("Sorry, but this Cesar does not have this garage. Please choose other garage")
        else:
            if len(self.max_garages()) > 0:
                self.max_garages()[0].cars.append(new_car)  # add new_car in the first garage with maximum free places
            else:
                print("Sorry, but all the garages of the Cesar are full and have no free spaces")


    # Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()
    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()
    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

