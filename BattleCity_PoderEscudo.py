from BattleCity_PoderAbstracto import PoderAbstracto

class PoderEscudo(PoderAbstracto):
    """Clase para el poder de granada"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego, tamanio: del sprite
    #\return No retorna valor
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*12, 32*2, 32, 32)

    ## Aumenta la armadura del tanque
    # \details Aumenta la armadura del jugador que al defender de un disparo disminuye por uno
    # \param grupoEnemigos: grupo con el jugador
    #\return No retorna valor
    def activarPoder(self, jugador):
        jugador.armadura += 1
