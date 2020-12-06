from ME_Entidad import ME_Entidad

class DepositoMedalla(ME_Entidad):
    """Clase para la entidad deposito de las medalla"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*8,32*5, 32, 32)
