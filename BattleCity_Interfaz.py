import pygame, math

class Interfaz():
    """Clase para la interfaz del juego"""

    def __init__(self, taman):
        """Constructor"""

        self.contador = 0
        self.tamanioPantalla = taman

        self.hud1_png = pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/HUD1.png").convert_alpha(), (self.tamanioPantalla[0], self.tamanioPantalla[1]))
        self.hud2_png = pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/HUD2.png").convert_alpha(), (self.tamanioPantalla[0], self.tamanioPantalla[1]))
        self.hud3_png = pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/HUD3.png").convert_alpha(), (self.tamanioPantalla[0], self.tamanioPantalla[1]))

    def recuperarInformacion(self, laberinto):
        """Método para obtener información del estado actual juego"""

        self.jugadorVivo = laberinto.tanqueJugador.vivo
        vidasJugador = laberinto.tanqueJugador.vidas
        puntuacionJugador = laberinto.tanqueJugador.puntuacion
        armaduraJugador = laberinto.tanqueJugador.armadura
        banderasCapturadas = laberinto.medallaEnemiga.rescadasRestantes
        nivelActual = laberinto.nivel

        font = pygame.font.Font("./Recursos/8bitOperatorPlus-Bold.ttf", math.floor(40/1.06)) 

        self.vidas       = font.render(str(vidasJugador),       True, (255, 255, 255)) 
        self.armadura    = font.render(str(armaduraJugador),    True, (255, 255, 255)) 
        self.puntuacion  = font.render(str(puntuacionJugador),  True, (255, 255, 255)) 
        self.banderas    = font.render(str(banderasCapturadas), True, (255, 255, 255)) 
        self.nivel       = font.render(str(nivelActual),        True, (255, 255, 255)) 

        self.vidasRect       = self.vidas.get_rect()
        self.armaduraRect    = self.armadura.get_rect()
        self.puntuacionRect  = self.puntuacion.get_rect()
        self.banderasRect    = self.banderas.get_rect()
        self.nivelRect       = self.nivel.get_rect()

        self.nivelRect.center        = (self.tamanioPantalla[0]/1.0746, self.tamanioPantalla[1]/6.9677)
        self.banderasRect.center     = (self.tamanioPantalla[0]/1.0285, self.tamanioPantalla[1]/2.5411)
        self.vidasRect.center        = (self.tamanioPantalla[0]/1.0285, self.tamanioPantalla[1]/1.8382)
        self.armaduraRect.center     = (self.tamanioPantalla[0]/1.0285, self.tamanioPantalla[1]/1.6)
        self.puntuacionRect.center   = (self.tamanioPantalla[0]/1.1, self.tamanioPantalla[1]/1.05)
        self.puntuacionRect.left     = (self.tamanioPantalla[0]/1.15)

        self.contador += 0.05
        if(self.contador > 20):
            self.contador = 0

    def draw(self, pantalla, laberinto):
        """Método para dibujar la interfaz del juego"""

        self.recuperarInformacion(laberinto)

        if(not self.jugadorVivo):
            pantalla.blit(self.hud3_png, (0, 0))
        else:
            if( math.floor(self.contador)%2 == 0):
                pantalla.blit(self.hud1_png, (0, 0))
            else:
                pantalla.blit(self.hud2_png, (0, 0))

        pantalla.blit(self.nivel, self.nivelRect)
        pantalla.blit(self.banderas, self.banderasRect)
        pantalla.blit(self.vidas, self.vidasRect)
        pantalla.blit(self.armadura, self.armaduraRect)
        pantalla.blit(self.puntuacion, self.puntuacionRect)
