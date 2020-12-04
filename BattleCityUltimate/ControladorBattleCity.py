import sys
sys.path.append('../')

from ME_Framework.ME_Controlador import ME_Controlador
from BattleCityUltimate.LaberintoBattleCity import LaberintoBattleCity
from BattleCityUltimate.MenuBattleCity import MenuBattleCity

class ControladorBattleCity(ME_Controlador):

    def __init__(self):
        """Constructor"""

        self.tamanio = [840, 720]
        super().__init__("Battle City Game", self.tamanio[0], self.tamanio[1])

        self.iniciar()

    def iniciar(self):
        self.laberinto = LaberintoBattleCity(self.tamanio)
        self.menu = MenuBattleCity(self.tamanio)

def main():
    battleCity = ControladorBattleCity()
    battleCity.iniciar()
    battleCity.ejecutar()

if __name__ == "__main__":
    main()