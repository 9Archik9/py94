import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример хранилища объектов (может быть заменено на базу данных или другое хранилище)
objects = []


@app.route('/create_object', methods=['POST'])
def create_object():
    data = request.json
    if not data or not isinstance(data, list) or len(data) == 0:
        return jsonify({'error': 'Invalid JSON data or empty array'}), 400

    for obj in data:
        if 'name' in obj and 'type' in obj:
            new_object = {
                'name': obj['name'],
                'type': obj['type']
                # Добавьте другие свойства объекта здесь
            }
            objects.append(new_object)
        else:
            return jsonify({'error': 'Invalid object format'}), 400

    return jsonify({'message': 'Objects created successfully'}), 201


@app.route('/get_objects', methods=['GET'])
def get_objects():
    return jsonify(objects)


# POST запрос для создания объекта
url_create = 'http://127.0.0.1:5000/create_object'
data = [
    {
        'name': 'Object 1',
        'type': 'Type A'
    },
    {
        'name': 'Object 2',
        'type': 'Type B'
    }
]

response = requests.post(url_create, json=data)
print(response.json())  # Ответ от сервера

# GET запрос для получения объектов
url_get = 'http://127.0.0.1:5000/get_objects'
response = requests.get(url_get)
print(response.json())  # Ответ от сервера

if __name__ == '__main__':
    app.run()
