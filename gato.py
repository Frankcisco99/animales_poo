class Gato:
    def __init__(self, nombre, vidas):
        self._nombre = nombre
        self._vidas = vidas
    
    def nombre(self):
        return f"Hola mi nombre es {self._nombre}"
    
gato1 = Gato("Gato", 5)
gato1.nombre()
        