import pygame, math

from PoderAbstracto import PoderAbstracto

class PoderMejorarTanque(PoderAbstracto):
    """Clase para el poder de mejorar el tanque"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio) 
        self.image = self.crearAnimacion(32*11, 32*2, 32, 32)

    def activarPoder(self, jugador):
        if jugador.tipoTanqueActual < 3:
            jugador.armadura = jugador.tipoTanqueActual + jugador.armadura + 1
            jugador.velocidad += 1
            jugador.tipoTanqueActual += 1
            jugador.cargarSprites(jugador.tipoTanqueActual)
        else:
            if jugador.armadura >= (jugador.tipoTanqueActual + 1):
                jugador.armadura += 1
            else:
                jugador.armadura = jugador.tipoTanqueActual + 1 

