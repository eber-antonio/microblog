from app import app
from flask import render_template

#decorador (agrega funcionalidad a una funcion sin modificarla)
@app.route('/') #crea una asociacion entre el url dado y la funcion
@app.route('/index')
def index():
    user = {'username': 'Eber'}
    posts = [
        {
            'author':{'username':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'username':'Susan'},
            'body':'The Avenger movie was so cool!'
        }
    ]

    return render_template('index.html', user=user, posts=posts)