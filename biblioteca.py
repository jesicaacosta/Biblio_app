# Lista para almacenar los libros
biblioteca = []

# Función para mostrar todos los libros
def mostrar_libros():
    if not biblioteca:
        print("No hay libros en la biblioteca.")
    else:
        print("Libros en la biblioteca:")
        for idx, libro in enumerate(biblioteca, start=1):
            print(f"{idx}. Título: {libro['titulo']}, {libro['autor']}, {libro['estrellas']}, "
                  f"{libro['comienzo_de_lectura']}, {libro['fin_de_lectura']}, Descripción: {libro['descripcion']}")

# Función para agregar un libro
def agregar_libro(libro):
    biblioteca.append(libro)

# Función para actualizar un libro
def actualizar_libro(index, nuevo_libro):
    if 0 <= index < len(biblioteca):
        biblioteca[index] = nuevo_libro

# Función para eliminar un libro
def eliminar_libro(index):
    if 0 <= index < len(biblioteca):
        biblioteca.pop(index)
