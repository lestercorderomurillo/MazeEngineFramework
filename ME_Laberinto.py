import pygame

class ME_Laberinto():
    """Laberinto del framework"""

    ## Constructor
    # \details Constructor de la clase
    # \param taman: tamanio para sprites
    #\return no retorna valor
    def __init__(self,taman):

        self.tamanio=taman
        self.mapa=[]
        self.grupoJugador = pygame.sprite.Group()
        self.grupoEnemigos = pygame.sprite.Group()
        self.grupoBloques = pygame.sprite.Group()
        self.grupoArmas = pygame.sprite.Group()

    ## Carga el nivel para el inicio del juego
    # \details Carga el nivel para el inicio del juego, con base al archivo en
    # la direccion dada por parametro archivo
    # \param archivo: direccion de archivo con datos para cargar el nivel actual
    #\return no retorna valor
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

    ## Actualizar el nivel actual
    # \details Actualiza el estado del nivel actual
    # \param archivo: no parametro requerido
    #\return No return value
    def update(self):
        """"""
    ## Recibe eventos para modificar estado
    # \details Al recibir evento verifica si se inicio el juego y si esta en ejecución
    # \param controlador: controlador para la ejecucion, evento: evento pygame
    #\return No return value
    def evento(self, controlador, evento):
        """"""

        if(evento.type == pygame.QUIT):
            controlador.ejecutandoInicio = False
            controlador.ejecutandoJuego = False

    ## Dibuja los elementos del juego
    # \details  permite el despliegue de la vistas de los elementos del juego
    # \param controlador: controlador para la ejecucion, pantalla: elementos del juego seran dibujados
    # en la pantalla dada por parametro pantalla
    #\return No return value
    def draw(self, controlador, pantalla):
        """"""

        self.grupoJugador.draw(pantalla)
        self.grupoEnemigos.draw(pantalla)
        self.grupoBloques.draw(pantalla)
        self.grupoArmas.draw(pantalla)
