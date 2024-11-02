from flask import Flask,render_template
from controllers.loginC import login_controller
from controllers.homeC import home_controller
from controllers.livroC import livro_controller

app = Flask(__name__)
app.secret_key = 'US'

app.register_blueprint(login_controller)
app.register_blueprint(home_controller)
app.register_blueprint(livro_controller)

@app.errorhandler(401)
def acesso_negado(error):
    return render_template('401.html'), 401

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)