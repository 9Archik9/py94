from base_class import Human

from random import randint


class Person(Human):
    def __init__(self):
        super().__init__()

    def work(self):
        earned_money = randint(5, 10)
        print(f'{self.name} earned {earned_money} coins in one day')
        self.add_to_bank(earned_money)
