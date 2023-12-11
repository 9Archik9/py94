class BaseHandler:
    def read(self):
        raise NotImplementedError

    def append(self, content):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError
