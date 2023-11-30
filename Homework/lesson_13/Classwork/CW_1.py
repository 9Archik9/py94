from custom_errors import CustomNameError


class User:
    def __init__(self, name):
        if not isinstance(name, str) or ' ' in name:
            raise CustomNameError(name)

        self.name = name
        print(f'{self.name} is valid!')


user1 = User("art")
