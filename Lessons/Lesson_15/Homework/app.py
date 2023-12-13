from Person import Person

man = Person()
work_period = 20


def app():
    for _ in range(work_period):
        man.work()


app()
print(f'\n{man.name} worked {work_period} day and earned {man.bank_amount} coins in total\n')

man.buy_house()
man.buy_car()
man.buy_house()

print(f'{man.name} have {man.bank_amount} coins on bank account')
man.sell_house()
print(f'{man.name} have {man.bank_amount} coins on bank account')
man.sell_car()
