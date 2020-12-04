from ME_Framework.ME_Controlador import ME_Controlador
from ME_Framework.ME_Laberinto import ME_Laberinto
import pygame, math

class LaberintoBattleCity(ME_Laberinto):

    def __init__(self, tamanio):
        """Constructor"""

        self.grupoJugador = pygame.sprite.Group()
        self.grupoEnemigos = pygame.sprite.Group()
        self.grupoBloques = pygame.sprite.Group()
        self.grupoBalas = pygame.sprite.Group()
        self.grupoPoderes = pygame.sprite.Group()
        self.grupoMedallas = pygame.sprite.Group()
        self.interfaz = Interfaz(tamanio)

    def update(self, controlador):
        """"""
        super().update()

        
    def draw(self, controlador, pantalla):
        super().draw(controlador, pantalla)

    def evento(self, controlador, evento):
        """"""
        if(evento.type == pygame.KEYDOWN):

            if(evento.key == pygame.K_ESCAPE):
                controlador.menuAbierto = True

        super().evento(controlador, evento)

class Interfaz():
    """Clase para la interfaz del juego"""

    def __init__(self, taman):
        """Constructor"""

        self.tamanio = taman

        self.visualStudio = True
        if(self.visualStudio):
            self.hud1_png = pygame.transform.scale(pygame.image.load("./BattleCityUltimate/Recursos/Imagenes/Menu/HUD1.png").convert_alpha(), (self.tamanio[0], self.tamanio[1]))
            self.hud2_png = pygame.transform.scale(pygame.image.load("./BattleCityUltimate/Recursos/Imagenes/Menu/HUD2.png").convert_alpha(), (self.tamanio[0], self.tamanio[1]))
            self.hud3_png = pygame.transform.scale(pygame.image.load("./BattleCityUltimate/Recursos/Imagenes/Menu/HUD3.png").convert_alpha(), (self.tamanio[0], self.tamanio[1]))
        else:
            self.hud1_png = pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/HUD1.png").convert_alpha(), (self.tamanio[0], self.tamanio[1]))
            self.hud2_png = pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/HUD2.png").convert_alpha(), (self.tamanio[0], self.tamanio[1]))
            self.hud3_png = pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/HUD3.png").convert_alpha(), (self.tamanio[0], self.tamanio[1]))

        self.contador = 0

    def draw(self, pantalla, laberinto):
        """Método para agregar la interfaz del juego"""

        vidasJugador = 1#laberinto.tanqueJugador.vida
        jugadorMuerto = False#laberinto.tanqueJugador.muerto
        puntuacionJugador = 100#laberinto.tanqueJugador.puntuacion
        armaduraJugador = 1#laberinto.tanqueJugador.armadura
        banderasCapturadas = 2#laberinto.medallaEnemiga.rescadasRestantes
        nivelActual = 1#laberinto.laberinto

        if(self.visualStudio):
            font = pygame.font.Font("./BattleCityUltimate/Recursos/8bitOperatorPlus-Bold.ttf", math.floor(40/1.06)) 
        else:
            font = pygame.font.Font("./Recursos/8bitOperatorPlus-Bold.ttf", math.floor(40/1.06)) 

        vidas       = font.render(str(vidasJugador),       True, (255, 255, 255)) 
        armadura    = font.render(str(armaduraJugador),    True, (255, 255, 255)) 
        puntuacion  = font.render(str(puntuacionJugador),  True, (255, 255, 255)) 
        banderas    = font.render(str(banderasCapturadas), True, (255, 255, 255)) 
        nivel       = font.render(str(nivelActual),        True, (255, 255, 255)) 

        vidasRect       = vidas.get_rect()
        armaduraRect    = armadura.get_rect()
        puntuacionRect  = puntuacion.get_rect()
        banderasRect    = banderas.get_rect()
        nivelRect       = nivel.get_rect()

        nivelRect.center        = (self.tamanio[0]/1.0746, self.tamanio[1]/6.9677)
        banderasRect.center     = (self.tamanio[0]/1.0285, self.tamanio[1]/2.5411)
        vidasRect.center        = (self.tamanio[0]/1.0285, self.tamanio[1]/1.8382)
        armaduraRect.center     = (self.tamanio[0]/1.0285, self.tamanio[1]/1.6)
        puntuacionRect.center   = (self.tamanio[0]/1.1, self.tamanio[1]/1.05)
        puntuacionRect.left     = (self.tamanio[0]/1.15)
        
        if(jugadorMuerto):
            pantalla.blit(self.hud3_png, (0, 0))
        else:
            if( math.floor(self.contador)%2 == 0):
                pantalla.blit(self.hud1_png, (0, 0))
            else:
                pantalla.blit(self.hud2_png, (0, 0))

        self.contador += 0.05
        if(self.contador > 20):
            self.contador = 0

        pantalla.blit(nivel, nivelRect)
        pantalla.blit(banderas, banderasRect)
        pantalla.blit(vidas, vidasRect)
        pantalla.blit(armadura, armaduraRect)
        pantalla.blit(puntuacion, puntuacionRect)