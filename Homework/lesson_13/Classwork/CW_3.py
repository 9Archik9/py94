from custom_errors import ConnectionRefused


class DataStorage:
    file = None

    @classmethod
    def connect_or_create(cls, file_path):
        try:
            with open(file_path, 'r') as f:
                cls.file = f.read()
                print(f"Connected to existing JSON file at '{file_path}'")
        except FileNotFoundError:
            with open(file_path, 'w'):
                cls.file = None
                print(f"Created a new JSON file at '{file_path}'")

    @classmethod
    def read(cls):
        try:
            if cls.file is None:
                raise ConnectionRefused
            return print(cls.file)
        except ConnectionRefused as e:
            print(e)


DataStorage.connect_or_create('example.json')
DataStorage.read()
