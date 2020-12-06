from ME_Controlador import ME_Controlador
from BattleCity_Laberinto import LaberintoBattleCity
from BattleCity_Menu import MenuBattleCity

class ControladorBattleCity(ME_Controlador):

    def __init__(self):
        """Constructor"""

        self.tamanioPantalla = [840, 720]
        self.tamanio = 40
        super().__init__("Battle City Game", self.tamanioPantalla[0], self.tamanioPantalla[1])

        self.iniciar()

    def iniciar(self):
        self.laberinto = LaberintoBattleCity(self.tamanio, self.tamanioPantalla)
        self.menu = MenuBattleCity(self.tamanioPantalla)

    def ejecutar(self):
        super().ejecutar()


def main():
    battleCity = ControladorBattleCity()
    battleCity.ejecutar()

if __name__ == "__main__":
    main()