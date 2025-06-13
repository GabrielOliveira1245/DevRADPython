# Importa o app e o db do seu aplicativo principal
from app import app, db

# Cria um contexto de aplicação para interagir com o banco de dados
with app.app_context():
    print("Criando tabelas do banco de dados...")
    db.create_all()
    print("Tabelas criadas com sucesso!")