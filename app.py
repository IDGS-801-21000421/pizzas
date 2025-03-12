from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

import forms

from models import *
from models import db

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()
app.config['SECRET_KEY'] = '12345'


@app.route('/', methods = ["GET", "POST"])
def index():

    create_form = forms.PedidoForm(request.form)
    pedidos = Pedido.query.all()
    pizza = Pizza.query.all()
        
    return render_template('index.html', form = create_form, pedidos = pedidos,pizza = pizza)

@app.route('/pedido', methods = ['GET', 'POST'])
def pedido():
    
    create_form=forms.PedidoForm(request.form)
    if request.method=='POST':
        pedido = Pedido(
            nombre = create_form.nombre.data,
            direccion = create_form.direccion.data,
            telefono = create_form.telefono.data,
            fecha = create_form.fecha.data,
            total = create_form.total.data
        )
        db.session.add(pedido)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form = create_form)
    

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()