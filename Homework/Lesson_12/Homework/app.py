from base_classes import *


class Duck(Animal):
    def voice(self):
        print('Krya!')

    def move(self):
        print('Duck swimming...')


class Tiger(Animal):
    def voice(self):
        print('Hrrrr!')

    def move(self):
        print('Tiger running...')


class Car(Transport):
    def __init__(self):
        self.status = 'off'

    def move(self):
        if self.status == 'on':
            print('Car drives')
        else:
            print('Please, start the engine')

    def launch(self):
        self.status = 'on'
        print('Engine is on')


duck = Duck()
tiger = Tiger()

for animal in (duck, tiger):
    animal.move()
    animal.voice()
    print()

car = Car()
car.launch()
car.move()
