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
