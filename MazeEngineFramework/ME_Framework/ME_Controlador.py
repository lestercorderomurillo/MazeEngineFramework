class ME_Controlador(object):
    """description of class"""

    def iniciarPyGame(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

        pygame.init()
        pygame.mixer.init(44100, -16, 1, 512)

    def iniciarVentana(self, nombre, anchura, altura):
        self.tamanio = [anchura, altura]
        self.pantalla = pygame.display.set_mode(tamanio)

        pygame.display.set_caption(nombre)

    def __init__(self, nombre, anchura, altura):
        """Constructor"""
        iniciarPyGame()
        iniciarVentana(nombre, anchura, altura)
      
