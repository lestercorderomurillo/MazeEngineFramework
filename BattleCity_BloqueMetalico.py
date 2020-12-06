from BattleCity_BloqueAbstracto import BloqueAbstracto 

class BloqueMetalico(BloqueAbstracto):
    """Clase para el bloque metálico del juego"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*14, 32*1, 32, 32)
        self.vidas = 4


    def update(self):

        if self.destruido:
            self.kill()

        elif self.vidas == 2:
            self.image = self.crearAnimacion(32*15, 32*1, 32, 32)
