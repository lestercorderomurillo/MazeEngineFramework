from ME_Avatar_Manipulable import ME_Avatar_Controlable
import math, enum, pygame

class TipoTanque(enum.IntEnum):
    """Enumeración de los tipos posibles para los tanques"""
    Inicial         = 0
    Principiante    = 1
    Avanzado        = 2
    Final           = 3

class TanqueJugador(ME_Avatar_Controlable):
    """clase para el tanque del jugador"""

    def __init__(self, x, y, tamanio):
        """Constructor"""
        super().__init__(x, y, tamanio)
        self.velocidadMaxima = 4
        self.armadura = 1
        self.puntuacion = 0
        self.tipoTanqueActual = TipoTanque.Inicial
        self.cargarSprites(self.tipoTanqueActual)
        self.cargarSpritesMuerte()
        self.image = self.animacionArriba[0]
        
    """
        #Sonidos
        self.sonidoAgarraPoder = pygame.mixer.Sound(Constantes.S_AG_PODER)
        self.sonidoNuevoTipo = pygame.mixer.Sound(Constantes.S_TIPO)
        self.sonidoDisparar = pygame.mixer.Sound(Constantes.S_DISPARAR)
        self.sonidoMoverse = pygame.mixer.Sound(Constantes.S_MOVER)
        self.sonidoQuieto = pygame.mixer.Sound(Constantes.S_QUIETO)
        self.sonidoMorir = pygame.mixer.Sound(Constantes.S_MORIR)

        self.sonidoAgarraPoder.set_volume(Constantes.VOLUMEN)
        self.sonidoNuevoTipo.set_volume(Constantes.VOLUMEN)
        self.sonidoDisparar.set_volume(Constantes.VOLUMEN)
        self.sonidoMoverse.set_volume(Constantes.VOLUMEN/4)
        self.sonidoQuieto.set_volume(Constantes.VOLUMEN/4)
        self.sonidoMorir.set_volume(Constantes.VOLUMEN)
    """

    def update(self):
        super().update()
        if self.contadorAnimarMuerte >= len(animacionMuerto):
            self.contadorAnimacionMuerte = 0
            if self.vidas > 0:
                self.reaparecer()


    def cargarSprites(self, tipoTanque):
        """Método para animar el tanque del jugador según su tipo"""

        #Se borran los sprites anteriores para actualizarlos con el tipo de tanque correspondiente
        self.animacionArriba.clear()
        self.animacionDerecha.clear()
        self.animacionAbajo.clear()
        self.animacionIzquierda.clear()

        for xx in range(2):
            self.animacionArriba.append(    self.crearAnimacion(32*(0+xx*1), 32*self.tipoTanqueActual, 32, 32) )
            self.animacionDerecha.append(   self.crearAnimacion(32*(2+xx*1), 32*self.tipoTanqueActual, 32, 32) )
            self.animacionAbajo.append(     self.crearAnimacion(32*(4+xx*1), 32*self.tipoTanqueActual, 32, 32) )
            self.animacionIzquierda.append( self.crearAnimacion(32*(6+xx*1), 32*self.tipoTanqueActual, 32, 32) )

        for x in range(2):
            self.animacionArriba.append(    self.animacionArriba[x]   )
            self.animacionDerecha.append(   self.animacionDerecha[x]  )
            self.animacionAbajo.append(     self.animacionAbajo[x]    )
            self.animacionIzquierda.append( self.animacionIzquierda[x])


    def cargarSpritesMuerte(self):
        """Método para animar la muerte de los tanques"""
        for x in range(3):
            self.animacionMuerto.append(self.crearAnimacion(32*(10+x), 0, 32, 32))


    def reaparecer(self):
        """Método para reaparecer el tanque"""

        self.armadura = 1
        self.velocidadMaxima = 4
        self.vivo = True
        self.rect.x = self.tamanio*4
        self.rect.y = self.tamanio*16
        self.direccion = Direccion.Arriba
        self.tipoTanqueActual = TipoTanque.Inicial
        self.cargarSprites(TipoTanque.Inicial)


            
