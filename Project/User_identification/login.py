import json
from getters import get_email, get_password


def check_login_data(email, password, users):
    for user in users:
        if user.get('email') == email and user.get('password') == password:
            return user.get('email')
    return 'Login error'


def login_method():
    while True:
        if get_email() == 'exit' or get_password() == 'exit':
            break
        else:
            email = get_email()
            password = get_password()

        result = check_login_data(email, password, users)
        if result != 'Login error':
            print(f'Welcome, {result}!')
            return result
        else:
            print(result)


with open('user_data.json', 'r') as json_file:
    users = json.load(json_file)
