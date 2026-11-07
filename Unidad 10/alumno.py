class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregarNota(self, nota):
        self.notas.append(nota)

    def calcularPromedio(self):
        try:
            total = 0
            for nota in self.notas:
                total = total + nota.notaExamen
            return total / len(self.notas)
        except ZeroDivisionError:
            return 0
