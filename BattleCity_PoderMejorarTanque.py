from BattleCity_PoderAbstracto import PoderAbstracto
import pygame
class PoderMejorarTanque(PoderAbstracto):
    """Clase para el poder de mejorar el tanque"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego, tamanio: del sprite
    #\return no retorna valor
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*11, 32*2, 32, 32)
        self.sonidoCambiarTipo = pygame.mixer.Sound("./Recursos/Sonidos/CambiaTipo.ogg")
        self.sonidoCambiarTipo.set_volume(0.5)

    ## Mejora el tanque del jugador
    # \details Aumenta la armadura y velocidad, cambia el sprite del tanque al mejorado
    # en caso de tener la máxima mejora, se mejora la armadura
    # \param jugador: avatar del jugador
    #\return no retorna valor
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
