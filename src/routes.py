from flask import Blueprint, render_template, jsonify
from src.models import db, User

# Define a new Blueprint for the API
main = Blueprint('api', __name__)

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/users', methods=['GET'])
def get_users():
    # Consulta todos los usuarios desde la base de datos
    users = User.query.all()

    # Convierte los usuarios a una lista de diccionarios
    # para que puedan ser serializados a JSON
    users_list = []
    for user in users:
        users_list.append({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })

    # Devuelve la lista en formato JSON
    return jsonify(users_list)

