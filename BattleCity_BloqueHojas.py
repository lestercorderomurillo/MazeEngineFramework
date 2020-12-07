##@package BloqueHojas
#  Es uno de los tipos especiales de bloque que existen en el juego. Dificulta la visibilidad de los objetos que están abajo.

##\details El bloque hereda de Bloque abstracto
from BattleCity_BloqueAbstracto import BloqueAbstracto

class BloqueHojas(BloqueAbstracto):

##Constructor de la clase  
#\details Este método construye una instancia de la clase BloqueHojas. Este bloque omite vidas y método update por que no puede ser destruido. También asigna al bloque un sprite.   
#\param x,y y tamanio, que determinan posicion y dimensiones del bloque
#\return No retorna valor alguno   
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*14, 32*3, 32, 32)
