import pygame, math

from ArmaMarda import ArmaMarda

class Bala(ArmaMarda):
    """Clase hija de la entidad proyectil"""

    def __init__(self,x, y, direccion, tamanio, bando):
        """Constructor"""

        super().__init__(x, y, direccion, tamanio)

        escala = (math.floor(Constantes.TAMANIO/4), math.floor(Constantes.TAMANIO/4))

        self.bando = bando
        self.ataque = 1
        self.animacionArriba.append(    pygame.transform.scale(self.crearAnimacion(32*13+0 , 0, 8, 8), escala))
        self.animacionDerecha.append(   pygame.transform.scale(self.crearAnimacion(32*13+8 , 0, 8, 8), escala))
        self.animacionAbajo.append(     pygame.transform.scale(self.crearAnimacion(32*13+16, 0, 8, 8), escala))
        self.animacionIzquierda.append( pygame.transform.scale(self.crearAnimacion(32*13+24, 0, 8, 8), escala))
        self.animacionExplosion.append( pygame.transform.scale(self.crearAnimacion(32*12, 0, 32, 32), escala))
        self.image = self.animacionArriba[0]
        self.velocidadActualX = 0
        self.velocidadActualY = 0

        self.rect = pygame.Rect(x, y, tamanio/4, tamanio/4)

        if (direccion == Direccion.Arriba):
            x += tamanio/2.6666
            y += tamanio/4
        elif (direccion == Direccion.Abajo):
            x += tamanio/2.6666
            y += tamanio/1.92
        elif (direccion == Direccion.Derecha):
            x += tamanio/1.92
            y += tamanio/2.6666
        elif (direccion == Direccion.Izquierda):
            x += tamanio/4
            y += tamanio/2.6666
            
        """
        self.sonidoMorir = pygame.mixer.Sound(Constantes.S_DESTRUIR_E)
        self.sonidoArmadura = pygame.mixer.Sound(Constantes.S_ARMADURA)
        self.sonidoDestruirBloque = pygame.mixer.Sound(Constantes.S_DESTRUIR_B)

        self.sonidoArmadura.set_volume(Constantes.VOLUMEN)
        self.sonidoMorir.set_volume(Constantes.VOLUMEN)
        self.sonidoDestruirBloque.set_volume(Constantes.VOLUMEN)
        """


    def update(self, grupoJugador, grupoEnemigos, grupoBloques, grupoBalas, grupoMedallas):
        """Método para actualizar el estado de la entidad proyectil"""
        super.update()
        
        if(self.direccion == Direccion.Abajo):
            self.image = self.animacionAbajo[self.imagenAnimacion]
            self.velocidadActualY = 20

        if(self.direccion == Direccion.Derecha):
            self.image = self.animacionDerecha[self.imagenAnimacion]
            self.velocidadActualX = 20

        if(self.direccion == Direccion.Arriba):
            self.image = self.animacionArriba[self.imagenAnimacion]
            self.velocidadActualY = -20

        if(self.direccion == Direccion.Izquierda):
            self.image = self.animacionIzquierda[self.imagenAnimacion]
            self.velocidadActualX = -20

        self.rect.x += self.velocidadActualX
        self.rect.y += self.velocidadActualY

