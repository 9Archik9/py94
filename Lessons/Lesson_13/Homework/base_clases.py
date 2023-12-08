class DataStorage:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.status = 'disconnected'
        self.content = None

    @property
    def file_path(self):
        return self.__file_path

    def _create_storage(self):
        with open(self.__file_path, 'w'):
            ...
        return open(self.__file_path, 'a+')

    def connect(self):
        try:
            file = open(self.__file_path, 'r')
            self.content = file.read()
            self.status = 'connected'
            file.close()
            print('File opened')
        except FileNotFoundError:
            file = self._create_storage()
            self.content = file.read()
            self.status = 'connected'
            file.close()
            print('File created')
        return open(self.__file_path, 'a+')

    @staticmethod
    def disconnect(file):
        file.close()
        print('File closed')
