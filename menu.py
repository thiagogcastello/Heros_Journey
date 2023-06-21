import pygame
from pygame.locals import *

pygame.init()


def mostrar_menu_principal(medidas_pantalla):

    pantalla = pygame.display.set_mode(medidas_pantalla)
    pygame.display.set_caption("Hero's Journey")
    clock = pygame.time.Clock()

    ruta_fuente = 'Heros_journey\\recursos\Planes_ValMore.ttf'
    
    #tamaño de los botones
    tamaño_fuente_botones = 46
    ancho_boton = 100
    alto_boton = 30
    separacion_botones = 50
    posicion_x = (medidas_pantalla[0] - ancho_boton) // 2
    posicion_1 = ((medidas_pantalla[1] - (alto_boton + separacion_botones) * 3) // 2) + separacion_botones * 3
    posicion_2 = posicion_1 + alto_boton + separacion_botones
    posicion_3 = posicion_2 + alto_boton +separacion_botones
    
    #musica
    pygame.mixer.music.load("Heros_journey\\recursos\sonidos\Adventure.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)

    #fondo en movimiento
    scroll = 0
    bg_images = []
    for i in range(2,6):
        bg_image = pygame.image.load(f"Heros_journey\\recursos\menu_principal\layers\\{i}.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, medidas_pantalla)
        bg_images.append(bg_image)

    fondo_base = pygame.image.load("Heros_journey\\recursos\menu_principal\layers\\1.png").convert_alpha()
    fondo_base = pygame.transform.scale(fondo_base, medidas_pantalla)

    #mousse
    new_mousse = pygame.image.load("Heros_journey\\recursos\mouse.png")
    new_mousse = pygame.transform.scale(new_mousse,(30,30))

    #tituol
    tamano_fuente = 200
    crecimiento = 1

    pygame.mouse.set_visible(False)

    running = True
    while running:

        clock.tick(60)

        #fondo
        pantalla.blit(fondo_base,(0,0))

        for x in range(10000):
            speed = 1
            for i in bg_images:
                pantalla.blit(i,((x * medidas_pantalla[0]) - scroll * speed, 0))
                speed += 0.3
            
        scroll += 5

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if boton_1.collidepoint(mouse_pos):
                    tamaño_fuente_botones = 66
                    return "nivel_1"
                if boton_2.collidepoint(mouse_pos):
                    return "leaderboards"
                if boton_3.collidepoint(mouse_pos):
                    return "exit"
                

        #boton 1
        boton_1 = pygame.Rect(posicion_x, posicion_1, ancho_boton, alto_boton)
        if boton_1.collidepoint(mouse_pos):
            tamaño_fuente_botones = 66
        else:
            tamaño_fuente_botones = 45
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_botones)
        texto = fuente.render("Play", True, (255, 255, 255))
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_1 + alto_boton // 2))
        pantalla.blit(texto, text_rect)

        #boton 2
        boton_2 = pygame.Rect(posicion_x - 100, posicion_2, ancho_boton * 3, alto_boton)
        if boton_2.collidepoint(mouse_pos):
            tamaño_fuente_botones = 66
        else:
            tamaño_fuente_botones = 45
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_botones)
        texto = fuente.render("Leaderboards", True, (255, 255, 255))
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_2 + alto_boton // 2))
        pantalla.blit(texto, text_rect)

        #boton 3
        boton_3 = pygame.Rect(posicion_x, posicion_3, ancho_boton, alto_boton)
        if boton_3.collidepoint(mouse_pos):
            tamaño_fuente_botones = 66
        else:
            tamaño_fuente_botones = 45
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_botones)
        texto = fuente.render("Exit", True, (255, 255, 255))
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_3 + alto_boton // 2))
        pantalla.blit(texto, text_rect)


        #titulo
        fuente = pygame.font.Font(ruta_fuente, tamano_fuente)
        titulo = fuente.render("Heros Journey", True, ("Black"))
        titulo_rect = titulo.get_rect(center=(medidas_pantalla[0] // 2, medidas_pantalla[1] // 4))
        pantalla.blit(titulo, titulo_rect)

        fuente = pygame.font.Font(ruta_fuente, 25)
        texto = fuente.render("Todos los derechos reservados.", True, (255, 255, 255))
        pantalla.blit(texto, (0, medidas_pantalla[1] - 25))

        tamano_fuente += crecimiento

        # Invierte la dirección del cambio de tamaño si se alcanza un límite
        if tamano_fuente >= 210 or tamano_fuente <= 190:
            crecimiento = -crecimiento




        #mouse
        pos = pygame.mouse.get_pos()
        pantalla.blit(new_mousse, pos)

        pygame.display.update()
        

    pygame.quit()
