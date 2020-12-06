from ME_Controlador import ME_Controlador
from BattleCity_Laberinto import LaberintoBattleCity
from BattleCity_Menu import MenuBattleCity
import pygame


class ControladorBattleCity(ME_Controlador):

    def __init__(self):
        """Constructor"""

        self.tamanioPantalla = [840, 720]
        self.tamanio = 40
        super().__init__("Battle City Game", self.tamanioPantalla[0], self.tamanioPantalla[1])

        self.iniciar()

        self.sonidoPerder = pygame.mixer.Sound("./Recursos/Sonidos/Perder.ogg")
        self.sonidoGanar = pygame.mixer.Sound("./Recursos/Sonidos/Ganar.ogg")
        self.sonidoEmpezarJuego = pygame.mixer.Sound("./Recursos/Sonidos/Inicio.ogg")
            
        self.sonidoPerder.set_volume(0.5)
        self.sonidoGanar.set_volume(0.5)
        self.sonidoEmpezarJuego.set_volume(0.5)

    def iniciar(self):
        self.laberinto = LaberintoBattleCity(self.tamanio, self.tamanioPantalla)
        self.menu = MenuBattleCity(self.tamanioPantalla)

    def ejecutar(self):
        super().ejecutar()


def main():
    pygame.mixer.init(44100, -16, 1, 512)
    battleCity = ControladorBattleCity()
    battleCity.ejecutar()
    pygame.mixer.quit()

if __name__ == "__main__":
    main()
