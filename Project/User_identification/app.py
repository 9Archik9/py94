from getters import get_email, get_password
from validators import check_data


def app(users):
    while True:
        email = get_email()
        if email.lower() == 'exit':
            print('Goodbye!')
            break

        password = get_password()
        if password.lower() == 'exit':
            print('Goodbye!')
            break

        result = check_data(email, password, users)
        if result != 'Login error':
            print(f'Welcome, {result}!')
            return result
        else:
            print(result)


users = [
        {'email': 'some@mail.ru', 'password': '123pass'},
        {'email': 'py94@gmail.com', 'password': 'py94'}
    ]

app(users)