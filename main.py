import pygame
from menu import *
from pantalla_final import *
from nivel import *
from leaderborads import * 

def main():
    pygame.init()

    #PANTALLA
    ancho_pantalla = 1800
    alto_pantalla = 900
    medidas_pantalla = (ancho_pantalla, alto_pantalla)
    pantalla = pygame.display.set_mode(medidas_pantalla)

    estado = "menu_principal"
    puntaje = {}

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if estado == "menu_principal":
            estado = mostrar_menu_principal(medidas_pantalla)
        elif estado == "nivel_1":
            estado, puntaje = nivel_1()
            if estado == "pantalla_puntaje":
                estado = mostrar_pantalla_final(medidas_pantalla, puntaje)
        elif estado == "leaderboards":
            estado = leaderbord(medidas_pantalla)
        elif estado == "exit":
            running = False


    pygame.quit()

if __name__ == "__main__":
    main()