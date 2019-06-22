from __future__ import annotations
import pickle


class Programmer:

    def __init__(self, name, language="Python", position="Junior") -> None:
        self.name = name
        self.language = language
        self.position = position
        self.enough_coffee = False

    def __str__(self):
        return f"Programmer. Name: {self.name}." \
            f"Lang :{self.language}; Position: {self.position} developer"
# setstate and getstate сейчас установлены по дефолту и никак не воздействуют на код.
# setstate испльзуется для десериализации.
    def __setstate__(self, state):    # принимает состояние объекта как словарь для воостановления объекта
        self.__dict__ = state
# getstat используется для сериализации (принимает объект, возвращает словарь с параметрами, кот будет превращен в байт
    def __getstate__(self):
        return self.__dict__


if __name__ == "__main__":
    programmer = Programmer("Captain America")
    programmer.enough_coffee = True
    # Lets dump object to pickle
    with open("data.txt", "wb") as file:
        pickle.dump(programmer, file)

    # Lets load it
    with open("data.txt", "rb") as file:
        restore_obj = pickle.load(file)
        print(type(restore_obj))
