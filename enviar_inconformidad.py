from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/enviar_inconformidad', methods=['POST'])
def enviar_inconformidad():
    nombre = request.form.get('nombre', '')
    fecha = request.form['fecha']
    hora = request.form['hora']
    descripcion = request.form['descripcion']
    calificacion = request.form['calificacion']
    foto = request.files.get('foto')

    # ahí va la puta base de datos
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
