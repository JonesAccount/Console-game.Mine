from time import sleep
from game import utils

class InfoUser:
    __username = None
    __ID = None
    __CounterName = True
    __CounterID = True
    __NumbersCheckName = []
    __line = "•" * 45

    def __init__(self):
        for i in range(10):
            self.__NumbersCheckName.append(i)
        print("[🥳] Добро пожаловать в игру❕")
        print("[📝] Прежде чем начать, узнаем имя и ID\n")
        print(self.__line)
        self.timer()
        self.GetUsername()

    def GetUsername(self):
        while True:
            if self.__CounterName == True:
                self.__username = input("[🤖] Твое имя: ")
                print(self.__line)
                self.timer()
            else:
                self.__username = input("[☺️] Еще раз попробуй: ")
                print(self.__line)
                self.timer()
            NameSetCheck = set(self.__username)
            for letter in NameSetCheck:
                for number in self.__NumbersCheckName:
                    if letter == str(number):
                        print("[🚫] Цифры нельзя")
                        print(self.__line)
                        self.timer()
                        self.__CounterName = False
                        self.GetUsername()
            break
        print(f"[✅] Принято: {self.__username}")
        print(self.__line)
        self.timer()
        self.GetID()

    def GetID(self):
        self.__ID = id(self.__username)
        print(f"[🔄] Формируем ID: 🆔{self.__ID}")
        print(self.__line)
        self.start_game()


    def start_game(self):
        print("\n[🤖] Все готово, запускать игру?"); print("[1] - да😏      |      [0] - нет🫩")
        print(self.__line)

        while True:
            action = input("[👤] ")
            print(self.__line)
            self.timer()
            try:
                action = int(action)
                if type(action) == int:
                    if action == 1 or action == 0:
                        break
                    else:
                        print("[🚫] 1 или 2")
                        print(self.__line)
                        self.timer()
            except ValueError:
                print("[🚫] Ответь нормально")
                print(self.__line)
                self.timer()

        if action == 1:
            print("\n[🥰] Хорошей игры!", end="")
            for i in range(5):
                sleep(0.4)
                print(".", end="")
            utils.clear_console()
            menu = Menu()
            menu.start_menu()
        else:
            print("\n[🥲] Пока", end="")
            for i in range(2):
                sleep(0.8)
            utils.clear_console()


    def timer(self):
        sleep(0.5)


class Tutorial:
    def __init__(self):
        pass


class Menu():
    def start_menu(self):
        print("""
        ===== MINER SIMULATOR =====

1. Играть / продолжить
2. Профиль игрока
3. Инвентарь
4. Шахта
5. Магазин
6. Настройки
7. Сохранить игру
0. Выйти

Выберите команду:
        """)


infouser = InfoUser()
tutorial = Tutorial()
