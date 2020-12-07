## @package DepositoMedalla
#Clase para el objeto de deposito medalla

from ME_Entidad import ME_Entidad

class DepositoMedalla(ME_Entidad):
    """Clase para la entidad deposito de las medalla"""
## Constructor para deposito medalla
#\details Asigna un sprite al deposito medalla e invoca al constructor del ME_Entidad
#\param x,y y tamanio
#\return Sin retorno 
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*8,32*5, 32, 32)
