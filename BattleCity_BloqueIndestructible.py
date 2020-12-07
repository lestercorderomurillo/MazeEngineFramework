##@package BloqueIndestructible
#Clase para el ladrillo indestructible del juego

##\details El bloque hereda de Bloque abstracto
from BattleCity_BloqueAbstracto import BloqueAbstracto

class BloqueIndestructible(BloqueAbstracto):

## Constructor de BloqueIndestructible. Recibe coordenadas y tamaño del bloque a crear 
#\param x,y y tamanio, que determinan posicion y dimensiones del bloque
#\details Este método construye una instancia de la clase BloqueIndestructible. Como su nombre lo indica, este tipo de ladrillo no se puede destruir, 
#por lo que se omite atributos como vidas y método update que sí están presentes en bloques destruibles. También asigna al bloque un sprite.   
#\return No retorna valor alguno
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*14, 32*2, 32, 32)
