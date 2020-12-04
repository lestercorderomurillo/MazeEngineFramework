import pygame, os

class ME_Controlador():
    """Controlador del Framework"""
        
    def __init__(self, nombre, anchura, altura):
        """Constructor"""
        self.iniciarPyGame()
        self.iniciarVentana(nombre, anchura, altura)

    def iniciarPyGame(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
        pygame.mixer.init(44100, -16, 1, 512)
        pygame.init()
        self.clock = pygame.time.Clock()

    def iniciarVentana(self, nombre, anchura, altura):
        self.tamanio = [anchura, altura]
        self.pantalla = pygame.display.set_mode(self.tamanio)
        pygame.display.set_caption(nombre)

        self.menuAbierto      = True 
        self.ejecutandoInicio = True
        self.ejecutandoJuego  = True

    def ejecutar(self):
        while(self.ejecutandoJuego):
            self.clock.tick(40)
            if(    (self.ejecutandoInicio)                   
                or (self.ejecutandoInicio == False and self.menuAbierto)):
                for evento in pygame.event.get():
                    self.menu.evento(self, evento)
            elif(not self.menuAbierto):
                self.laberinto.update(self)
                for evento in pygame.event.get():
                    self.laberinto.evento(self, evento)
            self.draw()
    
    def draw(self):
        self.laberinto.draw(self, self.pantalla)
        self.menu.draw(self, self.pantalla)
        pygame.display.flip()