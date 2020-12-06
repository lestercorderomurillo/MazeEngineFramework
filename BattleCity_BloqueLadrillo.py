from BattleCity_BloqueAbstracto import BloqueAbstracto

class BloqueLadrillo(BloqueAbstracto):
    """Clase para el ladrillo frágil del juego"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)

        self.image = self.crearAnimacion(32*14, 32*0, 32, 32)
        self.vidas = 2


    def update(self):
    
        if self.destruido:
            self.kill()

        elif self.vidas == 1:
            self.image = self.crearAnimacion(32*15, 32*0, 32, 32)
