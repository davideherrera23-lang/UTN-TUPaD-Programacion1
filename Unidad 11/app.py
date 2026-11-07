from flask import Flask, jsonify, request

from repositorio import (
    crear_tablas,
    obtener_autores_db,
    obtener_autor_db,
    insertar_autor_db,
    obtener_libros_db,
    obtener_libro_db,
    insertar_libro_db,
    actualizar_libro_db,
    eliminar_libro_db,
)

app = Flask(__name__)
crear_tablas()


def error(mensaje, codigo):
    return jsonify({"error": mensaje}), codigo


def es_entero(valor):
    return isinstance(valor, int) and not isinstance(valor, bool)


@app.route("/api/autores", methods=["GET"])
def listar_autores():
    return jsonify(obtener_autores_db()), 200


@app.route("/api/autores", methods=["POST"])
def crear_autor():
    datos = request.get_json(silent=True)
    if not datos or "nombre" not in datos or "nacionalidad" not in datos:
        return error("Los campos 'nombre' y 'nacionalidad' son obligatorios", 400)
    if not isinstance(datos["nombre"], str) or not isinstance(datos["nacionalidad"], str):
        return error("Los campos 'nombre' y 'nacionalidad' deben ser cadenas", 400)
    if datos["nombre"].strip() == "" or datos["nacionalidad"].strip() == "":
        return error("Los campos 'nombre' y 'nacionalidad' no pueden estar vacíos", 400)

    nuevo_id = insertar_autor_db(datos["nombre"], datos["nacionalidad"])
    return jsonify(obtener_autor_db(nuevo_id)), 201


@app.route("/api/libros", methods=["GET"])
def listar_libros():
    return jsonify(obtener_libros_db()), 200


@app.route("/api/libros/<int:id>", methods=["GET"])
def obtener_libro(id):
    libro = obtener_libro_db(id)
    if libro is None:
        return error("No existe un libro con id " + str(id), 404)
    return jsonify(libro), 200


@app.route("/api/libros", methods=["POST"])
def crear_libro():
    datos = request.get_json(silent=True)
    if not datos or "titulo" not in datos or "anio" not in datos or "autor_id" not in datos:
        return error("Los campos 'titulo', 'anio' y 'autor_id' son obligatorios", 400)
    if not isinstance(datos["titulo"], str) or datos["titulo"].strip() == "":
        return error("El campo 'titulo' debe ser una cadena no vacía", 400)
    if not es_entero(datos["anio"]) or not es_entero(datos["autor_id"]):
        return error("Los campos 'anio' y 'autor_id' deben ser enteros", 400)
    if obtener_autor_db(datos["autor_id"]) is None:
        return error("No existe un autor con id " + str(datos["autor_id"]), 404)

    nuevo_id = insertar_libro_db(datos["titulo"], datos["anio"], datos["autor_id"])
    return jsonify(obtener_libro_db(nuevo_id)), 201


@app.route("/api/libros/<int:id>", methods=["PUT"])
def actualizar_libro(id):
    libro = obtener_libro_db(id)
    if libro is None:
        return error("No existe un libro con id " + str(id), 404)

    datos = request.get_json(silent=True)
    if not datos or not ("titulo" in datos or "anio" in datos or "autor_id" in datos):
        return error("Debe enviar al menos uno de los campos 'titulo', 'anio' o 'autor_id'", 400)

    titulo = datos.get("titulo", libro["titulo"])
    anio = datos.get("anio", libro["anio"])
    autor_id = datos.get("autor_id", libro["autor_id"])

    if not isinstance(titulo, str) or titulo.strip() == "":
        return error("El campo 'titulo' debe ser una cadena no vacía", 400)
    if not es_entero(anio) or not es_entero(autor_id):
        return error("Los campos 'anio' y 'autor_id' deben ser enteros", 400)
    if obtener_autor_db(autor_id) is None:
        return error("No existe un autor con id " + str(autor_id), 404)

    actualizar_libro_db(id, titulo, anio, autor_id)
    return jsonify(obtener_libro_db(id)), 200


@app.route("/api/libros/<int:id>", methods=["DELETE"])
def eliminar_libro(id):
    if obtener_libro_db(id) is None:
        return error("No existe un libro con id " + str(id), 404)
    eliminar_libro_db(id)
    return jsonify({"mensaje": "El libro con id " + str(id) + " fue eliminado correctamente"}), 200


if __name__ == "__main__":
    app.run(debug=True)
