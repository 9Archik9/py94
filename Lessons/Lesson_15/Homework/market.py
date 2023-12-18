from base_class import Things


class House(Things):
    def buy(self, person):
        if person.bank_amount >= 100:
            person.remove_from_bank(100)
            person.estate_count += 1
            print(f'{person.name} bought a house for 100 coins!')
        else:
            print(f'{person.name} does\'t have enough coins.')

    def sell(self, person):
        if person.estate_count > 0:
            person.add_to_bank(100)
            person.estate_count -= 1
            print(f'{person.name} sold a house for 100 coins!')
        else:
            print(f'{person.name} does\'t have a house to sell.')


class Car(Things):
    def buy(self, person):
        if person.estate_count > 0:
            if person.bank_amount >= 40:
                person.remove_from_bank(40)
                person.chattel_count += 1
                print(f'{person.name} bought a car for 40 coins!')
            else:
                print(f'{person.name} does\'t have enough coins.')
        else:
            print(f'{person.name} can\'t buy a car without owning a house.')

    def sell(self, person):
        if person.chattel_count > 0:
            person.add_to_bank(40)
            person.chattel_count -= 1
            print(f'{person.name} sold a car for 40 coins!')
        else:
            print(f'{person.name} does\'t have a car to sell.')
