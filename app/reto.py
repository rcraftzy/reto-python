from flask import (
    Blueprint, render_template, request, flash, url_for, redirect
)
import requests

from random import randint

from app.db import get_db

bp = Blueprint('reto', __name__, url_prefix="/")


@bp.route('/', methods=['GET'])
def index():
    n=randint(1,2)

    if n == 1:
        response = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
        gender = response.json()
    if n == 2:
        response = requests.get('https://api.chucknorris.io/jokes/random')
        gender = response.json()
    print(n)
    print(gender)

    return render_template('reto/index.html', gender=gender)

@bp.route('/chuck', methods=['GET', 'POST'])
def chuck():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    gender = response.json()
    print(gender['value'])

    if request.method == 'POST':
        value = request.form.get('value')
        errors = []

        if not value:
            errors.append('No se encuentra el chiste')

        if len(errors) == 0:
            db, c = get_db()
            c.execute("INSERT INTO joke(value) VALUES (%s)", (value,))
            db.commit()

            return redirect(url_for('reto.index'))
        else:
            for error in errors:
                flash(error)

    return render_template('reto/index.html', gender=gender)

@bp.route('/dad', methods=['GET'])
def dad():
    response = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
    gender = response.json()
    print(gender)

    return render_template('reto/index.html', gender=gender)

@bp.route('/guardar', methods=['GET', 'POST'])
def guardar():
    return render_template('reto/index.html')

@bp.route('/guardado', methods=['GET'])
def guardado():
    db, c = get_db()

    c.execute("SELECT * FROM joke")
    jokes = c.fetchall()

    return render_template('reto/guardado.html', jokes=jokes)
