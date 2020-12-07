from ME_Entidad import ME_Entidad

import pygame, math

class ArmaMarda(ME_Entidad):
    """Clase abstracta para cualquier arma"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego,direccion: direccion del sprite ,tamanio: tamanio del sprite
    #\return no retorna valor
    def __init__(self, x, y, direccion, tamanio):
        """Constructor"""
        super().__init__(x, y, tamanio)

        self.animacionArriba     = []
        self.animacionDerecha    = []
        self.animacionAbajo      = []
        self.animacionIzquierda  = []
        self.animacionExplosion  = []
        self.imagenAnimacion = 0
        self.destruida = False
        self.ataque = 1
        self.direccion = direccion

    ## Actualizacion del estado del arma
    # \details actualización del estado del arma
    # \param  no parametro requerido
    #\return no retorna valor
    def update(self):
        if self.destruida:
            self.destruirArma()

    ## Se destruye a si mismo
    # \details se destruye a si mismo
    # \param  no parametro requerido
    #\return no retorna valor
    def destruirArma(self):
        """Método para destruir arma"""
        self.kill()
