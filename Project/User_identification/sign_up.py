import json
from getters import get_email, get_password, get_confirm_password


def check_signup_data(email, user_data: list):
    for user in user_data:
        if user['email'] == email:
            return True
    return False


def add_to_json(email, password, database):
    new_user = {"email": email,
                "password": password
                }
    database.append(new_user)
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)


def signup_method():
    while True:
        if get_email() == 'exit' or get_password() == 'exit' or get_confirm_password == 'exit':
            break
        else:
            email = get_email()
            password = get_password()
            confirm_password = get_confirm_password

        if check_signup_data(email, user_data):
            print('Such email or username already exist.\nTry again')
            break

        if password == confirm_password:
            add_to_json(email, confirm_password, user_data)
            print('User add successfully!')
            break
        else:
            print('Signup error. Password does\'t match')
            break


user_data = json.load(open('user_data.json'))
