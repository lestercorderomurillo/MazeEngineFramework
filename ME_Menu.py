import pygame, enum

class Menu(enum.IntEnum):
    """Enumeración de los estados del menu principal"""

    MenuPrincipal1  = 1
    MenuPrincipal2  = 2
    MenuPrincipal3  = 3
    Controles       = 4
    Reglas          = 5
    Victoria        = 6
    Derrota         = 7

class ME_Menu():
    """description of class"""

    ## Constructor
    # \details Constructor de la clase
    # \param No parametros requeridos
    #\return No return value
    def __init__(self):
        """Constructor"""

    ## Recibe eventos para modificar estado
    # \details Al recibir evento verifica si se inicio el juego y si esta en ejecución
    # \param controlador: controlador para la ejecucion, evento: evento pygame
    #\return No return value
    def evento(self, controlador, evento):
        """"""

        if(evento.type == pygame.QUIT):
            controlador.ejecutandoInicio = False
            controlador.ejecutandoJuego = False
