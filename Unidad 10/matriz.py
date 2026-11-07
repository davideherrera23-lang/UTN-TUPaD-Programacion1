class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def existeCelda(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return True
        return False

    def agregarCelda(self, celda):
        if self.existeCelda(celda.fila, celda.columna):
            return False
        self.celdasMatriz.append(celda)
        return True

    def mostrarCeldas(self):
        print("----------- CELDAS CARGADAS -----------")
        for celda in self.celdasMatriz:
            print("Fila:", celda.fila, "| Columna:", celda.columna, "| Valor:", celda.valor)

    def obtenerValor(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"
