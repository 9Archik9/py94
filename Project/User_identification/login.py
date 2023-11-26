import json
from getters import get_email, get_password


def check_login_data(email, password, database):
    for user in database:
        if user.get('email') == email and user.get('password') == password:
            return user.get('email')
    return 'Login error'


def login_method():
    while True:

        email = get_email()
        if email.lower() == 'exit':
            break
        password = get_password()
        if password.lower() == 'exit':
            break

        result = check_login_data(email, password, users)
        if result != 'Login error':
            print(f'Welcome, {result}!')
            return result
        else:
            print(result)


with open('user_data.json', 'r') as json_file:
    users = json.load(json_file)
