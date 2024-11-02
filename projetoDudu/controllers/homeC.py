from flask import Blueprint, render_template, request, redirect, url_for, session, flash

home_controller = Blueprint('home', __name__)

@home_controller.route('/', methods=['POST', 'GET'])
def home():
    usuario_logado = session.get('usuario_logado')
    return render_template('home.html', usuario=usuario_logado)

@home_controller.before_request
def autenticar_usuario():
    rota_protegida = request.endpoint in ['home.admin_page', 'home.user_page']  
    if rota_protegida and 'usuario_logado' not in session:
        return redirect(url_for('login_controller.login_page'))  

