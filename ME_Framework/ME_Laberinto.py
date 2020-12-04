import pygame

class ME_Laberinto():
    """Laberinto del framework"""

    def update(self):
        """"""

    def evento(self, controlador, evento):
        """"""

        if(evento.type == pygame.QUIT):
            controlador.ejecutandoInicio = False
            controlador.ejecutandoJuego = False

    def draw(self, controlador, pantalla):
        """"""

        if(not controlador.menuAbierto):
            pantalla.fill((0, 0, 0))
            self.grupoJugador.draw(pantalla)
            self.grupoEnemigos.draw(pantalla)
            self.grupoBloques.draw(pantalla)
            self.grupoBalas.draw(pantalla)
            self.grupoPoderes.draw(pantalla)
            self.interfaz.draw(pantalla, self)