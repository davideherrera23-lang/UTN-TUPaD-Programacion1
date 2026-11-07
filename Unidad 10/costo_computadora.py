from componente_cpu import ComponenteCPU
from computadora import Computadora


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


class CostoComputadora:
    @staticmethod
    def main():
        cotizar = "SI"
        while cotizar == "SI":
            marca = input("Ingrese la marca de la computadora: ")
            modelo = input("Ingrese el modelo de la computadora: ")
            computadora = Computadora(marca, modelo)

            otroComponente = "SI"
            while otroComponente == "SI":
                nombreComponente = input("Ingrese el componente: ")
                marcaComponente = input("Ingrese la marca del componente: ")
                cantidad = leerEntero("Ingrese la cantidad: ")
                precio = leerDecimal("Ingrese el precio por unidad: ")
                computadora.agregarComponente(ComponenteCPU(nombreComponente, marcaComponente, cantidad, precio))
                otroComponente = leerSiNo("¿Desea cargar otro componente? (SI/NO): ")

            print("-----------Computadora----------------")
            print("Marca:", computadora.marca)
            print("Modelo:", computadora.modelo)
            print("Componentes:")
            print("Componente Marca Cantidad Precio X Unidad SubTotal")
            for componente in computadora.componentes:
                print(componente.componente, componente.marca, componente.cantidad, componente.precio, componente.calcularSubTotal())
            costo = computadora.calcularCosto()
            precioVenta = computadora.calcularPrecioVenta()
            print("Costo Total", costo)
            print("El precio sugerido de venta es", costo, "+", precioVenta - costo, "=", precioVenta)

            cotizar = leerSiNo("¿Desea cotizar una nueva computadora? (SI/NO): ")


if __name__ == "__main__":
    CostoComputadora.main()
