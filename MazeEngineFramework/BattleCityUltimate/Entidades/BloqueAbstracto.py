import pygame, math, Constantes

from Entidad import Entidad

class BloqueAbstracto(Entidad):
    """Clase abstracta para la entidad ladrillo"""

    def __init__(self, x, y):
        """Constructor"""

        super().__init__(x, y)
        self.destruido = False
