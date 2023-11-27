import custom_exceptions


def input_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            custom_exceptions.NotANumberError(user_input).check_number()
            return float(user_input)
        except custom_exceptions.NotANumberError as e:
            print(f'{e}')


def calculation():
    operations = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: x ** y
    }

    while True:
        print('Select operation. +, -, *, /, **: ')
        choice = input("Enter operation symbol: ")

        if choice in operations:
            a = input_number('Enter first number: ')
            b = input_number('Enter second number: ')

            try:
                result = operations[choice](a, b)
                print(f'Result: {result}')
                break
            except ZeroDivisionError:
                print('Division by zero is not allowed')
        else:
            try:
                raise custom_exceptions.NotValidOperationError(choice)
            except custom_exceptions.NotValidOperationError as err:
                print(f'{err}')


calculation()
