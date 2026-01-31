from game.base_location import BaseLocation
from game import base_location
from time import sleep
from game import utils

class InfoUser:
    _username = None
    _ID = None
    _CounterName = True
    _CounterID = True
    _NumbersCheckName = []
    _line = "•" * 45

    def __init__(self):
        for i in range(10):
            self._NumbersCheckName.append(i)
        print("[🥳] Добро пожаловать в игру❕")
        print("[📝] Прежде чем начать, узнаем имя и ID\n")
        print(self._line)
        utils.timer()
        self.GetUsername()

    def GetUsername(self):
        while True:
            if self._CounterName == True:
                self._username = input("[🤖] Твое имя: ")
                print(self._line)
                utils.timer()
            else:
                self._username = input("[☺️] Еще раз попробуй: ")
                print(self._line)
                utils.timer()
            NameSetCheck = set(self._username)
            for letter in NameSetCheck:
                for number in self._NumbersCheckName:
                    if letter == str(number):
                        print("[🚫] Цифры нельзя")
                        print(self._line)
                        utils.timer()
                        self._CounterName = False
                        self.GetUsername()
            break
        print(f"[✅] Принято: {self._username}")
        print(self._line)
        utils.timer()
        self.GetID()

    def GetID(self):
        self._ID = id(self._username)
        print(f"[🔄] Формируем ID: 🆔{self._ID}")
        print(self._line)
        self.start_game()


    def start_game(self):
        print("\n[🤖] Все готово, запускать игру?"); print("[1] - да😏      |      [0] - нет🫩")
        print(self._line)

        while True:
            action = input("[👤] ")
            print(self._line)
            utils.timer()
            try:
                action = int(action)
                if type(action) == int:
                    if action == 1 or action == 0:
                        break
                    else:
                        print("[🚫] 1 или 2")
                        print(self._line)
                        utils.timer()
            except ValueError:
                print("[🚫] Ответь нормально")
                print(self._line)
                utils.timer()

        if action == 1:
            print("\n[🥰] Хорошей игры!", end="")
            for i in range(5):
                sleep(0.4)
                print(".", end="")
            print()
            utils.another_location()
            menu = Menu(self._line)
            menu.start_menu()
        else:
            print("\n[🥲] Пока", end="")
            sleep(1)

class Tutorial:
    def __init__(self):
        pass


class Menu():
    def __init__(self, line):
        self._line = line

    def start_menu(self):
        print("""--------МЕНЮ ИГРЫ--------

1. Играть / продолжить
2. Сохранить игру
3. Настройки
4. Выйти
""")
        try:
            self._action = int(input("[🤖] Выберите команду: "))
            print(self._line)
            utils.timer()
        except ValueError:
            print("[🚫] Такой команды не существует")
        if self._action == 1:
            base_location = BaseLocation()
            base_location.menu()
        elif self._action == 2:
            print("[💾] Игра успешна сохранена!")

infouser = InfoUser()
tutorial = Tutorial()
