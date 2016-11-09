#coding: utf 8 *
def hola (nombre="Mundo"):
    print "Hola", nombre

hola("Juan")
hola()
print
class animal:
    def __init__(self, patas=4, tipo="pequeño"):
        self.patas=patas
        self.tipo=tipo

class perro(animal):
    """pass //no hace nada"""

    def __init__(self, nombre="oddy", raza="Jack"):#Inicializa
        self.nombre=nombre
        self.raza=raza
        
    #def saluda(self):
     #   return "Te saluda %s" % self.nombre

perrito =perro(tipo ="Mediano",nombre="Lucas", raza="Jack")
perrito_juan=perro()
print(perrito.nombre)
print(perrito.raza)
print(perrito.tipo)
print(perrito.patas)
print
#perrito.saluda
print
print(perrito_juan.nombre)
print(perrito_juan.raza)
#perrito_juan.saluda