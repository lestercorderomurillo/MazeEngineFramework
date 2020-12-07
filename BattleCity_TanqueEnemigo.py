from ME_Avatar_Autonomo import ME_Avatar_Autonomo
from ME_Entidad import Direccion
from ME_Entidad import Bando

from BattleCity_Bala import Bala

from BattleCity_PoderVidaExtra import PoderVidaExtra
from BattleCity_PoderGranada import PoderGranada
from BattleCity_PoderEscudo import PoderEscudo
from BattleCity_PoderMejorarTanque import PoderMejorarTanque
from BattleCity_PoderCongelarEnemigos import PoderCongelarEnemigos
from BattleCity_PoderReforzarBase import PoderReforzarBase

import math, enum, pygame, random

class TipoTanque(enum.IntEnum):
    """Enumeración de los tipos posibles para los tanques"""
    Inicial         = 0
    Principiante    = 1
    Avanzado        = 2
    Final           = 3

class TanqueEnemigo(ME_Avatar_Autonomo):
    """Clase hija de la entidad tanque"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego, tamanio: del sprite,
    # esVarioColor: si tanque crea poder al morir, tipoTanque: tipo del tanque
    #\return no retorna valor
    def __init__(self, x, y, tamanio, esVariocolor, tipoTanque):
        """Constructor"""

        super().__init__(x, y, tamanio)

        #Atributos del tanque enemigo
        self.tipoTanqueActual = tipoTanque

        self.esVariocolor = esVariocolor
        self.tamanio = tamanio
        self.bando = Bando.Enemigo
        self.armadura = 1

        self.cargarSprites(self.tipoTanqueActual)
        self.cargarSpritesMuerte()

        #Imagen con la que inicia el tanque
        self.image = self.animacionArriba[0]

        if self.tipoTanqueActual == TipoTanque.Inicial:
            self.velocidadMaxima = 1
            self.armadura = 1
        elif self.tipoTanqueActual == TipoTanque.Principiante:
            self.velocidadMaxima = 2
            self.armadura = 2
        elif self.tipoTanqueActual == TipoTanque.Avanzado:
            self.velocidadMaxima = 4
            self.armadura = 3
        elif self.tipoTanqueActual == TipoTanque.Final:
            self.velocidadMaxima = 3
            self.armadura = 4


        self.sonidoAparecePoder = pygame.mixer.Sound("./Recursos/Sonidos/AparecePoder.ogg")
        self.sonidoAparecePoder.set_volume(0.5)
        self.DestruirEnemigo = pygame.mixer.Sound("./Recursos/Sonidos/DestruirEnemigo.ogg")
        self.DestruirEnemigo.set_volume(0.5)


    ## Actualiza del estado del tanque
    # \details Actualiza del estado del tanque incluyendo sus actuales colisiones, , vida,, movimiento, y si esta disparando
    # \param grupoBalas: grupo con balas en juego, grupoPoderes: grupo con poderes, grupoBloques: grupo con bloques en juejo
    # grupoJugador : grupo con jugador, grupoEnemigos: grupo con enemigos en juego
    #\return no retorna valor
    def update(self, grupoBalas, grupoPoderes, grupoBloques, grupoJugador, grupoEnemigos):
        """Método para actualizar el estado de la entidad tanque"""
        probDisparo = random.randint(0, 100)

        super().update()
        self.calcularColisiones(grupoBloques, grupoJugador, grupoEnemigos)
        if self.contadorAnimacionMuerte >= len(self.animacionMuerto):
            self.kill()
            self.DestruirEnemigo.play()
            self.generarPoder(grupoPoderes)

        self.moverAutomatico()

        if(probDisparo < 2 and self.activo):
            self.disparar(grupoBalas)

    ## Carga sprites para el tanque enemigo
    # \details  Carga sprites para el tanque enemigo según el tipoTanque  y el esVarioColor
    # que define si genera poderes en el juego al ser destruido
    # \param tipoTanque: tipo de tanque
    #\return no retorna valor
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

    ## Carga sprites para el tanque enemigo cuendo muere
    # \details Carga sprites para el tanque enemigo cuendo muere
    # \param no parametro requerido
    #\return no retorna valor
    def cargarSpritesMuerte(self):
        """Método para animar la muerte de los tanques enemigos"""
        for x in range(3):
            self.animacionMuerto.append(self.crearAnimacion(32*(10+x), 0, 32, 32))

    ## Dispara balas
    # \details Carga sprites de balas disparadas por tanque
    # \param grupoBalas: grupo con las balas en juego
    #\return no retorna valor
    def disparar(self,grupoBalas):
        """Método para disparar"""
        grupoBalas.add( Bala(self.rect.x,self.rect.y,self.direccion,self.tamanio,1) )


    ## Genera un poder al ser destruido por jugador
    # \details Cuando es destruido un enemigo con true Variocolor, este genera aleatoriomente
    # un poder en algún lugar del mapa
    # \param grupoPoderes: grupo con los poderes
    #\return no retorna valor
    def generarPoder(self, grupoPoderes):
        """Método para generar poderes aleatoriamente"""

        if self.esVariocolor:
            rand_poder = random.randint(1, 6)
            x = random.randint(1, 17)
            y = random.randint(1, 17)

            if rand_poder == 1 :
                poder = PoderVidaExtra(x*self.tamanio,y*self.tamanio, self.tamanio)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

            elif rand_poder == 2 :
                poder = PoderGranada(x*self.tamanio,y*self.tamanio, self.tamanio)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

            elif rand_poder == 3 :
                poder = PoderEscudo(x*self.tamanio,y*self.tamanio, self.tamanio)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

            elif rand_poder == 4 :
                poder = PoderMejorarTanque(x*self.tamanio,y*self.tamanio, self.tamanio)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

            elif rand_poder == 5 :
                poder = PoderCongelarEnemigos(x*self.tamanio,y*self.tamanio, self.tamanio)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

            elif rand_poder == 6 :
                poder = PoderReforzarBase(x*self.tamanio,y*self.tamanio, self.tamanio)
                grupoPoderes.add(poder)
                self.sonidoAparecePoder.play()

    ## Busca todas las colisiones ocurridas con el tanque enemigo
    # \details Revisa con que colisiono el tanque enemigo y almacena en grupos de colisiones respectivos
    # \param grupoBloques: grupo con los bloques en juego, grupoJugador: grupo con el jugador , grupoEnemigos: grupo con  los otros enemigos
    #\return no retorna valor
    def calcularColisiones(self, grupoBloques, grupoJugador, grupoEnemigos):
        """"""
        #Crea una lista con las entidades que colisionan los tanques
        colisionBloques = pygame.sprite.spritecollide(self, grupoBloques, False, pygame.sprite.collide_rect)
        colisionJugador = pygame.sprite.spritecollide(self, grupoJugador, False, pygame.sprite.collide_rect)
        colisionEnemigos = pygame.sprite.spritecollide(self, grupoEnemigos, False, pygame.sprite.collide_rect)

        if colisionBloques:
            self.colisionarBloques(colisionBloques)

        if colisionJugador:
            self.colisionarTanques(colisionJugador)

        if colisionEnemigos:
            self.colisionarTanques(colisionEnemigos)

    ## Verifica si la diferencia entre dos números es pequeña
    # \details Verifica que la diferencia entre dos números sea pequeña
    # \param a, b: valores a aplicar la diferencia
    #\return retorna booleano
    def retornarDiferencia(self, a, b):
        """Método para verificar que la diferencia entre dos números sea pequeña"""

        if(a > b):
            return (a - b) <= 10
        else:
            return (b - a) <= 10

    ## Verifica la colision de enemigo con bloques
    # \details  Verifica la colision de enemigo con bloques en el juego
    # \param listaColision: lista con objetos que colisionaron
    #\return no retorna valor
    def colisionarBloques(self, listaColision):
        """Método para detectar las colisiones de tanques con bloques"""

        for entidad in listaColision:
            if(self.velocidadActualX > 0 and self.retornarDiferencia(self.rect.right, entidad.rect.left) and self.direccion == Direccion.Derecha and self != entidad):
                self.rect.right = entidad.rect.left
                self.velocidadActualX = 0

            elif(self.velocidadActualX < 0 and self.retornarDiferencia(self.rect.left, entidad.rect.right) and self.direccion == Direccion.Izquierda and self != entidad):
                self.rect.left = entidad.rect.right
                self.velocidadActualX = 0

            elif(self.velocidadActualY > 0 and self.retornarDiferencia(self.rect.bottom, entidad.rect.top) and self.direccion == Direccion.Abajo and self != entidad):
                self.rect.bottom = entidad.rect.top
                self.velocidadActualY = 0

            elif(self.velocidadActualY < 0 and self.retornarDiferencia(self.rect.top, entidad.rect.bottom) and self.direccion == Direccion.Arriba and self != entidad):
                self.rect.top = entidad.rect.bottom
                self.velocidadActualY = 0

    ## Verifica la colision de enemigo con tanques
    # \details  Verifica la colision de tanque con otros tanques en el juego
    # \param listaColision: lista con objetos que colisionaron
    #\return no retorna valor
    def colisionarTanques(self, listaColision):
        """Método para detectar las colisiones de tanques con tanques"""

        for entidad in listaColision:
            if(entidad.vivo):
                if(self.velocidadActualX > 0 and self.retornarDiferencia(self.rect.right, entidad.rect.left) and self.direccion == Direccion.Derecha and self != entidad):
                    self.rect.right = entidad.rect.left
                    self.velocidadActualX = 0

                elif(self.velocidadActualX < 0 and self.retornarDiferencia(self.rect.left, entidad.rect.right) and self.direccion == Direccion.Izquierda and self != entidad):
                    self.rect.left = entidad.rect.right
                    self.velocidadActualX = 0

                elif(self.velocidadActualY > 0 and self.retornarDiferencia(self.rect.bottom, entidad.rect.top) and self.direccion == Direccion.Abajo and self != entidad):
                    self.rect.bottom = entidad.rect.top
                    self.velocidadActualY = 0

                elif(self.velocidadActualY < 0 and self.retornarDiferencia(self.rect.top, entidad.rect.bottom) and self.direccion == Direccion.Arriba and self != entidad):
                    self.rect.top = entidad.rect.bottom
                    self.velocidadActualY = 0
