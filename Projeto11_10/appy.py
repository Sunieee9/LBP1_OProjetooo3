from flask import Flask
from controllers.livroC import hello_controller
from controllers.loginC import login_controller

app = Flask(__name__)
app.register_blueprint(hello_controller)
app.register_blueprint(login_controller)

if __name__ == '__main__':
    app.run(debug=True)