import pygame, math

from PoderAbstracto import PoderAbstracto

class PoderEscudo(PoderAbstracto):
    """Clase para el poder de granada"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio) 
        self.image = self.crearAnimacion(32*12, 32*2, 32, 32)

    def activarPoder(self, jugador):
        jugador.armadura += 1
