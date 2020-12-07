from BattleCity_PoderAbstracto import PoderAbstracto

class PoderCongelarEnemigos(PoderAbstracto):
    """Clase para el poder de congelar enemigos"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego, tamanio: del sprite
    #\return No retorna valor
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*8, 32*2, 32, 32)


    ## Detiene el movimiento  de los tanques enemigos
    # \details Itera por todos los enemigos setea su velocidad a 0 y les quita la acciones de disparar
    # \param grupoEnemigos: grupo de tanque enemigos
    #\return No retorna valor
    def activarPoder(self, grupoEnemigos):
        for enemigo in grupoEnemigos:
            enemigo.activo = False
            enemigo.velocidadActualX = 0
            enemigo.velocidadActualY = 0
