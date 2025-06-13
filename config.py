import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    # Carrega a chave do ambiente ou usa uma padrão (NÃO USE EM PRODUÇÃO)
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-in-production")
    
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASEDIR, "database", "conversor.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False