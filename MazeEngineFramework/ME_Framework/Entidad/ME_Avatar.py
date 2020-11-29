from ME_Entidad import ME_Entidad
import enum, pygame

class Direccion(enum.Enum):
    """Enumeración de las direcciones posibles para los avatares"""
    Arriba    = 1
    Derecha   = 2
    Abajo     = 3
    Izquierda = 4

ajusteDeColision = 15

class ME_Avatar(ME_Entidad):
    """Clase genérica para los tipos de avatar"""

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

    def update(self):
        if self.velocidadActualX != 0 or self.velocidadActualY != 0:
            self.moviendose = True
        else:
            self.moviendose = False
        animarAvatar()
        self.rect.x += self.velocidadActualX * self.velocidadMaxima
        self.rect.y += self.velocidadActualY * self.velocidadMaxima


    def animarAvatar(self):
        """Método para animar al tanque"""

        if self.vivo:
            if (self.moviendose):
                imagenAnimacion = math.floor(self.contadorAnimarMovimiento)
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

            self.contadorAnimarMovimiento += 0.5

            #Todos los vectores de animación tienen 4 sprites
            if self.contadorAnimarMovimiento >= 4:
                self.contadorAnimarMovimiento = 0

        else:
            if self.contadorAnimarMuerte < len(animacionMuerto):
                imagenAnimacion = math.floor(self.contadorAnimarMuerte)
                self.image = self.animacionMuerto[imagenAnimacion]
                self.contadorAnimarMuerte += 0.1



