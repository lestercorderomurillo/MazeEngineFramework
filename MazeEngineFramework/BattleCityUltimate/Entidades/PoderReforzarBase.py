import pygame, math

from PoderAbstracto import PoderAbstracto

class PoderReforzarBase(PoderAbstracto):
    """Clase para el poder de reforzar la base aliada"""

    def __init__(self, x, y, tamanio):
        """Constructor"""

        super().__init__(x, y, tamanio)
        self.image = self.crearAnimacion(32*13, 32*2, 32, 32)


    def activarPoder(self, grupoBloques,tamanio):
                izq = True
                esquinaIzq = True
                arriba = True
                esqinaDer = True
                der = True
                for bloque in grupoBloques:
                    if bloque.rect.x == 7*tamanio and bloque.rect.y == 17*tamanio:
                        if isinstance(bloque,BloqueLadrillo):
                            bloque.kill()
                            grupoBloques.add(BloqueMetalico(7*tamanio, 17*tamanio))
                        izq = False
                    elif bloque.rect.x == 7*tamanio and bloque.rect.y == 16*tamanio:
                        if isinstance(bloque,BloqueLadrillo):
                            bloque.kill()
                            grupoBloques.add(BloqueMetalico(7*tamanio, 16*tamanio))
                        esquinaIzq=False
                    elif bloque.rect.x == 8*tamanio and bloque.rect.y == 16*tamanio:
                        if isinstance(bloque,BloqueLadrillo):
                            bloque.kill()
                            grupoBloques.add(BloqueMetalico(8*tamanio, 16*tamanio))
                        arriba = False
                    elif bloque.rect.x == 9*tamanio and bloque.rect.y == 16*tamanio:
                        if isinstance(bloque,BloqueLadrillo):
                            bloque.kill()
                            grupoBloques.add(BloqueMetalico(9*tamanio, 16*tamanio))
                        esqinaDer = False
                    elif bloque.rect.x == 9*tamanio and bloque.rect.y == 17*tamanio:
                        if isinstance(bloque,BloqueLadrillo):
                            bloque.kill()
                            grupoBloques.add(BloqueMetalico(9*tamanio, 17*tamanio))
                        der = False
                if izq:
                    grupoBloques.add(BloqueLadrillo(7*tamanio, 17*tamanio))
                if esquinaIzq:
                    grupoBloques.add(BloqueLadrillo(7*tamanio, 16*tamanio))
                if arriba:
                    grupoBloques.add(BloqueLadrillo(8*tamanio, 16*tamanio))
                if esqinaDer:
                    grupoBloques.add(BloqueLadrillo(9*tamanio, 16*tamanio))
                if der:
                    grupoBloques.add(BloqueLadrillo(9*tamanio, 17*tamanio))
