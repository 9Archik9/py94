import json


def get_email():
    return input('Write your email or username: ')


def get_password():
    return input('Write your password: ')


def get_confirm_password():
    return input('Confirm your password: ')


def load_user_data():
    return json.load(open('user_data.json'))
