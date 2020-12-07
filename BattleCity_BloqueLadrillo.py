##@package BloqueLadrillo
# Clase para el ladrillo frágil del juego

##\details El bloque hereda de Bloque abstracto
from BattleCity_BloqueAbstracto import BloqueAbstracto

class BloqueLadrillo(BloqueAbstracto):

## Constructor de BloqueLadrillo. Recibe coordenadas y tamaño del bloque a crear 
#\param x,y y tamanio, que determinan posicion y dimensiones del bloque
#\details Este método construye una instancia de la clase BloqueLadrillo. Establece la cantidad de disparos que un BloqueLadrillo recibirá antes de destruirse. También asigna al bloque un sprite.   
#\return No retorna valor alguno
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)

        self.image = self.crearAnimacion(32*14, 32*0, 32, 32)
        self.vidas = 2

## Método que el BloqueLadrillo usa para actualizar el estado de su aspecto.
#\param No recibe parametros
#\details Si el bloque es destruido, entonces desaparece de la pantalla. Si por el contrario sólo ha recibido 1 punto de daño, entonces cambia su aspecto para lucir con fisuras.
#\return No retorna valor alguno
    def update(self):
    
        if self.destruido:
            self.kill()

        elif self.vidas == 1:
            self.image = self.crearAnimacion(32*15, 32*0, 32, 32)
