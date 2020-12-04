import pygame, math

from ME_Framework.Entidad.ME_Entidad import ME_Entidad

class BloqueAbstracto(ME_Entidad):
    """Clase abstracta para la entidad ladrillo"""

    def __init__(self, x, y):
        """Constructor"""

        super().__init__(x, y)
        self.destruido = False
