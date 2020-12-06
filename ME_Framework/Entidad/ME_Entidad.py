import enum, pygame

class ME_Entidad(pygame.sprite.Sprite):
    """Clase genérica para las entidades del juego"""

    def __init__(self, x, y, taman):
        """Constructor"""
       # self.cargarSprite("./Recursos/Imagenes/Sprites/Sprites.png")
        super().__init__()
        self.cargarSprite("./BattleCityUltimate/Recursos/Imagenes/Sprites/Sprites.png")
        self.tamanio = taman
        self.rect = pygame.Rect(x, y, self.tamanio, self.tamanio)
        self.rect.x = x
        self.rect.y = y

    def cargarSprite(self, nombreArchivo):
        """Método para cargar el sprite a utilizar"""

        self.spriteSheet = pygame.image.load(nombreArchivo).convert()

    def crearAnimacion(self, x, y, anchura, altura ):
        """Método para seleccionar cierto componente dentro del sprite"""

        temp = pygame.Surface([anchura, altura]).convert()
        temp.blit(self.spriteSheet, (0 , 0) , (x, y, anchura, altura))
        temp.set_colorkey((0,0,0))
        temp = pygame.transform.scale(temp, (self.tamanio, self.tamanio))

        return temp
