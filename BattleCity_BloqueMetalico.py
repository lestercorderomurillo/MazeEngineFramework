## @package BloqueMetalico
#  Es uno de los tipos especiales de bloque que existen en el juego. Resiste más disparos que el bloque ladrillo antes de destruirse

##\details El bloque hereda de Bloque abstracto
from BattleCity_BloqueAbstracto import BloqueAbstracto 

class BloqueMetalico(BloqueAbstracto):
    """Clase para el bloque metálico del juego"""
## Constructor de BloqueMetalico. Recibe coordenadas y tamaño del bloque a crear
#\details Este método construye una instancia de la clase BloqueMetalico. Establece la cantidad de disparos que un BloqueMetalico recibirá antes de destruirse. También asigna al bloque metálico un sprite.    
#\param x,y y tamanio, que determinan posicion y dimensiones del bloque
#\return No retorna valor alguno   
    def __init__(self, x, y, tamanio):
 
        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*14, 32*1, 32, 32)
        self.vidas = 4


## Método que el BloqueMetalico usa para actualizar el estado de su aspecto.
#\details Si el bloque es destruido, entonces desaparece de la pantalla. Si por el contrario sólo ha recibido 2 puntos de daño, entonces cambia su aspecto para lucir con fisuras.
#\param No recibe parametros
#\return No retorna valor alguno
    def update(self):

        if self.destruido:
            self.kill()

        elif self.vidas == 2:
            self.image = self.crearAnimacion(32*15, 32*1, 32, 32)
