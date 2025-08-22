from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.models import db, User, Category, Service, Contract, Review
def setup_admin(app):
    admin = Admin(app, name='Rebusque2025', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Service, db.session))
    admin.add_view(ModelView(Contract, db.session))
    admin.add_view(ModelView(Review, db.session))
    return admin







