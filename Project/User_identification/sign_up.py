import json
from getters import get_email, get_password, get_confirm_password, load_user_data


def user_exists(email, users: list):
    return any(user['email'] == email for user in users)


def add_user_to_database(email, password, users):
    users.append({"email": email, "password": password})
    with open('user_data.json', 'w') as file:
        json.dump(users, file)


def signup_method():
    while True:
        email = get_email()
        if email.lower() == 'exit':
            break

        password = get_password()
        if password.lower() == 'exit':
            break

        if user_exists(email, users_base):
            print('Such email or username already exists. Try again')
        else:
            confirm_password = get_confirm_password()
            if confirm_password == password:
                add_user_to_database(email, password, users_base)
                print('User added successfully!')
                break
            else:
                print('Signup error')
                break


users_base = load_user_data()
