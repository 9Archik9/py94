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
    def move(self):
        print('Car drives')

    def launch(self):
        print('Engine is on')


duck = Duck()
duck.move()
duck.voice()

tiger = Tiger()
tiger.move()
tiger.voice()

car = Car()
car.launch()
car.move()
