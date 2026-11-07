class Vivienda:
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []

    def agregarHabitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        total = 0
        for habitacion in self.habitaciones:
            total = total + habitacion.metrosCuadrados
        if total > self.superficieTerreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")
        return total
