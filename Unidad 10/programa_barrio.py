from barrio import Barrio
from vivienda import Vivienda
from habitacion import Habitacion


class ProgramaBarrio:
    @staticmethod
    def main():
        barrio = Barrio("Los Pinos", "Constructora Sol")

        vivienda1 = Vivienda("San Martín", 120, "A", 1, 200.0)
        vivienda1.agregarHabitacion(Habitacion("Dormitorio", 15.0))
        vivienda1.agregarHabitacion(Habitacion("Cocina", 12.0))
        vivienda1.agregarHabitacion(Habitacion("Living", 25.0))

        vivienda2 = Vivienda("San Martín", 130, "A", 2, 250.0)
        vivienda2.agregarHabitacion(Habitacion("Dormitorio", 18.0))
        vivienda2.agregarHabitacion(Habitacion("Baño", 6.0))

        vivienda3 = Vivienda("Belgrano", 45, "B", 1, 300.0)
        vivienda3.agregarHabitacion(Habitacion("Dormitorio", 20.0))
        vivienda3.agregarHabitacion(Habitacion("Cocina", 14.0))
        vivienda3.agregarHabitacion(Habitacion("Garage", 30.0))

        barrio.agregarVivienda(vivienda1)
        barrio.agregarVivienda(vivienda2)
        barrio.agregarVivienda(vivienda3)

        print("Barrio:", barrio.nombre, "| Empresa constructora:", barrio.empresaConstructora)
        print("Superficie total de terreno:", barrio.getSuperficieTotalTerreno())
        print("Superficie total de terreno de la manzana A:", barrio.getSuperficieTotalTerrenoXManzana("A"))
        print("Superficie total de terreno de la manzana B:", barrio.getSuperficieTotalTerrenoXManzana("B"))
        print("Metros cubiertos de la vivienda 1:", vivienda1.getMetrosCuadradosCubiertos())
        print("Superficie total cubierta del barrio:", barrio.getSuperficieTotalCubierta())

        viviendaInvalida = Vivienda("Mitre", 10, "C", 1, 50.0)
        viviendaInvalida.agregarHabitacion(Habitacion("Salón", 40.0))
        viviendaInvalida.agregarHabitacion(Habitacion("Dormitorio", 20.0))
        barrio.agregarVivienda(viviendaInvalida)

        try:
            print("Superficie total cubierta del barrio:", barrio.getSuperficieTotalCubierta())
        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    ProgramaBarrio.main()
