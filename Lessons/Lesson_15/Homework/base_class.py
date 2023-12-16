class Human:
    def __init__(self):
        self.name = input('Enter your name: ')
        self.__bank_amount = 0
        self.estate = None  # house
        self.chattel = None  # car

    def __str__(self):
        return self.name

    @property
    def bank_amount(self):
        return self.__bank_amount

    def add_to_bank(self, amount):
        self.__bank_amount += amount

    def remove_from_bank(self, amount):
        self.__bank_amount -= amount

    def work(self):
        raise NotImplementedError


class Things:
    def buy(self, person):
        raise NotImplementedError

    def sell(self, person):
        raise NotImplementedError
