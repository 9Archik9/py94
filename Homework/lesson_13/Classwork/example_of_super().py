class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name} from the Parent class!")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling the parent class __init__ method
        self.age = age

    def greet(self):
        super().greet()  # Calling the parent class greet method
        print(f"I am {self.age} years old.")


c = Child("Anna", 25)
c.greet()
