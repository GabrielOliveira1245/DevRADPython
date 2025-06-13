from database.db import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"
    
    id = db.Column(db.Integer, primary_key=True)
    tipoUsuario = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    mudaSenha = db.Column(db.Boolean, default=False)
    liberacao = db.Column(db.Boolean, default=True)

    # RELACIONAMENTO: Liga o usuário ao seu perfil
    # O cascade garante que, se um usuário for deletado, seu perfil também será.
    perfil = db.relationship('Perfil', backref='usuario', uselist=False, cascade="all, delete-orphan")