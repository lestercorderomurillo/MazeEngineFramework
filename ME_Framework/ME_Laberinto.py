import pygame


class ME_Laberinto():
    """Laberinto del framework"""
    def __init__(self,taman):

        self.tamanio=taman
        self.mapa=[]
        self.grupoJugador = pygame.sprite.Group()
        self.grupoEnemigos = pygame.sprite.Group()
        self.grupoBloques = pygame.sprite.Group()
        self.grupoArmas = pygame.sprite.Group()

    def cargarNivel(self, archivo):
        datos = open(archivo, "r")
        y = 0
        for linea in datos:
            lista = linea.split('.')
            x = 0 
            linea = []
            for elemento in lista:
                linea.append(elemento)
                x += 1
            self.mapa.append(linea)
            y += 1

        #Agregue al final


    def update(self):
        """"""

    def evento(self, controlador, evento):
        """"""

        if(evento.type == pygame.QUIT):
            controlador.ejecutandoInicio = False
            controlador.ejecutandoJuego = False

    def draw(self, controlador, pantalla):
        """"""

        self.grupoJugador.draw(pantalla)
        self.grupoEnemigos.draw(pantalla)
        self.grupoBloques.draw(pantalla)
        self.grupoArmas.draw(pantalla)

    def reset(self):
        """Método para reiniciar el nivel"""

        self.__init__()
    
