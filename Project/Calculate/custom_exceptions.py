class NotANumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Error: '{self.value}' is not a number")

    def check_number(self):
        try:
            self.value
        except ValueError:
            raise NotANumberError(self.value)


class NotValidOperationError(Exception):
    def __init__(self, value):
        super().__init__(f"Error: unknown operation: '{value}'")
