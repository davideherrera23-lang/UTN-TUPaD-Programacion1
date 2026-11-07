from celda import Celda
from matriz import Matriz


def leerEntero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero")


class ProgramaMatriz:
    @staticmethod
    def main():
        matriz = Matriz()
        while True:
            valor = input("Ingrese el valor de la celda (FIN para terminar): ")
            if valor == "FIN":
                break
            fila = leerEntero("Ingrese la fila: ")
            columna = leerEntero("Ingrese la columna: ")
            celda = Celda(fila, columna, valor)
            if matriz.agregarCelda(celda):
                print("Celda cargada correctamente")
            else:
                print("La fila y columna indicadas ya fueron cargadas anteriormente")

        matriz.mostrarCeldas()

        print("----------- CONSULTA DE CELDA -----------")
        fila = leerEntero("Ingrese la fila a consultar: ")
        columna = leerEntero("Ingrese la columna a consultar: ")
        print(matriz.obtenerValor(fila, columna))


if __name__ == "__main__":
    ProgramaMatriz.main()
