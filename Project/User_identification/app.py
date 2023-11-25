from login import *
from sign_up import *


def app():
    user_choose = input('Select authorization option (write number): \n'
                        '1. Sign up\n'
                        '2. Login\n>')

    if user_choose == '1':
        signup_method()
    elif user_choose == '2':
        login_method()
    else:
        print('No such option')


app()
