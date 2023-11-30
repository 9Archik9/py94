class CustomNameError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid name: {self.name}'


class User:
    def __init__(self, name):
        if not isinstance(name, str) or ' ' in name:
            raise CustomNameError(name)

        self.name = name
        print(f'{self.name} is valid!')


user1 = User("art")
