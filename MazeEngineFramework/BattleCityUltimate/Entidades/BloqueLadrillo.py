import pygame, math, Constantes

from BloqueAbstracto import BloqueAbstracto

class BloqueLadrillo(BloqueAbstracto):
    """Clase para el ladrillo frágil del juego"""

    def __init__(self, x, y):
        """Constructor"""

        super().__init__(x, y)

        self.image = self.crearAnimacion(32*14, 32*0, 32, 32)
        self.vida = 2


    def update(self):
    
        if self.destruido:
            self.kill()

        elif self.vida == 1:
            self.image = self.crearAnimacion(32*15, 32*0, 32, 32)
