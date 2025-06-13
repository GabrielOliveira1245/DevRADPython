from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models.usuario import Usuario
from models.perfil import Perfil  # Importa o modelo Perfil
from database.db import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and check_password_hash(usuario.senha, senha):
            login_user(usuario)
            return redirect(url_for("main.dashboard"))
        
        flash("E-mail ou senha inválidos.", "danger") # Categoria 'danger' para estilização
    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        
        # Verifica se o email já existe
        if Usuario.query.filter_by(email=email).first():
            flash("Este e-mail já está em uso.", "warning")
            return redirect(url_for('auth.register'))

        hash_senha = generate_password_hash(senha)
        novo_usuario = Usuario(email=email, senha=hash_senha)

        # Cria um perfil vazio para o novo usuário
        novo_perfil = Perfil()
        novo_usuario.perfil = novo_perfil # Associa o perfil ao usuário
        
        db.session.add(novo_usuario)
        db.session.commit()
        
        flash("Cadastro realizado com sucesso! Faça o login.", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você foi desconectado.", "info")
    return redirect(url_for("auth.login"))