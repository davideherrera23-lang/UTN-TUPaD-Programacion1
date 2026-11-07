import requests

URL_BASE = "http://127.0.0.1:5000/api"


def mostrar(titulo, respuesta):
    print("-----", titulo, "-----")
    print("Código:", respuesta.status_code)
    print("Respuesta:", respuesta.json())
    print()


def main():
    try:
        respuesta = requests.get(URL_BASE + "/libros")
        mostrar("GET /api/libros", respuesta)

        respuesta = requests.post(
            URL_BASE + "/autores",
            json={"nombre": "Julio Cortázar", "nacionalidad": "Argentina"},
        )
        mostrar("POST /api/autores", respuesta)
        autor_id = respuesta.json()["id"]

        respuesta = requests.post(
            URL_BASE + "/libros",
            json={"titulo": "Rayuela", "anio": 1963, "autor_id": autor_id},
        )
        mostrar("POST /api/libros", respuesta)
        libro_id = respuesta.json()["id"]

        respuesta = requests.put(
            URL_BASE + "/libros/" + str(libro_id),
            json={"titulo": "Rayuela (Edición Revisada)"},
        )
        mostrar("PUT /api/libros/" + str(libro_id), respuesta)

        respuesta = requests.delete(URL_BASE + "/libros/" + str(libro_id))
        mostrar("DELETE /api/libros/" + str(libro_id), respuesta)

        respuesta = requests.get(URL_BASE + "/libros/" + str(libro_id))
        mostrar("GET /api/libros/" + str(libro_id) + " (verificación)", respuesta)
        if respuesta.status_code == 404:
            print("Verificado: el libro fue eliminado correctamente")
    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con la API. Ejecute primero: python app.py")


if __name__ == "__main__":
    main()
