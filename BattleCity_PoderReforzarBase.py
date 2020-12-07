from BattleCity_PoderAbstracto import PoderAbstracto
from BattleCity_BloqueLadrillo import BloqueLadrillo
from BattleCity_BloqueMetalico import BloqueMetalico

class PoderReforzarBase(PoderAbstracto):
    """Clase para el poder de reforzar la base aliada"""

    ## Constructor
    # \details Constructor de la clase
    # \param x , y: posiciones en la pantalla de juego, tamanio: del sprite
    #\return  no retorna valor
    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*13, 32*2, 32, 32)

    ## Mejora la base del jugador
    # \details En caso de bloques sean ladrillos los mejora a bloques metálicos
    # en caso de un bloque destruido crea uno nuevo en su lugar
    # en caso de bloques dañados se reparan
    # \param grupoBloques: grupo de bloques en el juego, tamanio : tamaño del sprite para bloques
    #\return no retorna valor
    def activarPoder(self, grupoBloques, tamanio):
                izq = True
                esquinaIzq = True
                arriba = True
                esqinaDer = True
                der = True
                for bloque in grupoBloques:
                    if bloque.rect.x == 7*tamanio and bloque.rect.y == 17*tamanio:
                        if isinstance(bloque,BloqueLadrillo):
                            bloque.kill()
                            grupoBloques.add(BloqueMetalico(7*tamanio, 17*tamanio, tamanio))
                        izq = False
                    elif bloque.rect.x == 7*tamanio and bloque.rect.y == 16*tamanio:
                        if isinstance(bloque,BloqueLadrillo):
                            bloque.kill()
                            grupoBloques.add(BloqueMetalico(7*tamanio, 16*tamanio, tamanio))
                        esquinaIzq=False
                    elif bloque.rect.x == 8*tamanio and bloque.rect.y == 16*tamanio:
                        if isinstance(bloque,BloqueLadrillo):
                            bloque.kill()
                            grupoBloques.add(BloqueMetalico(8*tamanio, 16*tamanio, tamanio))
                        arriba = False
                    elif bloque.rect.x == 9*tamanio and bloque.rect.y == 16*tamanio:
                        if isinstance(bloque,BloqueLadrillo):
                            bloque.kill()
                            grupoBloques.add(BloqueMetalico(9*tamanio, 16*tamanio, tamanio))
                        esqinaDer = False
                    elif bloque.rect.x == 9*tamanio and bloque.rect.y == 17*tamanio:
                        if isinstance(bloque,BloqueLadrillo):
                            bloque.kill()
                            grupoBloques.add(BloqueMetalico(9*tamanio, 17*tamanio, tamanio))
                        der = False
                if izq:
                    grupoBloques.add(BloqueLadrillo(7*tamanio, 17*tamanio, tamanio))
                if esquinaIzq:
                    grupoBloques.add(BloqueLadrillo(7*tamanio, 16*tamanio, tamanio))
                if arriba:
                    grupoBloques.add(BloqueLadrillo(8*tamanio, 16*tamanio, tamanio))
                if esqinaDer:
                    grupoBloques.add(BloqueLadrillo(9*tamanio, 16*tamanio, tamanio))
                if der:
                    grupoBloques.add(BloqueLadrillo(9*tamanio, 17*tamanio, tamanio))
