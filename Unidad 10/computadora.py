class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []

    def agregarComponente(self, componente):
        self.componentes.append(componente)

    def calcularCosto(self):
        total = 0
        for componente in self.componentes:
            total = total + componente.calcularSubTotal()
        return total

    def calcularPrecioVenta(self):
        costo = self.calcularCosto()
        if costo < 50000:
            return costo + costo * 0.40
        return costo + costo * 0.30
