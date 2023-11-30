class CustomNameError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid name: {self.name}'


class ConnectionRefused(Exception):
    def __str__(self):
        return 'File connection has not been established. Please call "connect_or_create" first'
