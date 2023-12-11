from base_clesses import BaseHandler
import json


class FileWorker(BaseHandler):
    def __init__(self, file_path):
        try:
            with open(file_path):
                pass  # open file to check exist
        except FileNotFoundError:
            raise FileNotFoundError(f'The file {file_path} does not exist')
        self.file_path = file_path
        self.handler = self._get_handler()

    def read(self):
        return self.handler.read()

    def append(self, content):
        return self.handler.append(content)

    def close(self):
        return self.handler.close()

    def _get_handler(self):
        if self.file_path.endswith('json'):
            return JsonHandler(self.file_path)
        elif self.file_path.endswith('txt'):
            return TxtHandler(self.file_path)
        else:
            raise ValueError('Incorrect input data. Expected json or txt')


class JsonHandler(BaseHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def open_file(self, mode):
        self.file = open(self.file_path, mode)

    def read(self):
        try:
            self.open_file('r')
            data = json.load(self.file)
            return data
        except json.decoder.JSONDecodeError:
            raise ValueError(
                'The contents of the file must be a list data type. Please reformat the file')  # should I raise
            # ValueError or can I do some different

    def append(self, content):
        data = self.read()
        data.append(content)
        self.open_file('w')
        json.dump(data, self.file)

    def close(self):
        self.file.close()
        self.file = None


class TxtHandler(BaseHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def read(self):
        self.file = open(self.file_path, 'r')
        data = self.file.read()
        return data

    def append(self, content):
        file = open(self.file_path, 'a+')
        file.write(f'{content}\n')
        return self.file

    def close(self):
        self.file.close()
        self.file = None
