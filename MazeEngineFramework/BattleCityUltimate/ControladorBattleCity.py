from ME_Framework import ME_Controlador

class ControladorBattleCity(ME_Controlador):

    def __init__(self):
        """Constructor"""
        super.__init__("Battle City Game", 840, 720)

        self.iniciar()
        self.update()

    def iniciar(self):
        self.laberinto = LaberintoBattleCity()
        self.ejecutandoJuego = True

    def update(self):

        ejecutandoInicio    = True
        fueraDelMenu        = False

if __name__ == "__main__":
    main()


def main():
    battleCity = ControladorBattleCity()
    battleCity.iniciar()
