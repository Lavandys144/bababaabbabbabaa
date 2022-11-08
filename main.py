class Worker:

    def __init__(self, name, age, money, surname, patronymic):
        self.name = name
        self.age = age
        self.money = money
        self.surname = surname
        self.patronymic = patronymic 

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Money:", self.money)
        print("Surname:", self.surname)
        print("Patronymic:", self.patronymic)
        

    def add_money(self, sum):
        self.money += sum
        print("Зарплата", self.money)

worker1 = Worker("Матвей", 15, 0, None)
worker1.info()
worker1.add_money(10000)
human1.info()
house = House(100, 100000)
print(house.sqare, house.price)
discount = int(input("Скидка: "))
human1.buy_house(house, discount)
human1.add_money(100000)
human1.buy_house(house, discount)
human1.info()
