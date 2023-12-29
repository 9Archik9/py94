from Person import Person
from market import House, Car

man = Person()
house = House()
car = Car()
work_period = 22


def app():
    for _ in range(work_period):
        man.work()


app()

print(f'\n{man.name} worked {work_period} day and earned {man.bank_amount} coins in total\n')

car.buy(man)
house.buy(man)
car.buy(man)

print(f'{man.name} have {man.bank_amount} coins on bank account')
house.sell(man)
print(f'{man.name} have {man.bank_amount} coins on bank account')
car.sell(man)
