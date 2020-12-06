from ME_Framework.Entidad.ME_Avatar import ME_Avatar
from ME_Framework.Entidad.ME_Avatar import Direccion

class ME_Avatar_Controlable(ME_Avatar):
    """Clase genérica para el avatar controlable"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.vidas = 3
        self.teclaPresionada = False

    def moverArriba(self):
        if(not self.teclaPresionada):
            self.velocidadActualY = -1
            self.direccion = Direccion.Arriba
            self.teclaPresionada = True

    def moverAbajo(self):
        if(not self.teclaPresionada):
            self.velocidadActualY = 1
            self.direccion = Direccion.Abajo
            self.teclaPresionada = True

    def moverDerecha(self):
        if(not self.teclaPresionada):
            self.velocidadActualX = 1
            self.direccion = Direccion.Derecha
            self.teclaPresionada = True

    def moverIzquierda(self):
        if(not self.teclaPresionada):
            self.velocidadActualX = -1
            self.direccion = Direccion.Izquierda
            self.teclaPresionada = True

    def detenerse(self):
        self.teclaPresionada = False
        self.velocidadActualX = 0
        self.velocidadActualY = 0

    def update(self):
        super().update()
