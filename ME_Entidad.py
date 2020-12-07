import enum, pygame

class Direccion(enum.IntEnum):
    """Enumeración de las direcciones posibles para los avatares"""
    Arriba    = 1
    Derecha   = 2
    Abajo     = 3
    Izquierda = 4

class Bando(enum.IntEnum):
    """Enumeración de los posibles bandos"""
    Aliado  = 0
    Enemigo = 1

class ME_Entidad(pygame.sprite.Sprite):
    """Clase genérica para las entidades del juego"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego,,taman: tamanio del sprite
    #\return no retorna valor
    def __init__(self, x, y, taman):
        """Constructor"""

        super().__init__()
        self.cargarSprite("./Recursos/Imagenes/Sprites/Sprites.png")
        self.tamanio = taman
        self.rect = pygame.Rect(x, y, self.tamanio, self.tamanio)
        self.rect.x = x
        self.rect.y = y

    ## Carga sprites
    # \details  Carga sprites para que se vean en la pantalla
    # \param nombreArchivo: nombre del archivo del que se cargara el sprite
    #\return no retorna valor
    def cargarSprite(self, nombreArchivo):
        """Método para cargar el sprite a utilizar"""

        self.spriteSheet = pygame.image.load(nombreArchivo).convert()

    ## Carga sprites para que realize una animación
    # \details  Carga sprites para que se actualizen los objetos actuales
    # \param x, y: posiciones en la pantalla , anchura: ancho del sprite, altura: alto del sprite
    #\return actualizacion de sprite
    def crearAnimacion(self, x, y, anchura, altura ):
        """Método para seleccionar cierto componente dentro del sprite"""

        temp = pygame.Surface([anchura, altura]).convert()
        temp.blit(self.spriteSheet, (0 , 0) , (x, y, anchura, altura))
        temp.set_colorkey((0, 0, 0))
        temp = pygame.transform.scale(temp, (self.tamanio, self.tamanio))

        return temp
