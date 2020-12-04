from ME_Framework.Entidad.ME_Avatar import ME_Avatar
from ME_Framework.Entidad.ME_Avatar import Direccion

class ME_Avatar_Controlable(ME_Avatar):
   """Clase genérica para el avatar controlable"""

   def __init__(self, x, y, tamanio):
      """Constructor"""

      super().__init__(x, y, tamanio)
      self.vidas = 3

   def moverArriba(self):
      self.velocidadActualY = 1

   def moverAbajo(self):
      self.velocidadActualY = -1

   def moverDerecha(self):
      self.velocidadActualX = 1

   def moverIzquierda(self):
      self.velocidadActualX = -1

   def update():
      super().update()
