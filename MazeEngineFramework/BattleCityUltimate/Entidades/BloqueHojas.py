import pygame, math, Constantes

from BloqueAbstracto import BloqueAbstracto

class BloqueHojas(BloqueAbstracto):
    """Clase para las hojas del juego"""

    def __init__(self, x, y):
        """Constructor"""

        super().__init__(x, y)
        self.image = self.crearAnimacion(32*14, 32*3, 32, 32)
