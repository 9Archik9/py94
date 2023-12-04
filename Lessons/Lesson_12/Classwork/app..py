import time
from parent_class import Auto


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='Unknown', weight='Unknown'):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("Attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("Load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='Unknown', weight='Unknown'):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"Max speed is {self.max_speed}")


# Создание объектов Truck и Car
truck1 = Truck(brand="Volvo", age=3, mark="VNL", max_load=2000, color="Blue", weight="5000kg")
truck2 = Truck(brand="Mercedes", age=5, mark="Actros", max_load=3000, color="White", weight="6000kg")

car1 = Car(brand="Toyota", age=2, mark="Camry", max_speed=180, color="Red", weight="1500kg")
car2 = Car(brand="BMW", age=1, mark="X5", max_speed=220, color="Black", weight="2000kg")

# Проверка методов и атрибутов объектов
print("Trucks:")
truck1.move()
truck1.load()
print(f"Truck 1 max load: {truck1.max_load}")

truck2.move()
truck2.load()
print(f"Truck 2 max load: {truck2.max_load}")

print("\nCars:")
car1.move()
print(f"Car 1 max speed: {car1.max_speed}")

car2.move()
print(f"Car 2 max speed: {car2.max_speed}")
