import pygame, os, enum

class EstadoJuego(enum.IntEnum):
    """Enumeración de las posibles estado del juego"""
    Jugar   = 1
    Ganar   = 2
    Perder  = 3

class ME_Controlador():
    """Controlador del Framework"""

    ## Constructor
    # \details Constructor de la clase
    # \param taman: tamanio para sprites
    #\return No return value
    def __init__(self, nombre, anchura, altura):
        """Constructor"""
        self.iniciarPyGame()
        self.iniciarVentana(nombre, anchura, altura)
        self.estadoJuego = EstadoJuego.Jugar
        self.menu = None
        self.laberinto = None

        self.sonidoPerder = None
        self.sonidoGanar = None
        self.sonidoEmpezarJuego = None

    ## Inicia la ejecucion de pygame
    # \details Despliega la pantalla inicial
    # \param no requiere parametros
    #\return No return value
    def iniciarPyGame(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
        pygame.mixer.init(44100, -16, 1, 512)
        pygame.init()
        self.clock = pygame.time.Clock()

    ## Inicia el despliegue para la pantalla inicial para el juego
    # \details Despliega la pantalla inicial para el juego
    # \param nombre: nombre del juego, anchura, altura
    #\return No return value
    def iniciarVentana(self, nombre, anchura, altura):
        self.pantalla = pygame.display.set_mode(self.tamanioPantalla)
        pygame.display.set_caption(nombre)

        self.menuAbierto      = True
        self.ejecutandoInicio = True
        self.ejecutandoJuego  = True

    ## Ejecución del juego
    # \details Metodo que contieno lógica de ejecución del juego
    # \param no requiere parametros
    #\return No return value
    def ejecutar(self):
        self.sonidoEmpezarJuego.play()
        while(self.ejecutandoJuego):
            self.clock.tick(30)
            if(    (self.ejecutandoInicio)
                or (self.ejecutandoInicio == False and self.menuAbierto)):
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        self.ejecutandoJuego     = False
                    else:
                        self.menu.evento(self, evento)
            elif(not self.menuAbierto):
                self.laberinto.update(self)
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        self.ejecutandoJuego     = False
                    else:
                        self.laberinto.evento(self, evento)

            if self.estadoJuego == EstadoJuego.Ganar:
                self.sonidoGanar.play()
                self.menu.estadoActual = 6
                self.menuAbierto      = True
            elif self.estadoJuego == EstadoJuego.Perder:
                self.sonidoPerder.play()
                self.menu.estadoActual = 7
                self.menuAbierto      = True

            if self.estadoJuego != EstadoJuego.Jugar:
                pygame.time.delay(1000)

            self.draw()

            if self.estadoJuego != EstadoJuego.Jugar:
                pygame.time.delay(2000)
                self.estadoJuego = EstadoJuego.Jugar
                self.menuAbierto      = True
                self.ejecutandoInicio = True
                self.menu.estadoActual = 1
                self.laberinto.resetear()
        pygame.quit()

    ## Dibuja los el laberinto y el menu del juego
    # \details permite el despliegue de la vistas del laberinto y el menu
    # \param no requiere parametros
    #\return No return value
    def draw(self):
        self.laberinto.draw(self, self.pantalla)
        self.menu.draw(self, self.pantalla)
        pygame.display.flip()
