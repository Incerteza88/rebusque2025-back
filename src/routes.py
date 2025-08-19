from flask import Blueprint, render_template, jsonify, url_for
import os
from src.models import db, User

# Define a new Blueprint for the API
main = Blueprint('api', __name__)

@main.route('/')
def index():
    # Obtiene la URL base de tu archivo .env
    base_url = os.getenv('BASE_URL')
    
    # Usa url_for para generar la URL del admin
    admin_url = url_for('admin.index')
    
    # Combina la URL base con la URL del admin
    # Esto es opcional si solo necesitas la URL generada por url_for
    full_admin_url = f"{base_url}{admin_url}" if base_url else admin_url
    
    # Renderiza la plantilla, pasando la URL del admin
    return render_template('index.html', admin_url=full_admin_url)

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

