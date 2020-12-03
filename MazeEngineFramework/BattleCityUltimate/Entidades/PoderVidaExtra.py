import pygame, math

from PoderAbstracto import PoderAbstracto

class PoderVidaExtra(PoderAbstracto):
    """Clase para el poder de vida extra"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio) 
        self.image = self.crearAnimacion(32*10, 32*2, 32, 32)

    def activarPoder(self, jugador):
        jugador.vida += 1
