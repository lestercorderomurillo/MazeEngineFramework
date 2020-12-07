from BattleCity_PoderAbstracto import PoderAbstracto

class PoderGranada(PoderAbstracto):
    """Clase para el poder de granada"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego, tamanio: del sprite
    #\return no retorna valor
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*9, 32*2, 32, 32)

    ## Detiene el movimiento  de los tanques enemigos
    # \details Itera por todos los enemigos setea su velocidad a 0 y les quita la acciones de disparar
    # \param jugador: avatar del jugador grupoEnemigos: grupo de tanque enemigos
    #\return no retorna valor
    def activarPoder(self, jugador, grupoEnemigos):
        for tanque in grupoEnemigos:
            tanque.esVariocolor = False
            tanque.vivo = False
            if tanque.tipoTanqueActual == 1:
                jugador.puntuacion += 100
            elif tanque.tipoTanqueActual == 2:
                jugador.puntuacion += 200
            elif tanque.tipoTanqueActual == 3:
                jugador.puntuacion += 300
            elif tanque.tipoTanqueActual == 4:
                jugador.puntuacion += 400
