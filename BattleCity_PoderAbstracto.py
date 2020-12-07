from ME_Entidad import ME_Entidad

class PoderAbstracto(ME_Entidad):
    """Clase abstracta para la entidad poder"""


## Constructor
# \details Constructor de la clase
# \param x , y: posicion en la pantalla de juego, tamanio: tamaño de sprite
#\return No retorna valor
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
