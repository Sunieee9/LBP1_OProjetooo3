from flask import Blueprint, render_template, request, redirect, url_for, make_response, flash, session
from models.livroM import Livrinhos, Livro

livro_controller = Blueprint('livro', __name__)

@livro_controller.route('/livro', methods=['GET', 'POST'])
def livro():
    if 'usuario_logado' not in session:
        flash("Você precisa estar logado para acessar a página de livros.")
        return redirect(url_for('login_controller.login_page'))

    if request.method == 'POST':
        id = request.form.get('id')  
        return add_to_cart(id)

    return render_template('livros.html', livros=Livrinhos)

def add_to_cart(id):
    resp = make_response(redirect(url_for('livro.ver'))) 
    cookie = request.cookies.get(f'produto_{id}')  
    if cookie:
        resp.set_cookie(f'produto_{id}', str(int(cookie) + 1), max_age=60*60*24)  
    else:
        resp.set_cookie(f'produto_{id}', "1", max_age=60*60*24) 
    
    return resp 

@livro_controller.route('/carrinho/del', methods=['POST'])
def delete():
    if 'usuario_logado' not in session:
        flash("Você precisa estar logado para acessar a página do carrinho.")
        return redirect(url_for('login_controller.login_page'))

    id = request.form.get('id')  
    resp = make_response(redirect(url_for('livro.ver')))  
    cookie = request.cookies.get(f'produto_{id}')  
    if cookie:
        if int(cookie) > 1:
            resp.set_cookie(f'produto_{id}', str(int(cookie) - 1), max_age=60*60*24)  
        else:
            resp.set_cookie(f'produto_{id}', '0', expires=0)   
    return resp

@livro_controller.route('/carrinho', methods=['GET'])
def ver():
    if 'usuario_logado' not in session:
        flash("Você precisa estar logado para acessar a página do carrinho.")
        return redirect(url_for('login_controller.login_page'))

    carrinho = [] 
    total = 0 
    for livro in Livrinhos:
        quantidade = int(request.cookies.get(f'produto_{livro.id}', 0)) 
        if quantidade > 0:
            subtotal = quantidade * livro.preco
            total += subtotal 
            carrinho.append({
                'nome': livro.titulo,
                'preco': livro.preco,
                'quantidade': quantidade,
                'subtotal': subtotal,
                'id': livro.id 
            })
    return render_template('carrinho.html', carrinho=carrinho, total=total)
