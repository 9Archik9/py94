from base_class import Things


class House(Things):
    def buy(self, person):
        if person.bank_amount >= 100 and person.chattel is not None:
            person.remove_from_bank(100)
            person.estate = 'house'
            print(f'{person.name} bought a house for 100 coins!')
        else:
            print(f'{person.name} does\'t have enough coins.')

    def sell(self, person):
        if person.estate == 'house':
            person.add_to_bank(100)
            person.estate = True
            print(f'{person.name} sold the house for 100 coins!')
        else:
            print(f'{person.name} does\'t have a house to sell.')


class Car(Things):
    def buy(self, person):
        if person.estate != 'house':
            print(f'{person.name} can\'t buy a car without owning a house.')
        elif person.bank_amount >= 40:
            person.remove_from_bank(40)
            person.chattel = True
            print(f'{person.name} bought a car for 40 coins!')
        else:
            print(f'{person.name} does\'t have enough coins.')

    def sell(self, person):
        if person.chattel == 'car':
            person.add_to_bank(40)
            person.chattel = ''
            print(f'{person.name} sold the car for 40 coins!')
        else:
            print(f'{person.name} does\'t have a car to sell.')
