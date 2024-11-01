from flask import Flask, render_template, request, redirect, url_for
from biblioteca import biblioteca, mostrar_libros, agregar_libro, actualizar_libro, eliminar_libro

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', biblioteca=biblioteca)

@app.route('/agregar', methods=['POST'])
def agregar():
    libro = {
        'titulo': request.form['titulo'],
        'autor': request.form['autor'],
        'estrellas': request.form['estrellas'],
        'comienzo_de_lectura': request.form['comienzo_de_lectura'],
        'fin_de_lectura': request.form['fin_de_lectura'],
        'descripcion': request.form['descripcion']
    }
    agregar_libro(libro)
    return redirect(url_for('index'))

@app.route('/eliminar/<int:index>', methods=['POST'])
def eliminar(index):
    eliminar_libro(index)
    return redirect(url_for('index'))

@app.route('/editar/<int:index>', methods=['GET', 'POST'])
def editar(index):
    if request.method == 'POST':
        libro_actualizado = {
            'titulo': request.form['titulo'],
            'autor': request.form['autor'],
            'estrellas': request.form['estrellas'],
            'comienzo_de_lectura': request.form['comienzo_de_lectura'],
            'fin_de_lectura': request.form['fin_de_lectura'],
            'descripcion': request.form['descripcion']
        }
        actualizar_libro(index, libro_actualizado)
        return redirect(url_for('index'))
    
    # Si es un GET, muestra el libro a editar
    libro_a_editar = biblioteca[index]
    return render_template('editar.html', libro=libro_a_editar, index=index)

if __name__ == '__main__':
    app.run(debug=True)
