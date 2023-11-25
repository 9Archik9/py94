def check_data(email, password, users):
    for user in users:
        if user.get('email') == email and user.get('password') == password:
            return user.get('email')
    return 'Login error'
