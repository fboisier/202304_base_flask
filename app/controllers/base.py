from flask import render_template, redirect, session

from app import app


@app.route('/')
def inicio():

    if 'usuario' in session:
        return render_template('inicio.html')
    else:
        return redirect('/login')