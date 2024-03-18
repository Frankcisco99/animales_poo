
class Perro:
    def __init__(self, nombre, raza, edad):
        self._nombre = nombre
        self._raza = raza
        self._edad = edad
        
    def mi_nombre(self):
        return f"Mi nombre {self._nombre}"


perro1 = Perro("Blanco", "Poddle", 2)
perro2 = Perro("","",3)