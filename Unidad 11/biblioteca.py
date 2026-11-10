import os
import sqlite3

NOMBRE_DB = "biblioteca.db"

class Autor:
    """Representa a un autor de libros."""

    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor #{self.id_autor}: {self.nombre} ({self.nacionalidad})"

class Libro:
    """Representa un libro. Tiene un Autor (agregación)."""

    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor

    def __str__(self):
        return (f"Libro #{self.id_libro}: '{self.titulo}' "
                f"({self.anio_publicacion}) - de {self.autor.nombre}")

def conectar():
    """Abre una conexión a la base y activa las claves foráneas.
    (SQLite las trae desactivadas por defecto, por eso el PRAGMA)."""
    conexion = sqlite3.connect(NOMBRE_DB)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

def inicializar_bd():
    """Crea las tablas autores y libros si todavía no existen."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS autores (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre       TEXT NOT NULL,
                nacionalidad TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo   TEXT NOT NULL,
                anio     INTEGER,
                autor_id INTEGER NOT NULL,
                FOREIGN KEY (autor_id) REFERENCES autores(id)
            )
        """)
        conexion.commit()
    finally:
        conexion.close()

def registrar_autor(nombre, nacionalidad):
    """Inserta un autor y devuelve el ID que le asignó la base."""
    if not nombre or not str(nombre).strip():
        raise ValueError("El nombre del autor no puede estar vacío.")

    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
            (nombre.strip(), nacionalidad),
        )
        conexion.commit()
        return cursor.lastrowid
    finally:
        conexion.close()

def registrar_libro(titulo, anio, autor_id):
    """Inserta un libro vinculado a un autor y devuelve su ID."""
    if not titulo or not str(titulo).strip():
        raise ValueError("El título del libro no puede estar vacío.")

    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
                (titulo.strip(), anio, autor_id),
            )
        except sqlite3.IntegrityError:
            raise ValueError(f"No existe un autor con id {autor_id}.")
        conexion.commit()
        return cursor.lastrowid
    finally:
        conexion.close()

def listar_libros():
    """SELECT con JOIN: devuelve (titulo, anio, nombre_autor) de cada libro."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT libros.id, libros.titulo, libros.anio, autores.nombre
            FROM libros
            JOIN autores ON libros.autor_id = autores.id
            ORDER BY libros.id
        """)
        return cursor.fetchall()
    finally:
        conexion.close()

def actualizar_titulo_libro(id_libro, nuevo_titulo):
    """UPDATE del título. Devuelve True si se modificó, False si no existe."""
    if not nuevo_titulo or not str(nuevo_titulo).strip():
        raise ValueError("El nuevo título no puede estar vacío.")

    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE libros SET titulo = ? WHERE id = ?",
            (nuevo_titulo.strip(), id_libro),
        )
        conexion.commit()
        return cursor.rowcount > 0
    finally:
        conexion.close()

def eliminar_libro(id_libro):
    """DELETE por ID. Devuelve True si se eliminó, False si no existe."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
        conexion.commit()
        return cursor.rowcount > 0
    finally:
        conexion.close()

def mostrar_libros():
    libros = listar_libros()
    if not libros:
        print("(No hay libros registrados)")
        return
    for id_libro, titulo, anio, nombre_autor in libros:
        print(f"[{id_libro}] {titulo} | Año: {anio} | Autor: {nombre_autor}")

if __name__ == "__main__":
    try:
        if os.path.exists(NOMBRE_DB):
            os.remove(NOMBRE_DB)

        print("1) Inicializando la base de datos...")
        inicializar_bd()
        print("Base de datos creada correctamente.\n")

        print("2) Registrando autores y libros...")
        id_borges = registrar_autor("Jorge Luis Borges", "Argentina")
        id_garcia = registrar_autor("Gabriel García Márquez", "Colombiana")
        print(f"Autor registrado con ID {id_borges}")
        print(f"Autor registrado con ID {id_garcia}")

        id_l1 = registrar_libro("El Aleph", 1949, id_borges)
        id_l2 = registrar_libro("Ficciones", 1944, id_borges)
        id_l3 = registrar_libro("Cien años de soledad", 1967, id_garcia)
        print(f"   Libros registrados con IDs {id_l1}, {id_l2} y {id_l3}\n")

        autor_obj = Autor(id_borges, "Jorge Luis Borges", "Argentina")
        libro_obj = Libro(id_l1, "El Aleph", 1949, autor_obj)
        print("Demostración de las clases:")
        print("", autor_obj)
        print("", libro_obj)

        print("3) Listado de libros registrados:")
        mostrar_libros()
        print()

        print("4) Actualizando el título del libro 2...")
        if actualizar_titulo_libro(id_l2, "Ficciones (Edición revisada)"):
            print("Título actualizado. Listado para verificar:")
            mostrar_libros()
        else:
            print("No se encontró el libro a actualizar.")
        print()

        print("5) Eliminando el libro 3...")
        if eliminar_libro(id_l3):
            print("Libro eliminado. Listado resultante:")
            mostrar_libros()
        else:
            print("No se encontró el libro a eliminar.")

        print("Extra) Probando manejo de errores:")
        print("Eliminar libro inexistente ->", eliminar_libro(999))
        try:
            registrar_libro("Libro huérfano", 2000, 999)
        except ValueError as error:
            print("Libro con autor inexistente ->", error)

    except sqlite3.Error as error:
        print("Error de base de datos:", error)
    except ValueError as error:
        print("Error de validación:", error)