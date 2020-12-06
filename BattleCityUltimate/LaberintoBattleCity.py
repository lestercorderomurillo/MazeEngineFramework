import sys
sys.path.append('../')
from ME_Framework.ME_Controlador import ME_Controlador
from ME_Framework.ME_Laberinto import ME_Laberinto

from BattleCityUltimate.Entidades.Medalla import Medalla
from BattleCityUltimate.Entidades.DepositoMedalla import DepositoMedalla
from BattleCityUltimate.Entidades.BloqueLadrillo import BloqueLadrillo
from BattleCityUltimate.Entidades.BloqueAgua import BloqueAgua
from BattleCityUltimate.Entidades.BloqueHojas import BloqueHojas
from BattleCityUltimate.Entidades.BloqueMetalico import BloqueMetalico
from BattleCityUltimate.Entidades.BloqueIndestructible import BloqueIndestructible
from BattleCityUltimate.Entidades.TanqueEnemigo import TanqueEnemigo
from BattleCityUltimate.Entidades.TanqueJugador import TanqueJugador


import pygame, math,random

#MAPA1="./Recursos/Mapas/mapa1.data"
#MAPA2="./Recursos/Mapas/mapa2.data"
#MAPA3="./Recursos/Mapas/mapa3.data"
#MAPA4="./Recursos/Mapas/mapa4.data"
#MAPA5="./Recursos/Mapas/mapa5.data"
MAPA1="./BattleCityUltimate/Recursos/Mapas/mapa1.data"
MAPA2="./BattleCityUltimate/Recursos/Mapas/mapa2.data"
MAPA3="./BattleCityUltimate/Recursos/Mapas/mapa3.data"
MAPA4="./BattleCityUltimate/Recursos/Mapas/mapa4.data"
MAPA5="./BattleCityUltimate/Recursos/Mapas/mapa5.data"

MAP_SIZE = 18

BANDOJUGADOR = 0
BANDOENEMIGO = 1
MAX_ENEMIGOS = 12

class LaberintoBattleCity(ME_Laberinto):

    def __init__(self, taman, tamanioPantalla):
        """Constructor"""
        super().__init__(taman)
        self.grupoPoderes = pygame.sprite.Group()
        self.grupoMedallas = pygame.sprite.Group()
        self.grupoEntidadesSinColision = pygame.sprite.Group()
        self.interfaz = Interfaz(tamanioPantalla)
        self.cargarNivel()
        self.contadorGenerarEnemigos = 0

    def update(self, controlador):
        """Método para actualizar los grupos de sprites"""

        self.grupoJugador.update()
        self.grupoEnemigos.update(self.grupoArmas, self.grupoPoderes)
        self.grupoArmas.update()
        self.medallaEnemiga.update(self.tanqueJugador, self.depositoMedalla)
        self.medallaAliada.update(self.tanqueJugador, self.depositoMedalla)
        self.grupoBloques.update()
        self.grupoPoderes.update(self.tanqueJugador)
        super().update()
        self.generarEnemigos()

        
    def draw(self, controlador, pantalla):

        if(not controlador.menuAbierto):
            pantalla.fill((0, 0, 0))
            self.grupoMedallas.draw(pantalla)
            self.grupoPoderes.draw(pantalla)
            super().draw(controlador, pantalla)
            self.grupoEntidadesSinColision.draw(pantalla)
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

            if(evento.key == pygame.K_UP and self.tanqueJugador.direccion == 1):
                self.tanqueJugador.detenerse()
            if(evento.key == pygame.K_DOWN and self.tanqueJugador.direccion == 3):
                self.tanqueJugador.detenerse()
            if(evento.key == pygame.K_LEFT and self.tanqueJugador.direccion == 4):
                self.tanqueJugador.detenerse()
            if(evento.key == pygame.K_RIGHT and self.tanqueJugador.direccion == 2):
                self.tanqueJugador.detenerse()

        super().evento(controlador, evento)

    def verificarPosicion(self,x,y):
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

        rand_tanque = random.randint(0, 100)
        rand_variocolor = random.randint(0, 100)
        x, y = self.verificarPosicion(6,17)


        esVariocolor = False

        #Para que haya poca probabilidad de que sea variocolor
        if(rand_variocolor >= 0 and rand_variocolor < 60):   #Probabilidad 25/100 de ser variocolor
            esVariocolor = True

        if(     rand_tanque >= 0  and rand_tanque < 60):    #Probabilidad 60/100 de ser tipo inicial
            tanqueEnemigo = TanqueEnemigo(self.tamanio*x, self.tamanio*y, self.tamanio, esVariocolor, 1)

        elif(   rand_tanque >= 60 and rand_tanque < 80):    #Probabilidad 20/100 de ser tipo principiante
            tanqueEnemigo = TanqueEnemigo(self.tamanio*x, self.tamanio*y, self.tamanio, esVariocolor, 2)

        elif(   rand_tanque >= 80 and rand_tanque < 95):    #Probabilidad 15/100 de ser tipo avanzado
            tanqueEnemigo = TanqueEnemigo(self.tamanio*x, self.tamanio*y, self.tamanio, esVariocolor, 3)

        elif(   rand_tanque >= 95 and rand_tanque < 100):   #Probabilidad 5/100 de ser tipo final
            tanqueEnemigo = TanqueEnemigo(self.tamanio*x, self.tamanio*y, self.tamanio, esVariocolor, 4)

        else:                                               #Cualquier otro caso posible
            tanqueEnemigo = TanqueEnemigo(self.tamanio*x, self.tamanio*y, self.tamanio, esVariocolor, 1)

        return tanqueEnemigo

    def generarEnemigos(self):
        """Método para generar tanques enemigos aleatoriamente"""

        if(self.contarEnemigos() < MAX_ENEMIGOS):
            self.contadorGenerarEnemigos += 1
            if self.contadorGenerarEnemigos > 75:
                self.contadorGenerarEnemigos = 0

                self.grupoEnemigos.add(self.agregarTanqueEnemigo())

    def contarEnemigos(self):
        """Método para contar los tanques enemigos"""

        return len(self.grupoEnemigos)

    def consultarEstadoJuego(self):
        """Método para consultar el estado actual del juego"""
        
        #estado = EstadoJuego.Jugar

        #if self.tanqueJugador.sinVidas:
        #    estado = EstadoJuego.Perder
        #elif self.medallaAliada.destruida == True:
        #    estado = EstadoJuego.Perder
        #elif self.medallaEnemiga.rescadasRestantes == 0:
        #    estado = EstadoJuego.Ganar
        estado = 0
        return estado




























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
