from ME_Avatar_Autonomo import ME_Avatar_Autonomo
import math, enum, pygame, random
from Bala import Bala

from PoderVidaExtra import PoderVidaExtra
from PoderGranada import PoderGranada
from PoderEscudo import PoderEscudo
from PoderMejorarTanque import PoderMejorarTanque
from PoderCongelarEnemigos import PoderCongelarEnemigos
from PoderReforzarBase import PoderReforzarBase

class TipoTanque(enum.IntEnum):
    """Enumeración de los tipos posibles para los tanques"""
    Inicial         = 0
    Principiante    = 1
    Avanzado        = 2
    Final           = 3

class TanqueEnemigo(ME_Avatar_Autonomo):
    """Clase hija de la entidad tanque"""
    def __init__(self, x, y, tamanio, esVaricolor, tipoTanque):  
        """Constructor"""

        super().__init__(x, y, tamanio) 
	self.tamanio = tamanio
        #Atributos del tanque enemigo
        self.tipoTanqueActual = tipoTanque
        self.image = self.animacionArriba[0]
        self.esVariocolor = esVariocolor

        self.cargarSprites(self.tipoTanqueActual)
        self.cargarSpritesMuerte()

        #Imagen con la que inicia el tanque
        self.image = self.animacionArriba[0]

        if self.tipoTanqueActual = TipoTanque.Inicial:
            self.velocidadMaxima = 1
            self.armadura = 1
        elif self.tipoTanqueActual = TipoTanque.Principiante:
            self.velocidadMaxima = 2
            self.armadura = 2
        elif self.tipoTanqueActual = TipoTanque.Avanzado:
            self.velocidadMaxima = 4
            self.armadura = 3
        elif self.tipoTanqueActual = TipoTanque.Final:
            self.velocidadMaxima = 3
            self.armadura = 4

    def update(self, grupoBalas, grupoPoderes):
        """Método para actualizar el estado de la entidad tanque"""
        super().update()
        if self.contadorAnimarMuerte >= len(animacionMuerto):
            self.kill()
            self.generarPoder(grupoPoderes)
        
        self.moverAutomatico()
        self.disparar(grupoBalas)

    def cargarSprites(self, tipoTanque):
        """Método para animar el tanque enemigo según su tipo"""

        if(self.esVariocolor):
            for xx in range(4):
                #Los tanques variocolor tienen 4 sprites
                self.animacionArriba.append(    self.crearAnimacion(32*(0 +xx*1), (32*tipoTanque+32*8), 32, 32))
                self.animacionDerecha.append(   self.crearAnimacion(32*(4 +xx*1), (32*tipoTanque+32*8), 32, 32))
                self.animacionAbajo.append(     self.crearAnimacion(32*(8 +xx*1), (32*tipoTanque+32*8), 32, 32))
                self.animacionIzquierda.append( self.crearAnimacion(32*(12+xx*1), (32*tipoTanque+32*8), 32, 32))
        else:
            for xx in range(2):
                self.animacionArriba.append(    self.crearAnimacion(32*(0+xx*1), (32*tipoTanque+32*4), 32, 32))
                self.animacionDerecha.append(   self.crearAnimacion(32*(2+xx*1), (32*tipoTanque+32*4), 32, 32))
                self.animacionAbajo.append(     self.crearAnimacion(32*(4+xx*1), (32*tipoTanque+32*4), 32, 32))
                self.animacionIzquierda.append( self.crearAnimacion(32*(6+xx*1), (32*tipoTanque+32*4), 32, 32))

            for x in range(2):
                self.animacionArriba.append(    self.animacionArriba[x]   )
                self.animacionDerecha.append(   self.animacionDerecha[x]  )
                self.animacionAbajo.append(     self.animacionAbajo[x]    )
                self.animacionIzquierda.append( self.animacionIzquierda[x])


    def cargarSpritesMuerte(self):
        """Método para animar la muerte de los tanques enemigos"""
        for x in range(3):
            self.animacionMuerto.append(self.crearAnimacion(32*(10+x), 0, 32, 32))

    def disparar(self,grupoBalas):
        """Método para disparar"""
        grupoBalas.add( Bala(self.rect.x,self.rect.y,self.direccion,self.tamanio,1) )

    def generarPoder(self, grupoPoderes):
        """Método para generar poderes aleatoriamente"""

        if self.esVariocolor:
            rand_poder = random.randint(1, 6)
            x = random.randint(1, 17)
            y = random.randint(1, 17)

            if rand_poder == 1 :
                poder = PoderVidaExtra(x*Constantes.TAMANIO,y*Constantes.TAMANIO)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

            elif rand_poder == 2 :
                poder = PoderGranada(x*Constantes.TAMANIO,y*Constantes.TAMANIO)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

            elif rand_poder == 3 :
                poder = PoderEscudo(x*Constantes.TAMANIO,y*Constantes.TAMANIO)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

            elif rand_poder == 4 :
                poder = PoderMejorarTanque(x*Constantes.TAMANIO,y*Constantes.TAMANIO)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

            elif rand_poder == 5 :
                poder = PoderCongelarEnemigos(x*Constantes.TAMANIO,y*Constantes.TAMANIO)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

            elif rand_poder == 6 :
                poder = PoderReforzarBase(x*Constantes.TAMANIO,y*Constantes.TAMANIO)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

