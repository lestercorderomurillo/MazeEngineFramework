from BattleCity_BloqueAbstracto import BloqueAbstracto

class BloqueHojas(BloqueAbstracto):
    """Clase para las hojas del juego"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*14, 32*3, 32, 32)
