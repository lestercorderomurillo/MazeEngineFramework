from ME_Controlador import ME_Controlador
from ME_Laberinto import ME_Laberinto
from ME_Entidad import Direccion

from BattleCity_Interfaz import Interfaz

from BattleCity_Medalla import Medalla
from BattleCity_DepositoMedalla import DepositoMedalla
from BattleCity_BloqueLadrillo import BloqueLadrillo
from BattleCity_BloqueAgua import BloqueAgua
from BattleCity_BloqueHojas import BloqueHojas
from BattleCity_BloqueMetalico import BloqueMetalico
from BattleCity_BloqueIndestructible import BloqueIndestructible
from BattleCity_TanqueEnemigo import TanqueEnemigo
from BattleCity_TanqueJugador import TanqueJugador

from BattleCity_PoderVidaExtra import PoderVidaExtra
from BattleCity_PoderGranada import PoderGranada
from BattleCity_PoderEscudo import PoderEscudo
from BattleCity_PoderMejorarTanque import PoderMejorarTanque
from BattleCity_PoderCongelarEnemigos import PoderCongelarEnemigos
from BattleCity_PoderReforzarBase import PoderReforzarBase

import pygame, random, enum

MAPA1 = "./Recursos/Mapas/mapa1.data"
MAPA2 = "./Recursos/Mapas/mapa2.data"
MAPA3 = "./Recursos/Mapas/mapa3.data"
MAPA4 = "./Recursos/Mapas/mapa4.data"
MAPA5 = "./Recursos/Mapas/mapa5.data"

MAP_SIZE = 18

BANDOJUGADOR = 0
BANDOENEMIGO = 1
MAX_ENEMIGOS = 12

class EstadoJuego(enum.IntEnum):
    """Enumeración de las posibles estado del juego"""
    Jugar   = 1
    Ganar   = 2
    Perder  = 3

