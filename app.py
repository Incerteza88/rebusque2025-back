import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from src.models import db
from src.routes import main # Importa el Blueprint 'main'
from src.admin import setup_admin
from flask_migrate import Migrate

# Crea la instancia de la aplicación Flask
app = Flask(__name__, template_folder='src/templates')

# Configuración de la aplicación
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///rebusque2025.db"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Inicializa las extensiones con la aplicación
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# Registra los Blueprints
app.register_blueprint(main)
setup_admin(app)

if __name__ == '__main__':
    with app.app_context():
        # Crea todas las tablas si no existen.
        # Esto es solo para la primera vez, se recomienda usar Flask-Migrate
        db.create_all()
    
    # Inicia el servidor
    app.run(debug=True)