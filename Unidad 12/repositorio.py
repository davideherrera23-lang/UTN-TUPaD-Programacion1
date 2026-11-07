import sqlite3

NOMBRE_DB = "biblioteca.db"


def conectar():
    conexion = sqlite3.connect(NOMBRE_DB)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def crear_tablas():
    conexion = conectar()
    try:
        conexion.execute(
            "CREATE TABLE IF NOT EXISTS autores ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "nombre TEXT NOT NULL, "
            "nacionalidad TEXT NOT NULL)"
        )
        conexion.execute(
            "CREATE TABLE IF NOT EXISTS libros ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "titulo TEXT NOT NULL, "
            "anio INTEGER NOT NULL, "
            "autor_id INTEGER NOT NULL, "
            "FOREIGN KEY (autor_id) REFERENCES autores(id))"
        )
        conexion.commit()
    finally:
        conexion.close()


def obtener_autores_db():
    conexion = conectar()
    try:
        filas = conexion.execute("SELECT id, nombre, nacionalidad FROM autores").fetchall()
        return [dict(fila) for fila in filas]
    finally:
        conexion.close()


def obtener_autor_db(id):
    conexion = conectar()
    try:
        fila = conexion.execute(
            "SELECT id, nombre, nacionalidad FROM autores WHERE id = ?", (id,)
        ).fetchone()
        if fila is None:
            return None
        return dict(fila)
    finally:
        conexion.close()


def insertar_autor_db(nombre, nacionalidad):
    conexion = conectar()
    try:
        cursor = conexion.execute(
            "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)", (nombre, nacionalidad)
        )
        conexion.commit()
        return cursor.lastrowid
    finally:
        conexion.close()


def obtener_libros_db():
    conexion = conectar()
    try:
        filas = conexion.execute(
            "SELECT libros.id, libros.titulo, libros.anio, libros.autor_id, "
            "autores.nombre AS autor_nombre, autores.nacionalidad AS autor_nacionalidad "
            "FROM libros INNER JOIN autores ON libros.autor_id = autores.id"
        ).fetchall()
        return [dict(fila) for fila in filas]
    finally:
        conexion.close()


def obtener_libro_db(id):
    conexion = conectar()
    try:
        fila = conexion.execute(
            "SELECT libros.id, libros.titulo, libros.anio, libros.autor_id, "
            "autores.nombre AS autor_nombre, autores.nacionalidad AS autor_nacionalidad "
            "FROM libros INNER JOIN autores ON libros.autor_id = autores.id "
            "WHERE libros.id = ?",
            (id,),
        ).fetchone()
        if fila is None:
            return None
        return dict(fila)
    finally:
        conexion.close()


def insertar_libro_db(titulo, anio, autor_id):
    conexion = conectar()
    try:
        cursor = conexion.execute(
            "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
            (titulo, anio, autor_id),
        )
        conexion.commit()
        return cursor.lastrowid
    finally:
        conexion.close()


def actualizar_libro_db(id, titulo, anio, autor_id):
    conexion = conectar()
    try:
        conexion.execute(
            "UPDATE libros SET titulo = ?, anio = ?, autor_id = ? WHERE id = ?",
            (titulo, anio, autor_id, id),
        )
        conexion.commit()
    finally:
        conexion.close()


def eliminar_libro_db(id):
    conexion = conectar()
    try:
        conexion.execute("DELETE FROM libros WHERE id = ?", (id,))
        conexion.commit()
    finally:
        conexion.close()
