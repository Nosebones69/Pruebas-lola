from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/procesar_login', methods=['POST'])
def procesar_login():
    email = request.form['email']
    password = request.form['password']
    # más logicaa
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
