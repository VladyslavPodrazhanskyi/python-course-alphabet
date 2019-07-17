import unittest
from classes import Car, Garage, Cesar
from constants import CARS_PRODUCER, CARS_TYPES, TOWNS
from uuid import uuid4, UUID


# 1) Tests for class Car:
class CarTest(unittest.TestCase):

    def setUp(self):
        """Create 2 cars for testing"""
        self.car1 = Car(45000, 10000)
        self.car2 = Car(8000, 150000)

    # Testing fields of cars:
    def test_car_price(self):
        """Tests of cars' prices"""
        self.assertEqual(self.car1.price, 45000)
        self.assertEqual(self.car2.price, 8000)

    def test_car_mileage(self):
        """Tests of cars' mileage"""
        self.assertEqual(self.car1.mileage, 10000)
        self.assertEqual(self.car2.mileage, 150000)

    def test_car_type(self):
        """Tests of cars' types"""
        self.assertIsInstance(self.car1.type, str)
        self.assertIsInstance(self.car2.type, str)

        self.assertIn(self.car1.type, CARS_TYPES)
        self.assertIn(self.car2.type, CARS_TYPES)

    def test_car_producer(self):
        """Tests of cars' producers"""
        self.assertIsInstance(self.car1.producer, str)
        self.assertIsInstance(self.car2.producer, str)

        self.assertIn(self.car1.producer, CARS_PRODUCER)
        self.assertIn(self.car2.producer, CARS_PRODUCER)

    def test_car_unique_number(self):
        """Tests for cars' numbers
        1) Check that cars' numbers are of uuid format
        2) Checking that numbers of 2 cars are not equal
        """
        self.assertIsInstance(self.car1.number, UUID)
        self.assertIsInstance(self.car2.number, UUID)

        self.assertNotEqual(self.car1.number, self.car2.number)

    # Testing methods of cars:

    def test_change_num(self):
        """Tests of method change_num of class Car:

                1) Check that new numbers of a car is not equal to its previous number
                2) Check that new car number is of uuid format
        """
        previous_number = self.car1.number
        self.car1.change_num()
        new_number = self.car1.number

        self.assertNotEqual(new_number, previous_number)
        self.assertIsInstance(new_number, UUID)

    def test_cars_compare(self):
        """Cars can be compared by price. This test check it.
        Price of car1 is higher than that of car2
        """
        self.assertGreater(self.car1, self.car2)


# 2) Tests for class Garage:
class GarageTest(unittest.TestCase):
    def setUp(self):
        """Create 2 garages and 10 cars for testing"""
        self.garage1 = Garage(3)
        self.garage2 = Garage(2)
        self.garage3 = Garage(1)
        self.car1 = Car(50000, 0)
        self.car2 = Car(70000, 100)
        self.car3 = Car(15000, 100000)
        self.car4 = Car(8000, 150000)
        self.car5 = Car(3000, 500000)
        self.car6 = Car(25000, 0)
        self.car7 = Car(45000, 10000)
        self.car8 = Car(7500, 300000)
        self.car9 = Car(500, 800000)
        self.car10 = Car(11000, 200000)

    # Testing fields of garages:

    def test_garage_places(self):
        """Tests of garage's places"""
        self.assertEqual(self.garage1.places, 3)
        self.assertIsInstance(self.garage1.places, int)

    def test_garage_towns(self):
        """Tests of garage's town"""
        self.assertIsInstance(self.garage1.town, str)
        self.assertIn(self.garage1.town, TOWNS)

    def test_garage_default_cars(self):
        """Tests of default cars of the garage, should be empty list"""
        self.assertIsInstance(self.garage1.cars, list)
        self.assertEqual(len(self.garage1.cars), 0)

    def test_garage_default_owner(self):
        """Tests of default owner of the garage, should be NONE"""
        self.assertEqual(self.garage1.owner, None)

    # Testing methods of garages:

    def test_free_places(self):
        """Tests of method free_places of class Garage:

        1) Check of method free_places by default of 3 garages
        2) Add list of 3 cars for garage 1. Number of free_places should be 0
        3) Add list of 1 car for garage 2. Number of free_places should be 1
        4) Add list of 4 cars for garage 3. It's more than it can contain. Method returns None,
        because the garages will not be added

        """
        self.assertEqual(self.garage1.free_places(), 3)
        self.assertEqual(self.garage2.free_places(), 2)
        self.assertEqual(self.garage3.free_places(), 1)

        self.garage1.cars = [self.car1, self.car2, self.car3]
        self.assertEqual(self.garage1.free_places(), 0)

        self.garage2.cars = [self.car4]
        self.assertEqual(self.garage2.free_places(), 1)

        self.garage3.cars = [self.car5, self.car6, self.car7, self.car8]
        self.assertEqual(self.garage3.free_places(), None)

    def test_add_car(self):
        """Tests of method add_car of class Garage:

        1) Check if method add_cars works for garage with empty list of cars (by default)
        2) Check if method add_cars works for garage with not empty list of cars but with free places
        3) Check if method add_cars does not add new car if there is no free places in the garage.

        """
        self.garage2.add_car(self.car1)
        expected_result1 = [self.car1]
        real_result1 = self.garage2.cars
        self.assertEqual(real_result1, expected_result1)

        self.garage2.add_car(self.car2)
        expected_result2 = [self.car1, self.car2]
        real_result2 = self.garage2.cars
        self.assertEqual(real_result2, expected_result2)

        self.garage2.add_car(self.car3)  # garage2 is full and car3 cannot be added
        false_result = [self.car1, self.car2, self.car3]  # if method add a car even if there is no free spaces
        expected_result3 = [self.car1, self.car2]
        real_result3 = self.garage2.cars
        self.assertNotEqual(real_result3, false_result)
        self.assertEqual(real_result3, expected_result3)

    def test_remove_car(self):
        """Tests of method remove_car of class Garage:

        1) add 2 cars to garage1 and remove car1 from the garage,
        check if car1 was removed and car2 is available.

        2) remove car2 from the garage and check that list of cars is empty.

        """
        self.garage1.add_car(self.car1)
        self.garage1.add_car(self.car2)

        self.garage1.remove_car(self.car1)
        expected_result1 = [self.car2]
        real_result1 = self.garage1.cars
        self.assertEqual(real_result1, expected_result1)

        self.garage1.remove_car(self.car2)
        expected_result2 = []
        real_result2 = self.garage1.cars
        self.assertEqual(real_result2, expected_result2)

    def test_hit_hat(self):
        """Test of method hit_hat

        Add all 3 cars to garage1 and check if total cost of all cars calculated correctly(135000).
        Check that incorect value e.g. 15000 is not working
        """
        self.garage1.add_car(self.car1)
        self.garage1.add_car(self.car2)
        self.garage1.add_car(self.car3)

        self.assertEqual(self.garage1.hit_hat(), 135000)
        self.assertNotEqual(self.garage1.hit_hat(), 15000)


