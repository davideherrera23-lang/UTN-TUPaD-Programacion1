class Barrio:
    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []

    def agregarVivienda(self, vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerreno(self):
        total = 0
        for vivienda in self.viviendas:
            total = total + vivienda.superficieTerreno
        return total

    def getSuperficieTotalTerrenoXManzana(self, manzana):
        total = 0
        for vivienda in self.viviendas:
            if vivienda.manzana == manzana:
                total = total + vivienda.superficieTerreno
        return total

    def getSuperficieTotalCubierta(self):
        total = 0
        for vivienda in self.viviendas:
            total = total + vivienda.getMetrosCuadradosCubiertos()
        return total
