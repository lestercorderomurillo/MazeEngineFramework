import pygame, math

from PoderAbstracto import PoderAbstracto

class PoderGranada(PoderAbstracto):
    """Clase para el poder de granada"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio) 
        self.image = self.crearAnimacion(32*9, 32*2, 32, 32)

    def activarPoder(self, jugador, grupoEnemigos):
        for tanque in grupoEnemigos:
            tanque.esVariocolor = False
            tanque.muerto = True
            if tanque.tipoTanqueActual == TipoTanque.Inicial:
                jugador.puntuacion += 100
            elif tanque.tipoTanqueActual == TipoTanque.Principiante:
                jugador.puntuacion += 200
            elif tanque.tipoTanqueActual == TipoTanque.Avanzado:
                jugador.puntuacion += 300
            elif tanque.tipoTanqueActual == TipoTanque.Final:
                jugador.puntuacion += 400
