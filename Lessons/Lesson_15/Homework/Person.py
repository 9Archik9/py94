from base_class import Human

from random import randint


class Person(Human):
    def __init__(self):
        super().__init__()

    def work(self):
        earned_money = randint(5, 10)
        print(f'{self.name} earned {earned_money} coins in one day')
        self.add_to_bank(earned_money)

    def buy_house(self):
        if self.chattel:
            if self.bank_amount >= 100:
                self.remove_from_bank(100)
                self.estate = True
                print(f'{self.name} bought a house! 100 coins were debited from the bank account')
            else:
                print(f'{self.name} doesnt have enough money to buy a house')
        else:
            print(f'{self.name} needs to buy a car first before buying a house')

    def buy_car(self):
        if self.bank_amount >= 40:
            self.remove_from_bank(40)
            self.chattel = True
            print(f'{self.name} bought a car! 40 coins were debited from the bank account')
        else:
            print(f'{self.name} doesnt have enough money to buy a car')

    def sell_house(self):
        self.add_to_bank(100)
        self.estate = None
        print(f'{self.name} sell house! 100 coins were debited')

    def sell_car(self):
        self.add_to_bank(40)
        self.estate = None
        print(f'{self.name} sell car! 40 coins were debited')
