from BattleCityUltimate.Entidades.PoderAbstracto import PoderAbstracto

class PoderCongelarEnemigos(PoderAbstracto):
    """Clase para el poder de congelar enemigos"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio) 
        self.image = self.crearAnimacion(32*8, 32*2, 32, 32)

    def activarPoder(self, grupoEnemigos):
        for enemigo in grupoEnemigos:
            enemigo.activo = False
            enemigo.velocidadActualX = 0
            enemigo.velocidadActualY = 0
