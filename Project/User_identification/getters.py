def exit_on_keyword(func):
    def wrapper():
        while True:
            value = func()
            if value.lower() == 'exit':
                print('Goodbye!')
                return 'exit'
            else:
                return value

    return wrapper


@exit_on_keyword
def get_email():
    return input('Write your email or username: ')


@exit_on_keyword
def get_password():
    return input('Write your password: ')


@exit_on_keyword
def get_confirm_password():
    return input('Confirm your password')
