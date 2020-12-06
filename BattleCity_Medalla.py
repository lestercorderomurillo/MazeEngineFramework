from ME_Entidad import ME_Entidad
from ME_Entidad import Direccion


import pygame

class Medalla(ME_Entidad):
    """Clase para la entidad medalla"""

    def __init__(self, x, y, tamanio, bando):
        """Constructor"""

        super().__init__(x, y, tamanio)

        self.rescadasRestantes = 3

        self.tomada = False
        self.bando = bando
        self.destruida = False

        self.xInicial = x
        self.yInicial = y

        if(self.bando == 1):
            self.imageSrc = self.crearAnimacion(32*9,32*3, 32, 32)
        else:
            self.imageSrc = self.crearAnimacion(32*8,32*4, 32, 32)

        self.image = self.imageSrc

        #self.sonidoEntregarMedalla = pygame.mixer.Sound(Constantes.S_BANDERA)
        #self.sonidoEntregarMedalla.set_volume(Constantes.VOLUMEN)

    def update(self, jugador, deposito):
        """Método para actualizar el estado de la entidad medalla"""

        if(self.bando == 1):
            if (self.tomada):
                if jugador.vivo == False:
                    self.rect.x = self.xInicial
                    self.rect.y = self.yInicial
                    self.tomada = False
                else:
                    if (jugador.direccion == Direccion.Arriba):
                        self.rect.x = jugador.rect.x + 16
                        self.rect.y = jugador.rect.y - 2
                        self.image = pygame.transform.flip(self.imageSrc, False, False)
                    if (jugador.direccion == Direccion.Abajo):
                        self.rect.x = jugador.rect.x + 16
                        self.rect.y = jugador.rect.y - 31
                        self.image = pygame.transform.flip(self.imageSrc, False, False)
                    if (jugador.direccion == Direccion.Derecha):
                        self.rect.x = jugador.rect.x + 3
                        self.rect.y = jugador.rect.y - 16
                        self.image = pygame.transform.flip(self.imageSrc, False, False)
                    if (jugador.direccion == Direccion.Izquierda):
                        self.rect.x = jugador.rect.x - 3
                        self.rect.y = jugador.rect.y - 16 
                        self.image = pygame.transform.flip(self.imageSrc, True, False)
                    if (self.rect.colliderect(deposito)):
                        self.tomada = False
                        self.rescadasRestantes -= 1
                        #self.sonidoEntregarMedalla.play()
            else:
                self.rect.x = self.xInicial
                self.rect.y = self.yInicial
                if (self.rect.colliderect(jugador)):
                    self.tomada = True
