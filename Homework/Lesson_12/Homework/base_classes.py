class Moving:
    def move(self):
        raise NotImplementedError("Method move could be implement in child class")


class Animal(Moving):
    def voice(self):
        raise NotImplementedError("Method voice could be implement in child class")


class Transport(Moving):
    def launch(self):
        raise NotImplementedError("Method launch could be implement in child class")
