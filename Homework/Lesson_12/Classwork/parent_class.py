class Auto:
    def __init__(self, brand, age, mark, color='Unknown', weight='Unknown'):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("Move")

    def stop(self):
        print("Stop")

    def birthday(self):
        self.age += 1
