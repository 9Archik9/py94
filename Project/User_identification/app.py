from login import *
from sign_up import *


def app():
    while True:
        user_choose = input('Select authorization option (write number): \n'
                            '1. Sign up\n'
                            '2. Login\n'
                            '3. Exit\n>')

        if user_choose == '1':
            signup_method()
            break
        elif user_choose == '2':
            login_method()
            break
        elif user_choose == '3':
            print('Goodbye')
            break
        else:
            print('No such option')


app()
