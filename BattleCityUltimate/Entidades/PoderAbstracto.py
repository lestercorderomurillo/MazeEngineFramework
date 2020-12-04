from ME_Framework.Entidad.ME_Entidad import ME_Entidad

class PoderAbstracto(ME_Entidad):
    """Clase abstracta para la entidad poder"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio) 
