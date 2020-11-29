class Entidad(pygame.sprite.Sprite):
    """Clase base para el control de entidades del juego"""

    def __init__(self, x, y,tamanio):
        """Constructor"""

        super().__init__()

	self.tamanio = tamanio
        self.rect = pygame.Rect(x, y, self.tamanio, self.tamanio)
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = 0
        self.velocidad_y = 0

    def cargarSprite(self, nombreArchivo):
        """Método para cargar el sprite a utilizar"""

        self.spriteSheet = pygame.image.load(nombreArchivo).convert()

    def crearAnimacion(self, x, y, anchura, altura ):
        """Método para seleccionar cierto componente dentro del sprite"""

        temp = pygame.Surface([anchura, altura]).convert()
        temp.blit(self.spriteSheet, (0 , 0) , (x, y, anchura, altura))
        temp.set_colorkey(Constantes.NEGRO)
        temp = pygame.transform.scale(temp, (self.tamanio, self.tamanio))

        return temp