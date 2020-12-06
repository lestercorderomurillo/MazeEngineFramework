from BattleCity_PoderAbstracto import PoderAbstracto
import pygame
class PoderMejorarTanque(PoderAbstracto):
    """Clase para el poder de mejorar el tanque"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio) 
        self.image = self.crearAnimacion(32*11, 32*2, 32, 32)
        self.sonidoCambiarTipo = pygame.mixer.Sound("./Recursos/Sonidos/CambiaTipo.ogg")
        self.sonidoCambiarTipo.set_volume(0.5)
        
    def activarPoder(self, jugador):
        if jugador.tipoTanqueActual < 3:
            self.sonidoCambiarTipo.play()
            jugador.armadura = jugador.tipoTanqueActual + jugador.armadura + 1
            jugador.velocidadMaxima += 1
            jugador.tipoTanqueActual += 1
            jugador.cargarSprites(jugador.tipoTanqueActual)
        else:
            if jugador.armadura >= (jugador.tipoTanqueActual + 1):
                jugador.armadura += 1
            else:
                jugador.armadura = jugador.tipoTanqueActual + 1 

