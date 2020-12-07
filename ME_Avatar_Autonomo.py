from ME_Avatar import ME_Avatar
from ME_Entidad import Direccion

import random

class ME_Avatar_Autonomo(ME_Avatar):
    """Clase genérica para el avatar autónomo"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego,taman: tamanio del sprite
    #\return no retorna valor
    def __init__(self, x, y, tamanio):
        """Constructor"""

        self.contadorInactividad = 0
        super().__init__(x, y, tamanio)

    ## Metodo para movimiento automático de los avatares
    # \details Genera el movimiento automático de los avatares
    # \param  no parametro requerido
    #\return no retorna valor
    def moverAutomatico(self):
        """Método para el movimiento automático de los avatares"""

        if self.vivo:
            if self.activo:

                randMuevase = random.randint(0, 100)
                randDireccion = random.randint(0, 4)

                if(randMuevase <= 30 and self.velocidadActualX == 0 and self.velocidadActualY == 0):
                    if(randDireccion == 0):
                        self.direccion = Direccion.Izquierda
                        self.velocidadActualX = -1
                        self.velocidadActualY = 0
                    elif(randDireccion == 1):
                        self.direccion = Direccion.Derecha
                        self.velocidadActualX = 1
                        self.velocidadActualY = 0
                    elif(randDireccion == 2):
                        self.direccion = Direccion.Arriba
                        self.velocidadActualY = -1
                        self.velocidadActualX = 0
                    elif(randDireccion == 3):
                        self.direccion = Direccion.Abajo
                        self.velocidadActualY = 1
                        self.velocidadActualX = 0
                elif(randMuevase == 0):
                    self.velocidadActualX = 0
                    self.velocidadActualY = 0

            elif self.contadorInactividad < 500:
                self.contadorInactividad += 1
            else:
                self.contadorInactividad = 0
                self.activo = True
