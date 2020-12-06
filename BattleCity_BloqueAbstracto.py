from ME_Entidad import ME_Entidad

import pygame, math

class BloqueAbstracto(ME_Entidad):
    """Clase abstracta para la entidad ladrillo"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.destruido = False
