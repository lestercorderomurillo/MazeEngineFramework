from ME_Menu import ME_Menu
from ME_Menu import Menu

import pygame

class MenuBattleCity(ME_Menu):

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
