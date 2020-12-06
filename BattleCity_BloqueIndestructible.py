from BattleCity_BloqueAbstracto import BloqueAbstracto

class BloqueIndestructible(BloqueAbstracto):
    """Clase para el ladrillo indestructible del juego"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*14, 32*2, 32, 32)
