class Worker:

    def __init__(self, name, age, money, house):
        self.name = name
        self.age = age
        self.money = money
        self.house = house

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Money:", self.money)
        print("House:", self.house)

    def add_money(self, sum):
        self.money += sum
        print("Итоговая сумма", self.money)

    def make_deal(self, house, mon):
        self.money -= mon
        self.house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.money >= price:
            self.make_deal(house, price)
            print("Совершена покупка")
        else:
            print("Не хватает средств")

class House():
    def __init__(self, sqare, price):
        self.sqare = sqare
        self.price = price

    def final_price(self, discount):
        final_price = self.price * (100 - discount) / 100
        print("Финальная цена: ", final_price)
        return final_price

human1 = Worker("Матвей", 15, 0, None)
human1.info()
human1.add_money(10000)
human1.info()
house = House(100, 100000)
print(house.sqare, house.price)
discount = int(input("Скидка: "))
human1.buy_house(house, discount)
human1.add_money(100000)
human1.buy_house(house, discount)
human1.info()