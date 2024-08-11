from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/enviar_contacto', methods=['POST'])
def enviar_contacto():
    email = request.form['email']
    mensaje = request.form['mensaje']

    # más base de datos
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
