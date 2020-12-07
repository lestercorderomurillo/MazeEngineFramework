from BattleCity_PoderAbstracto import PoderAbstracto

class PoderVidaExtra(PoderAbstracto):
    """Clase para el poder de vida extra"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego, tamanio: del sprite
    #\return No return value
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*10, 32*2, 32, 32)

    ## Jugador obtiene una vida extra
    # \details En caso de ser morir, aumenta por una las veces que puede revivir
    # \param jugador: avatar del jugador
    #\return no retorna valor
    def activarPoder(self, jugador):
        jugador.vidas += 1
