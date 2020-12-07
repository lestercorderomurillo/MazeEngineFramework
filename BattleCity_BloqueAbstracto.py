## @package BloqueAbstracto
#Es la clase de bloque del cual heredarán todos los demás tipos de bloque.

##\details  La clase hereda de ME_Entidad
from ME_Entidad import ME_Entidad

import pygame, math

class BloqueAbstracto(ME_Entidad):
    """Clase abstracta para la entidad ladrillo"""

##Constructor de la clase, que luego será invocado por el resto de bloques que hereden de ella.  
#\details Este constructor será utilizado por el resto de clases que hereden de BloqueAbstracto. El constructor a su vez invoca el de ME_Entidad y define destruido como
#variable para determinar cuándo el bloque debe desaperecer de pantalla.   
#\param x,y y tamanio, que determinan posicion y dimensiones del bloque
#\return No retorna valor alguno   
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.destruido = False
