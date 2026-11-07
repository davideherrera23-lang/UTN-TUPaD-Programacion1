from ingrediente import Ingrediente
from plato import Plato


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


class MenuRestaurant:
    @staticmethod
    def main():
        platosMenu = []
        otroPlato = "SI"
        while otroPlato == "SI":
            nombre = input("Ingrese el nombre del plato: ")
            precio = leerDecimal("Ingrese el precio: ")
            esBebida = leerSiNo("¿Es una bebida? (SI/NO): ") == "SI"
            plato = Plato(nombre, precio, esBebida)

            if not esBebida:
                otroIngrediente = "SI"
                while otroIngrediente == "SI":
                    nombreIngrediente = input("Ingrese el nombre del ingrediente: ")
                    cantidad = leerDecimal("Ingrese la cantidad: ")
                    unidad = input("Ingrese la unidad de medida: ")
                    plato.agregarIngrediente(Ingrediente(nombreIngrediente, cantidad, unidad))
                    otroIngrediente = leerSiNo("¿Desea cargar otro ingrediente? (SI/NO): ")

            platosMenu.append(plato)
            otroPlato = leerSiNo("¿Desea cargar otro plato? (SI/NO): ")

        print("-----------MENÚ----------------")
        for plato in platosMenu:
            print(plato.nombreCompleto)
            print("Precio: $", plato.precio)
            if not plato.esBebida:
                print("Ingredientes:")
                print("Nombre Cantidad Unidad de Medida")
                for ingrediente in plato.ingredientes:
                    print(ingrediente.nombre, ingrediente.cantidad, ingrediente.unidadMedida)
            print("----------------------------------")


if __name__ == "__main__":
    MenuRestaurant.main()
