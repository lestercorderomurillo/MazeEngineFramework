from ME_Framework.Entidad.ME_Entidad import ME_Entidad
import pygame, math

class ArmaMarda(ME_Entidad):
    """Clase abstracta para cualquier arma"""
    
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

    def update(self):
        if self.destruida:
            self.destruirArma()

    def destruirArma(self):
        """Método para destruir arma"""
        self.kill()
