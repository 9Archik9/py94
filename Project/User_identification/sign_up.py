import json
from getters import get_email, get_password, get_confirm_password


def check_signup_data(email, database: list):
    for user in database:
        if user['email'] == email:
            return True
    return False


def add_to_json(email, password):
    database = json.load(open('user_data.json'))
    new_user = {"email": email,
                "password": password
                }
    database.append(new_user)
    with open('user_data.json', 'w') as file:
        json.dump(database, file)


def signup_method():
    while True:
        email = get_email()
        if email.lower() == 'exit':
            break

        password = get_password()
        if password.lower() == 'exit':
            break

        if check_signup_data(email, users_base):
            print('Such email or username already exist.\nTry again')
        elif not check_signup_data(email, users_base):
            if get_confirm_password() == password:
                add_to_json(email, password)
                print('User add successfully!')
                break
            else:
                print('Signup error')
                break


users_base = json.load(open('user_data.json'))
