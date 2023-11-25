from login import *


def app():
    user_choose = input('Select authorization option (write number): \n'
                        '1. Sign up\n'
                        '2. Login\n>')
    if user_choose == '2':
        login_method()


app()
