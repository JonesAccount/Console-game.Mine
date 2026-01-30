from time import sleep

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
        print("[📝] Прежде чем начать, узнаем о тебе\n")
        print(self.__line)
        self.timer()

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
        self.ID()

    def ID(self):
        while True:
            try:
                if self.__CounterID == True:
                    self.__ID = int(input("[🤖] Твой ID из 4 цифр: "))
                else:
                    self.__ID = int(input("[☺️] Еще раз попробуй: "))
                print(self.__line)
                if len(str(self.__ID)) != 4:
                    print("[🚫] Нужно ввести 4 цифры")
                    self.__CounterID = False
                    print(self.__line)
                    continue
                else:
                    break
            except ValueError:
                self.__CounterID = False
                print(self.__line)

        print(f"[✅] Принято: ID:{self.__ID}")
        print(self.__line)
        self.timer()

    def timer(self):
        sleep(0.5)

infouser = InfoUser()
infouser.GetUsername()