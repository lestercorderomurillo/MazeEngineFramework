from ME_Avatar import ME_Avatar
from ME_Entidad import Direccion

class ME_Avatar_Controlable(ME_Avatar):
    """Clase genérica para el avatar controlable"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego,taman: tamanio del sprite
    #\return no retorna valor
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.vidas = 3
        self.teclaPresionada = False

    ## Metodo para movimiento hacia arriba del avatar
    # \details Genera el movimiento movimiento hacia arriba del avatar
    # \param  no parametro requerido
    #\return no retorna valor
    def moverArriba(self):
        if(not self.teclaPresionada):
            self.velocidadActualY = -1
            self.direccion = Direccion.Arriba
            self.teclaPresionada = True

    ## Metodo para movimiento hacia abajo del avatar
    # \details Genera el movimiento movimiento hacia abajo del avatar
    # \param  no parametro requerido
    #\return no retorna valor
    def moverAbajo(self):
        if(not self.teclaPresionada):
            self.velocidadActualY = 1
            self.direccion = Direccion.Abajo
            self.teclaPresionada = True

    ## Metodo para movimiento hacia la derecha del avatar
    # \details Genera el movimiento movimiento hacia la derecha  del avatar
    # \param  no parametro requerido
    #\return no retorna valor
    def moverDerecha(self):
        if(not self.teclaPresionada):
            self.velocidadActualX = 1
            self.direccion = Direccion.Derecha
            self.teclaPresionada = True

    ## Metodo para movimiento hacia la izquierda del avatar
    # \details Genera el movimiento movimiento haciala izquierdadel avatar
    # \param  no parametro requerido
    #\return no retorna valor
    def moverIzquierda(self):
        if(not self.teclaPresionada):
            self.velocidadActualX = -1
            self.direccion = Direccion.Izquierda
            self.teclaPresionada = True

    ## Metodo para que avatar detenta su movimiento
    # \details detiene movimiento del avatar
    # \param  no parametro requerido
    #\return no retorna valor
    def detenerse(self):
        self.teclaPresionada = False
        self.velocidadActualX = 0
        self.velocidadActualY = 0

    ## Actualizacion del estado del avatar
    # \details actualización del estado del avatar
    # \param  no parametro requerido
    #\return no retorna valor
    def update(self):
        super().update()
