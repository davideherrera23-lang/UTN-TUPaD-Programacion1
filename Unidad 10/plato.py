class Plato:
    def __init__(self, nombreCompleto, precio, esBebida):
        self.nombreCompleto = nombreCompleto
        self.precio = precio
        self.esBebida = esBebida
        self.ingredientes = []

    def agregarIngrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
