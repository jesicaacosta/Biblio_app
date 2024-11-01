import os #se utiliza para construir rutas de archivos de manera compatible con cualquier so, lo cual es útil al guardar imágenes en una ubicación específica del servidor.
from werkzeug.utils import secure_filename #toma el nombre de un archivo subido por el usuario y lo transforma en un nombre seguro,
from flask import Flask, render_template, request, redirect, url_for
from biblioteca import biblioteca, mostrar_libros, agregar_libro, actualizar_libro, eliminar_libro

app = Flask(__name__)

# Define la carpeta de subida para las imágenes
UPLOAD_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')


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


#----------- Funcion ELIMINAR
@app.route('/eliminar/<int:index>', methods=['POST'])
def eliminar(index): #eliminar es el manejador de la ruta que se invoca cuando un usuario quiere eliminar un libro, y se encarga de redirigir después de la eliminación.
    eliminar_libro(index) ## Llama a la fncion para realizar la eliminacion
    return redirect(url_for('index'))



#----------- FUNCION EDITAR 
@app.route('/editar/<int:index>', methods=['GET', 'POST'])
def editar_libro(index):
    if request.method == 'POST':
        libro_actualizado = {
            'titulo': request.form['titulo'],
            'autor': request.form['autor'],
            'estrellas': request.form['estrellas'],
            'comienzo_de_lectura': request.form['comienzo_de_lectura'],
            'fin_de_lectura': request.form['fin_de_lectura'],
            'descripcion': request.form['descripcion']
        }
        actualizar_datos_libro(index, libro_actualizado)  # Llamar a la función de actualización
        return redirect(url_for('index'))
    
    # Si es un GET, muestra el libro a editar
    libro_a_editar = biblioteca[index]
    return render_template('editar.html', libro=libro_a_editar, index=index)


def actualizar_datos_libro(index, libro_actualizado):
    # Aquí implementas la lógica para actualizar el libro en la biblioteca
    biblioteca[index] = libro_actualizado



if __name__ == '__main__':
    app.run(debug=True)
