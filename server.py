from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/login')
def login():

    if 'usuario' in session:
        return redirect('/')
        

    return render_template('login.html')

@app.route('/procesar_login', methods=['POST'])
def procesar_login():
    print("POST: ", request.form)
    if request.form['email'] == 'fboisier@codingdojo.cl' and request.form['password'] == '123456':
        session['usuario'] = request.form['email']
        flash('Genial, pudiste entrar sin problemas!!!!', 'success')

    else:
        flash('Existe un error en tu correo o contraseña', 'danger')
        return redirect('/login')

    return redirect('/')

@app.route('/')
def inicio():

    if 'usuario' in session:
        return render_template('inicio.html')
    else:
        return redirect('/login')
    
@app.route('/salir')
def salir():
    session.clear()
    flash('Saliste sin problemas!!!', 'info')
    return redirect('/login')


if __name__=="__main__":
    app.run(debug=True)   