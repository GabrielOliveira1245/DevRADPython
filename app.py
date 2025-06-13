from flask_login import login_required
from flask import Flask
from config import Config
from database.db import db
from flask_login import LoginManager
from models.usuario import Usuario
from routes.auth_routes import auth_bp
from routes.main_routes import main_bp

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa banco de dados
db.init_app(app)

# Login
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Registrar rotas (blueprints)
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

# Iniciar aplicação
if __name__ == "__main__":
    app.run(debug=True, port=5001)