from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

# Inicializamos la extensión de SQLAlchemy
db = SQLAlchemy()

# Creamos la clase del modelo
class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'