# 3) Testing of class Cesar:

class CesartTests(unittest.TestCase):
    def setUp(self):
        """Create 20 cars, 7 Garages, and 3 Cesars for testing"""
        self.car1 = Car(50000.00, 0)
        self.car2 = Car(70000.00, 100)
        self.car3 = Car(15000, 100000.00)
        self.car4 = Car(8000, 150000)
        self.car5 = Car(3000, 500000)
        self.car6 = Car(25000.00, 0)
        self.car7 = Car(45000, 10000)
        self.car8 = Car(7500, 300000)
        self.car9 = Car(500, 800000)
        self.car10 = Car(11000, 200000)
        self.car11 = Car(200000, 0)
        self.car12 = Car(180000, 10000)
        self.car13 = Car(150000, 200000)
        self.car14 = Car(100000, 500000)
        self.car15 = Car(40000, 1000000)
        self.car16 = Car(17000, 111115)
        self.car17 = Car(18000, 100000)
        self.car18 = Car(19000, 75000)
        self.car19 = Car(20000, 60000)
        self.car20 = Car(25000, 0)

        self.garage1 = Garage(3)  # has no cars, 3 empty places, total cost of cars = 0

        self.garage2 = Garage(2)
        self.garage2.cars = [self.car1, self.car2]  # has 2 cars, no empty places, total cost of cars  = 120 000

        self.garage3 = Garage(1)
        self.garage3.cars = [self.car3]  # has 1 car, no empty places,  total cost of cars =  15 000

        self.garage4 = Garage(10)  # has 5 cars, 5 empty places, total cost of cars = 88 500
        self.garage4.cars = [
            self.car4,
            self.car5,
            self.car6,
            self.car7,
            self.car8
        ]

        self.garage5 = Garage(5)
        self.garage5.cars = [self.car9, self.car10]  # has 2 cars, 3 empty places, total cost of cars = 11 500

        self.garage6 = Garage(6)  # has 5 cars, 1 empty place, total cost of cars = 670000
        self.garage6.cars = [
            self.car11,
            self.car12,
            self.car13,
            self.car14,
            self.car15
        ]

        self.garage7 = Garage(4)  # has 2 cars, 2 empty places, total cost of cars = 35000
        self.garage7.cars = [self.car16, self.car17]

        self.cesar1 = Cesar("Trump")

        self.cesar2 = Cesar("Soros")
        self.cesar2.garages = [self.garage1, self.garage5, self.garage7]

        self.cesar3 = Cesar("Bezos")
        self.cesar3.garages = [self.garage2, self.garage3, self.garage6]

    # Testing fields of cesars:

    def test_cesar_name(self):
        """Tests of garage's names"""
        self.assertEqual(self.cesar1.name, "Trump")
        self.assertEqual(self.cesar2.name, "Soros")

    def test_cesar_garages(self):
        """Tests field garages of the cesar"""
        self.assertIsInstance(self.cesar1.garages, list)
        self.assertIsInstance(self.cesar2.garages, list)

        self.assertEqual(len(self.cesar1.garages), 0)
        self.assertEqual(len(self.cesar2.garages), 3)

    def test_cesar_register_id(self):
        """Tests for cesar's register_id:
        1) Check that cesar's register_id is of uuid format
        2) Checking that numbers of 2 cesars are not equal
        """
        self.assertIsInstance(self.cesar1.register_id, UUID)
        self.assertIsInstance(self.cesar2.register_id, UUID)

        self.assertNotEqual(self.cesar1.register_id, self.cesar2.register_id)

    # Testing methods of cesars:

    def test_max_garages(self):
        """Tests of method max_garages of class Cesar:

        1) Check of the method max_garages for cesar1 with empty list of garages by default.

        2) Check of the method max_garages for cesar2 that has 2 garages with maximum free places

        3) Check of the method max_garages for cesar3 that has 1 garages with maximum free places

        """
        real_result1 = self.cesar1.max_garages()
        expected_result1 = []
        self.assertEqual(real_result1, expected_result1)

        real_result2 = self.cesar2.max_garages()
        expected_result2 = [self.garage1, self.garage5]
        self.assertEqual(real_result2, expected_result2)

        real_result3 = self.cesar3.max_garages()
        expected_result3 = [self.garage6]
        self.assertEqual(real_result3, expected_result3)

    def test_hit_hat(self):
        """Tests of method hit_hat of class Cesar:
        """
        self.assertEqual(self.cesar1.hit_hat(), 0)
        self.assertEqual(self.cesar2.hit_hat(), 46500)
        self.assertEqual(self.cesar3.hit_hat(), 805000)

    def test_garages_count(self):
        """Tests of method garages_count of class Cesar:
        """
        self.assertEqual(self.cesar1.garages_count(), 0)
        self.assertEqual(self.cesar2.garages_count(), 3)
        self.assertEqual(self.cesar3.garages_count(), 3)

    def test_cars_count(self):
        """Tests of method cars_count of class Cesar:
        """
        self.assertEqual(self.cesar1.cars_count(), 0)
        self.assertEqual(self.cesar2.cars_count(), 4)
        self.assertEqual(self.cesar3.cars_count(), 8)

    def test_add_car(self):
        """Tests of method add_car of class Cesar:

        1. Try to add car18 to cesar1. It has no garages, so method must not add the car.
        2. Try to add car18 to cesar2 to the garage2 which does not belongs to cesar2, method must not add the car
        3. Add car18 to cesar2. It has max free places in garage 1 and 5 and therefore car must be added in garage1
        4. Add car19 to cesar3. It has free places in garage6 only, it has index 2 of list garages of the cesar3
        5. Add car20 to cesar2 in its garage5 that has index 1 in the list of garages of cesar2
        """
        self.cesar1.add_car(self.car18)
        self.assertEqual(self.cesar1.cars_count(), 0)

        self.cesar2.add_car(self.car18, self.garage2) # try to add car18 to cesar2 to garage that belongs to cesar3
        for garage in self.cesar2.garages:
            self.assertNotIn(self.car18, garage.cars) # check that car 18 is not available in any garages of cesar2
        self.assertEqual(self.cesar2.cars_count(), 4) # check that quantity of cars of cesar2 was not changed
        self.assertEqual(self.cesar3.cars_count(), 8) # check that quantiy of cars of cesar3 was not changed


        self.cesar2.add_car(self.car18)
        self.assertIn(self.car18, self.cesar2.garages[0].cars)
        self.assertEqual(self.cesar2.cars_count(), 5)

        self.cesar3.add_car(self.car19)
        self.assertIn(self.car19, self.cesar3.garages[2].cars)
        self.assertEqual(self.cesar3.cars_count(), 9)

        self.cesar2.add_car(self.car20, self.garage5)
        self.assertIn(self.car20, self.cesar2.garages[1].cars)
        self.assertEqual(self.cesar2.cars_count(), 6)

    def test_cesars_compare(self):
        """Testing methods __eq__, __gt__, __lt__"""

        self.assertTrue(self.cesar1 < self.cesar2)
        self.assertFalse(self.cesar2 == self.cesar3)
        self.assertTrue(self.cesar3 > self.cesar1)


if __name__ == "__main__":
    unittest.main()
