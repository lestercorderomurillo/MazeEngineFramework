## @package MenuBattleCity
# Clase que engloba los métodos y atributos para que el juego posea un menú principal específico para él.


from ME_Menu import ME_Menu
from ME_Menu import Menu

import pygame

class MenuBattleCity(ME_Menu):
## Constructor de la clase MenuBattleCity, usado para crear ventanas que representen el menú del juego
#\details El constructor comienza invocando el constructor de ME_Menu. Luego, declara atributos que servirán para guardar las pantallas de cada sección del menú
#. Tales atributos se inicializan al utilizar el método pygame.transform.scale, el cual recibe el resultado de pygame.image.load para poder adaptar las pantallas del menú al tamaño
#requerido por las dimensiones que este constructor recibe por parámetro. Una vez guardadas las pantallas en los atributos, se utiliza pygame.mixer para recuperar
#efectos de sonido guardados y tenerlos a mano en forma de atributos. Asimismo, set_volume es usado para ajustar el volumen de cada efecto de sonido.. 
#\param tamanioPantalla, una dupla/vector de 2 que contiene altura y ancho de ventana.
#\return No retorna nada.
    def __init__(self, tamanioPantalla):
        """Constructor"""

        super().__init__()
        self.estadoActual = Menu.MenuPrincipal1

        self.menu1_png =        pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/Menu1.png").convert(), (tamanioPantalla[0], tamanioPantalla[1]))
        self.menu2_png =        pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/Menu2.png").convert(), (tamanioPantalla[0], tamanioPantalla[1]))
        self.menu3_png =        pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/Menu3.png").convert(), (tamanioPantalla[0], tamanioPantalla[1]))
        self.reglas_png =       pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/Reglas.png").convert(), (tamanioPantalla[0], tamanioPantalla[1]))
        self.controles_png =    pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/Controles.png").convert(), (tamanioPantalla[0], tamanioPantalla[1]))
        self.victoria_png =     pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/Victory.png").convert(), (tamanioPantalla[0], tamanioPantalla[1]))
        self.derrota_png =      pygame.transform.scale(pygame.image.load("./Recursos/Imagenes/Menu/GameOver.png").convert(), (tamanioPantalla[0], tamanioPantalla[1]))
        self.sonidoPausa = pygame.mixer.Sound("./Recursos/Sonidos/Pausa.ogg")
        self.sonidoPausa.set_volume(0.5)
        self.sonidoMoverOpcion = pygame.mixer.Sound("./Recursos/Sonidos/OpcionMenu.ogg")
        self.sonidoMoverOpcion.set_volume(0.5)
## Método usado para manejar eventos dentro de menú
#\details Método evento() reacciona a las teclas pulsadas por el usuario por mediante la comparación de evento.type con 
#alguna tecla almacenada en pygame 
#\param evento, almacena la información del evento ocurrido, y controlador
#\return No retorna valores
    def evento(self, controlador, evento):
        """"""
        if(evento.type == pygame.KEYDOWN):
            self.sonidoMoverOpcion.play()
            if(evento.key == pygame.K_DOWN):
                if(controlador.menuAbierto and controlador.ejecutandoInicio):
                    if(self.estadoActual != Menu.Reglas):
                        if(self.estadoActual != Menu.Controles):
                            if(self.estadoActual < Menu.MenuPrincipal3):
                                self.estadoActual += 1
                            else:
                                self.estadoActual = Menu.MenuPrincipal1

            elif(evento.key == pygame.K_UP):
                if(controlador.menuAbierto and controlador.ejecutandoInicio):
                    if(self.estadoActual != Menu.Reglas):
                        if(self.estadoActual != Menu.Controles):
                            if(self.estadoActual > Menu.MenuPrincipal1):
                                self.estadoActual -= 1
                            else:
                                self.estadoActual = Menu.MenuPrincipal3

            elif(evento.key == pygame.K_RETURN):
                if(controlador.menuAbierto and controlador.ejecutandoInicio):
                    if(self.estadoActual ==  Menu.MenuPrincipal1):
                        self.estadoActual = Menu.Reglas
                        controlador.menuAbierto = False
                        controlador.ejecutandoInicio = False
                    elif(self.estadoActual ==  Menu.MenuPrincipal2):
                        self.estadoActual = Menu.Controles
                    elif(self.estadoActual ==  Menu.MenuPrincipal3):
                        self.estadoActual = Menu.Reglas

            elif(evento.key == pygame.K_ESCAPE):
                if(controlador.menuAbierto and not controlador.ejecutandoInicio):
                    self.sonidoPausa.play()
                    controlador.menuAbierto = False
                elif(self.estadoActual == Menu.Controles):
                    self.estadoActual = Menu.MenuPrincipal2
                elif(self.estadoActual == Menu.Reglas):
                    self.estadoActual = Menu.MenuPrincipal3

        super().evento(controlador, evento)
## Método para dibujar y mostrar el estado actual de la pantalla de menú
#\details El método examina el el atributo estadoActual para ver  a qué pantalla de menú cambiar
#\param objeto controlador, pantalla
#\return  no hay retorno, pero sí ocurre un cambio en pantalla
    def draw(self, controlador, pantalla):
        """"""
        if(controlador.menuAbierto):
            pantalla.fill((0, 0, 0))

            if(self.estadoActual == Menu.MenuPrincipal1):
                pantalla.blit(self.menu1_png, (0, 0))
            elif(self.estadoActual == Menu.MenuPrincipal2):
                pantalla.blit(self.menu2_png, (0, 0))
            elif(self.estadoActual == Menu.MenuPrincipal3):
                pantalla.blit(self.menu3_png, (0, 0))
            elif(self.estadoActual == Menu.Controles):
                pantalla.blit(self.controles_png, (0, 0))
            elif(self.estadoActual == Menu.Reglas):
                pantalla.blit(self.reglas_png, (0, 0))
            elif(self.estadoActual == Menu.Victoria):
                pantalla.blit(self.victoria_png, (0, 0))
            elif(self.estadoActual == Menu.Derrota):
                pantalla.blit(self.derrota_png, (0, 0))
