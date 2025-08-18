from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.models import db, User

def setup_admin(app):
	admin = Admin(app, name='Rebusque2025', template_mode='bootstrap3')
	admin.add_view(ModelView(User, db.session))
	return admin
