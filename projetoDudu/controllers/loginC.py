from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash
from models.homeM import User

admin_user = User("admin", "senhaforte", "admin")  
user1 = User("user1", "1234", "user")              
user_list = [admin_user, user1]

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        for user in user_list:
            if user.validate(username, password):
                session['usuario_logado'] = user.username
                session['role'] = user.role  
                flash(f'{user.username} logado com sucesso!')
                
                if user.role == 'admin':
                    return redirect(url_for('login_controller.admin_page'))
                else:
                    return redirect(url_for('login_controller.user_page'))
        
        flash('Usuário ou senha incorretos.')
        return redirect(url_for('login_controller.login_page'))
    
    return render_template('login.html')

@login_controller.route('/admin')
def admin_page():
    if 'usuario_logado' not in session or session.get('role') != 'admin':
        flash("Você precisa estar logado como administrador para acessar essa página.")
        return redirect(url_for('login_controller.login_page'))
    return render_template('admin.html')

@login_controller.route('/user')
def user_page():
    if 'usuario_logado' not in session:
        flash("Você precisa estar logado para acessar essa página.")
        return redirect(url_for('login_controller.login_page'))
    return render_template('user.html')

@login_controller.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    session.pop('role', None)
    flash("Você foi deslogado com sucesso.")
    return redirect(url_for('home.home'))
