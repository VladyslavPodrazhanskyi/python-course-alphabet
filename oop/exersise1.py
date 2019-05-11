# Polymorhpizm

class Cat:
    def speak(self):
        return "Weow"


class Dog:
    def speak(self):
        return "Wof"

class Cow:
    def speak(self):
        return "Moo"


cat = Cat()
dog = Dog()
cow = Cow()

print(cat.speak(), dog.speak(), cow.speak())