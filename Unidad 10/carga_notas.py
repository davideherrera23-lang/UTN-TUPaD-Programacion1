from alumno import Alumno
from nota import Nota


def leerEntero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero")


def leerDecimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debe ingresar un número decimal")


def leerSiNo(mensaje):
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta == "SI" or respuesta == "NO":
            return respuesta
        print("Responda SI o NO")


class CargaNotas:
    @staticmethod
    def main():
        alumnos = []
        salirAlumno = "NO"
        while salirAlumno == "NO":
            print("INGRESE DATOS DEL ALUMNO")
            nombreCompleto = input("INGRESE NOMBRE COMPLETO: ")
            legajo = leerEntero("INGRESE LEGAJO: ")
            alumno = Alumno(nombreCompleto, legajo)

            salirNotas = "NO"
            while salirNotas == "NO":
                nombreCatedra = input("INGRESE NOMBRE CATEDRA: ")
                notaExamen = leerDecimal("Nota: ")
                nota = Nota(nombreCatedra, notaExamen)
                alumno.agregarNota(nota)
                salirNotas = leerSiNo("DESEA SALIR DE LA CARGA DE NOTAS (SI/NO): ")

            alumnos.append(alumno)
            salirAlumno = leerSiNo("DESEA SALIR DE CARGA DE ALUMNOS (SI/NO): ")

        for alumno in alumnos:
            print("----------- Datos Alumno -----------")
            print("Nombre completo:", alumno.nombreCompleto)
            print("Legajo:", alumno.legajo)
            for nota in alumno.notas:
                print("Cátedra:", nota.catedra, "| Nota:", nota.notaExamen)
            print("El promedio del alumno es:", round(alumno.calcularPromedio(), 2))


if __name__ == "__main__":
    CargaNotas.main()
