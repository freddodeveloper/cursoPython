class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentarse(self):
        mensaje_base = super().presentarse()
        return f"{mensaje_base} Estudio la carrera de {self.carrera}."


class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def trabajar(self):
        return f"{self.nombre} está trabajando como {self.puesto}."


if __name__ == "__main__":
    maria = Estudiante("Maria", 20, "Ingeniería en Sistemas")

    juan = Empleado("Juan", 35, "Gerente de Ventas")

    print("--- Resultados ---")
    print(maria.presentarse())
    print(juan.presentarse())
    print(juan.trabajar())

    print(f"\n¿Maria es una Persona?: {isinstance(maria, Persona)}")
