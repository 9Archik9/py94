from base_clases import DataStorage


class DataStorageWrite(DataStorage):
    def connect(self):
        file = super().connect()
        return file

    def _create_storage(self):
        file = super()._create_storage()
        return file

    def append(self, content):
        file = self.connect()
        file.write(content)
        file.close()
        print('Content added')


data_storage_write = DataStorageWrite('example.json')
f = data_storage_write.connect()
data_storage_write.append("[Hello world!]\n")
data_storage_write.disconnect(f)
print(data_storage_write.file_path)
var = data_storage_write.content
print(f'\n{var}')
