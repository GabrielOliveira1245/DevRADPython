from database.db import db

class Perfil(db.Model):
    __tablename__ = "perfil"
    
    id = db.Column(db.Integer, primary_key=True)
    # Garante que o ID do usuário não pode ser nulo, forçando a ligação
    userID = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    
    # Adicionado valores padrão para evitar erros se estiverem vazios
    nome = db.Column(db.String(50), default='')
    contato = db.Column(db.String(11), default='')
    foto = db.Column(db.String)