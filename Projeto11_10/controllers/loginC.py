from flask import Blueprint, render_template

login_controller = Blueprint('login', __name__)

@login_controller.route('/login', methods=['post', 'get'])
def login():
    return render_template('login.html')