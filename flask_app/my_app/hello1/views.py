from my_app import app


@app.route('/')
@app.route('/interaccion')
def interaccion():
    return "interaccion Hola"