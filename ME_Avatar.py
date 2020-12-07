from ME_Entidad import ME_Entidad
from ME_Entidad import Direccion

import enum, pygame, math

ajusteDeColision = 15

class ME_Avatar(ME_Entidad):
    """Clase genérica para los tipos de avatar"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego,taman: tamanio del sprite
    #\return no retorna valor
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.tamanio = tamanio
        self.rect = pygame.Rect(x, y, self.tamanio - (self.tamanio/ajusteDeColision), self.tamanio - (self.tamanio/ajusteDeColision))
        self.direccion = Direccion.Arriba
        self.animacionArriba     = []
        self.animacionDerecha    = []
        self.animacionAbajo      = []
        self.animacionIzquierda  = []
        self.animacionMuerto     = []

        self.moviendose = False
        self.vivo = True
        self.activo = True
        self.velocidadMaxima = 1
        self.velocidadActualX = 0
        self.velocidadActualY = 0

        #Imagen con la que inicia el avatar
        self.image = None
        self.contadorAnimacionMovimiento = 0
        self.contadorAnimacionMuerte = 0

    ## Actualiza del estado del avatar
    # \details Actualiza del estado del avatar incluyendo su moviento actual
    # \param  no parametro requerido
    #\return no retorna valor
    def update(self):
        """"""
        if self.velocidadActualX != 0 or self.velocidadActualY != 0:
            self.moviendose = True
        else:
            self.moviendose = False
        self.animarAvatar()
        self.rect.x += self.velocidadActualX * self.velocidadMaxima
        self.rect.y += self.velocidadActualY * self.velocidadMaxima

    ## Animación del avatar
    # \details Actualiza del estado del sprite para el avatar
    # \param  no parametro requerido
    #\return no retorna valor
    def animarAvatar(self):
        """Método para animar al avatar"""

        if self.vivo:
            if (self.moviendose):
                imagenAnimacion = math.floor(self.contadorAnimacionMovimiento)
            else:
                imagenAnimacion = 0

            if(self.direccion == Direccion.Arriba ):
                self.image = self.animacionArriba[imagenAnimacion]

            elif(self.direccion == Direccion.Derecha ):
                self.image = self.animacionDerecha[imagenAnimacion]

            elif(self.direccion == Direccion.Abajo ):
                self.image = self.animacionAbajo[imagenAnimacion]

            elif(self.direccion == Direccion.Izquierda ):
                self.image = self.animacionIzquierda[imagenAnimacion]

            self.contadorAnimacionMovimiento += 0.5

            #Todos los vectores de animación tienen 4 sprites
            if self.contadorAnimacionMovimiento >= 4:
                self.contadorAnimacionMovimiento = 0

        else:
            self.velocidadActualX = 0
            self.velocidadActualY = 0
            if self.contadorAnimacionMuerte < len(self.animacionMuerto):
                imagenAnimacion = math.floor(self.contadorAnimacionMuerte)
                self.image = self.animacionMuerto[imagenAnimacion]
                self.contadorAnimacionMuerte += 0.1
