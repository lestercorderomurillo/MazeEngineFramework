from BattleCity_BloqueAbstracto import BloqueAbstracto

class BloqueAgua(BloqueAbstracto):
    """Clase para el agua del juego"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*14, 32*4, 32, 32)
