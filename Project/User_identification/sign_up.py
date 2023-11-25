import json
from getters import get_email, get_password


def add_to_json(email, password):
    user_data = json.load(open('user_data.json'))
    new_user = {"email": email,
                "password": password
                }
    user_data.append(new_user)
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)


def signup_method():
    while True:
        email = get_email()
        if email.lower() == 'exit':
            print('Goodbye!')
            break

        password = get_password()
        confirm_password = input('Confirm your password: ')
        if (password.lower() or confirm_password) == 'exit':
            print('Goodbye!')
            break

        if password == confirm_password:
            add_to_json(email, confirm_password)
            print('User add successfully!')
            break
        else:
            print('Signup error. Password does\'t match')
            break
