from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
users = []


@app.route('/')
def index():
    global users
    users_url = 'http://185.225.232.111:8000/user/'
    response = requests.get(users_url)

    if response.status_code == 200:
        users = response.json()

        for user in users:
            user_id = user.get('id')
            user_info_url = f'http://185.225.232.111:8000/user/{user_id}'
            user_info_response = requests.get(user_info_url)

            if user_info_response.status_code == 200:
                user_info = user_info_response.json()
                user['age'] = user_info.get('age')

        return render_template('index.html', users=users)
    else:
        return 'Data retrieval error'


@app.route('/drop_all', methods=['GET', 'POST'])
def drop_all():
    global users
    if request.method == 'POST':
        users = []

        return redirect(url_for('index'))
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