class LaberintoBattleCity(ME_Laberinto):

    def __init__(self, taman, tamanioPantalla):
        """Constructor"""
        super().__init__(taman)
        self.tamanioPantalla = tamanioPantalla
        self.grupoPoderes = pygame.sprite.Group()
        self.grupoMedallas = pygame.sprite.Group()
        self.grupoEntidadesSinColision = pygame.sprite.Group()
        self.interfaz = Interfaz(tamanioPantalla)
        self.cargarNivel()
        self.contadorGenerarEnemigos = 0
        self.sonidoPausa = pygame.mixer.Sound("./Recursos/Sonidos/Pausa.ogg")
        self.sonidoAgarraPoder = pygame.mixer.Sound("./Recursos/Sonidos/AgarrarPoder.ogg")
        self.sonidoPausa.set_volume(0.5)
        self.sonidoPausa.set_volume(0.5)
        
    def update(self, controlador):
        """Método para actualizar los grupos de sprites"""
        controlador.estadoJuego = self.consultarEstadoJuego()
        
        self.grupoJugador.update(self.grupoBloques, self.grupoJugador, self.grupoEnemigos)
        self.grupoEnemigos.update(self.grupoArmas, self.grupoPoderes, self.grupoBloques, self.grupoJugador, self.grupoEnemigos)
        self.grupoArmas.update(self.grupoBloques, self.grupoJugador, self.grupoEnemigos, self.grupoArmas, self.grupoMedallas)
        self.medallaEnemiga.update(self.tanqueJugador, self.depositoMedalla)
        self.medallaAliada.update(self.tanqueJugador, self.depositoMedalla)
        self.grupoBloques.update()
        self.recolectarPoder()
        super().update()
        self.generarEnemigos()

    def recolectarPoder(self):
        """"""
        colisionJugadorConPoder = pygame.sprite.spritecollide(self.tanqueJugador, self.grupoPoderes, True, pygame.sprite.collide_rect)
        
        if(colisionJugadorConPoder):
            self.sonidoAgarraPoder.play()
            for poder in colisionJugadorConPoder:
                if( isinstance(poder, PoderCongelarEnemigos)):
                    poder.activarPoder(self.grupoEnemigos)
                elif(isinstance(poder, PoderEscudo)):
                    poder.activarPoder(self.tanqueJugador)
                elif(isinstance(poder, PoderGranada)):
                    poder.activarPoder(self.tanqueJugador, self.grupoEnemigos)
                elif(isinstance(poder, PoderMejorarTanque)):
                    poder.activarPoder(self.tanqueJugador)
                elif(isinstance(poder, PoderReforzarBase)):
                    poder.activarPoder(self.grupoBloques, self.tamanio)
                elif(isinstance(poder, PoderVidaExtra)):
                    poder.activarPoder(self.tanqueJugador)

    def draw(self, controlador, pantalla):

        if(not controlador.menuAbierto):
            pantalla.fill((0, 0, 0))
            self.grupoMedallas.draw(pantalla)
            super().draw(controlador, pantalla)
            self.grupoEntidadesSinColision.draw(pantalla)
            self.grupoPoderes.draw(pantalla)
            self.interfaz.draw(pantalla, self)


    def cargarNivel(self):
        self.nivel = random.randint(1, 5)

        if(self.nivel == 1):
            archivo = MAPA1
        elif(self.nivel == 2):
            archivo = MAPA2
        elif(self.nivel == 3):
            archivo = MAPA3
        elif(self.nivel == 4):
            archivo = MAPA4
        elif(self.nivel == 5):
            archivo = MAPA5

        datos = open(archivo, "r")
        y = 0
        for linea in datos:
            lista = linea.split('.')
            x = 0
           
            for elemento in lista:
         
                if (elemento == '1'):
                    self.grupoBloques.add(BloqueLadrillo(x*self.tamanio, y*self.tamanio, self.tamanio))
                if (elemento == '2'):
                    self.grupoBloques.add(BloqueMetalico(x*self.tamanio, y*self.tamanio, self.tamanio))
                if (elemento == '3'):
                    self.grupoEntidadesSinColision.add(BloqueHojas(x*self.tamanio, y*self.tamanio, self.tamanio))
                if (elemento == '4'):
                    self.grupoBloques.add(BloqueAgua(x*self.tamanio, y*self.tamanio, self.tamanio))
                if (elemento == '5'):
                    self.grupoBloques.add(BloqueIndestructible(x*self.tamanio, y*self.tamanio, self.tamanio))
                if (elemento == 'E'):
                    self.medallaEnemiga = Medalla(x*self.tamanio, y*self.tamanio, self.tamanio, BANDOENEMIGO)
                if (elemento == 'D'):
                    self.depositoMedalla = DepositoMedalla(x*self.tamanio, y*self.tamanio, self.tamanio)
                if (elemento == 'A'):
                    self.medallaAliada = Medalla(x*self.tamanio, y*self.tamanio, self.tamanio, BANDOJUGADOR)
                if (elemento == 'J'):
                    self.tanqueJugador = TanqueJugador(x*self.tamanio, y*self.tamanio, self.tamanio)

                x += 1
            y += 1

        #Agregue al final
        self.grupoMedallas.add(self.medallaEnemiga)
        self.grupoMedallas.add(self.medallaAliada)
        self.grupoJugador.add(self.tanqueJugador)
        self.grupoEntidadesSinColision.add(self.depositoMedalla)

        #Crea muros alrededor para que los tanques no puedan salir del mapa
        for x in range(-1, MAP_SIZE+1):
            for y in range(-1, MAP_SIZE+1):
                if ((x == -1 or x == MAP_SIZE) or (y == -1 or y == MAP_SIZE)):
                    self.grupoBloques.add(BloqueIndestructible( self.tamanio*x , self.tamanio*y, self.tamanio))
        
        super().cargarNivel(archivo)


    def evento(self, controlador, evento):
        """"""
        if(evento.type == pygame.KEYDOWN):

            if(evento.key == pygame.K_ESCAPE):
                controlador.menuAbierto = True
                self.sonidoPausa.play()
                self.tanqueJugador.velocidadActualX = 0
                self.tanqueJugador.velocidadActualY = 0
            elif(evento.key == pygame.K_SPACE):
                self.tanqueJugador.disparar(self.grupoArmas)
            elif(evento.key == pygame.K_UP):
                self.tanqueJugador.moverArriba()
            elif(evento.key == pygame.K_DOWN):
                self.tanqueJugador.moverAbajo()
            elif(evento.key == pygame.K_LEFT):
                self.tanqueJugador.moverIzquierda()
            elif(evento.key == pygame.K_RIGHT):
                self.tanqueJugador.moverDerecha()

        elif(evento.type == pygame.KEYUP):

            if(evento.key == pygame.K_UP and self.tanqueJugador.direccion == Direccion.Arriba):
                self.tanqueJugador.detenerse()
            if(evento.key == pygame.K_DOWN and self.tanqueJugador.direccion == Direccion.Abajo):
                self.tanqueJugador.detenerse()
            if(evento.key == pygame.K_LEFT and self.tanqueJugador.direccion == Direccion.Izquierda):
                self.tanqueJugador.detenerse()
            if(evento.key == pygame.K_RIGHT and self.tanqueJugador.direccion == Direccion.Derecha):
                self.tanqueJugador.detenerse()

        super().evento(controlador, evento)

    def verificarPosicion(self, x, y):
        """Método para verificar que la posición para generar un tanque sea válida"""

        posicionValida = False

        while posicionValida == False:
            randX = random.randint(0, x)
            randY = random.randint(0, y)

            if(self.mapa[randX][randY] == "-"):
                posicionValida = True

        return (randY, randX)

    def agregarTanqueEnemigo(self):
        """Método para retornar un tanque enemigo aleatorio"""

        randTanque = random.randint(0, 100)
        randVariocolor = random.randint(0, 100)
        x, y = self.verificarPosicion(6,17)


        esVariocolor = False

        #Para que haya poca probabilidad de que sea variocolor
        if(randVariocolor >= 0 and randVariocolor < 60):   #Probabilidad 25/100 de ser variocolor
            esVariocolor = True

        if(     randTanque >= 0  and randTanque < 60):    #Probabilidad 60/100 de ser tipo inicial
            tanqueEnemigo = TanqueEnemigo(self.tamanio*x, self.tamanio*y, self.tamanio, esVariocolor, 1)

        elif(   randTanque >= 60 and randTanque < 80):    #Probabilidad 20/100 de ser tipo principiante
            tanqueEnemigo = TanqueEnemigo(self.tamanio*x, self.tamanio*y, self.tamanio, esVariocolor, 2)

        elif(   randTanque >= 80 and randTanque < 95):    #Probabilidad 15/100 de ser tipo avanzado
            tanqueEnemigo = TanqueEnemigo(self.tamanio*x, self.tamanio*y, self.tamanio, esVariocolor, 3)

        elif(   randTanque >= 95 and randTanque < 100):   #Probabilidad 5/100 de ser tipo final
            tanqueEnemigo = TanqueEnemigo(self.tamanio*x, self.tamanio*y, self.tamanio, esVariocolor, 4)

        else:                                               #Cualquier otro caso posible
            tanqueEnemigo = TanqueEnemigo(self.tamanio*x, self.tamanio*y, self.tamanio, esVariocolor, 1)

        return tanqueEnemigo

    def generarEnemigos(self):
        """Método para generar tanques enemigos aleatoriamente"""

        if(len(self.grupoEnemigos) < MAX_ENEMIGOS):
            self.contadorGenerarEnemigos += 1
            if self.contadorGenerarEnemigos > 75:
                self.contadorGenerarEnemigos = 0

                self.grupoEnemigos.add(self.agregarTanqueEnemigo())

    def consultarEstadoJuego(self):
        """Método para consultar el estado actual del juego"""
        
        estado = EstadoJuego.Jugar

        if self.tanqueJugador.vidas == 0:
            estado = EstadoJuego.Perder
        elif self.medallaAliada.destruida == True:
            estado = EstadoJuego.Perder
        elif self.medallaEnemiga.rescadasRestantes <= 0:
            estado = EstadoJuego.Ganar
        return estado

    def resetear(self):
        """Método para reiniciar el laberinto"""

        self.__init__(self.tamanio ,self.tamanioPantalla)
