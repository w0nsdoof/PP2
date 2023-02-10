class account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, n:int):
        self.balance += n
        # print(f" Пополнение: {n} \n    Баланс:  {self.balance}")

    def withdrawl(self, n:int):
        if n > self.balance:
            print("   Запрос превышает сумму на балансе   ")
        else:
            self.balance -= n
            # print(f" Снято: {n} \nБаланс: {self.balance}" )
    def info(self):
        print("Владелец: " + str(self.owner))
        print(f"Баланс: {self.balance}")

