import pygame
from base_datos import *

pygame.init()

def leaderbord(medidas_pantalla):

    pantalla = pygame.display.set_mode(medidas_pantalla)
    pygame.display.set_caption("Hero's Journey")
    clock = pygame.time.Clock()

    #musica
    pygame.mixer.music.load("Heros_journey\\recursos\sonidos\Adventure.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.0)

    #mousse
    new_mousse = pygame.image.load("Heros_journey\\recursos\mouse.png")
    new_mousse = pygame.transform.scale(new_mousse,(30,30))

    pygame.mouse.set_visible(False)

    fondo_base = pygame.image.load("Heros_journey\\recursos\origbig.png")
    fondo_base = pygame.transform.scale(fondo_base, medidas_pantalla)

    #scores
    puntajes = buscar_top_10_bd()

    ruta_fuente = 'Heros_journey\\recursos\Planes_ValMore.ttf'

    #medallas
    medidas_medallas = (30,30)
    gold_medal = pygame.image.load("Heros_journey\\recursos\medallas\medal_02_gold.png")
    gold_medal = pygame.transform.scale(gold_medal,medidas_medallas)
    silver_medal = pygame.image.load("Heros_journey\\recursos\medallas\medal_02_silver.png")
    silver_medal = pygame.transform.scale(silver_medal,medidas_medallas)
    bronze_medal = pygame.image.load("Heros_journey\\recursos\medallas\medal_02_bronze.png")
    bronze_medal = pygame.transform.scale(bronze_medal,medidas_medallas)

    #boton
    ancho_boton = 500
    alto_boton = 60
    posicion_x = medidas_pantalla[0] // 2 - ancho_boton // 2
    posicion_2 = medidas_pantalla[1] - alto_boton - 80
    tamaño_fuente_boton = 46


    running = True
    while running:

        clock.tick(60)

        #fondo
        pantalla.blit(fondo_base,(0,0))

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_volver.collidepoint(event.pos):
                    return "menu_principal"
                
        fuente = pygame.font.Font(ruta_fuente, 40)
        x = medidas_pantalla[0] // 2 - 200
        x_score = x + 225
        y = 100
        texto = fuente.render(f"  Nombre  | Score ", True, "Black")
        pantalla.blit(texto, (x, y -60))
        
        if not puntajes:
            texto = fuente.render("Todavia no se cargo ningun puntaje.", True, "Black")
            pantalla.blit(texto, (x - 110 , y + 100))
        else:
            i=1
            for nombre, puntuacion in puntajes:
                if puntuacion is not None:
                    texto = fuente.render(f"{i}. {nombre}", True, "Black")
                    pantalla.blit(texto, (x, y))
                    texto = fuente.render(f"|  {puntuacion}", True, "Black")
                    pantalla.blit(texto, (x_score, y))
                    if i == 1:
                        pantalla.blit(gold_medal, (x - 45, y))
                    elif i == 2:
                        pantalla.blit(silver_medal, (x - 45, y))
                    elif i == 3:
                        pantalla.blit(bronze_medal, (x - 45, y))
            
                y += 60
                i += 1


        #boton
        boton_volver = pygame.Rect(posicion_x, posicion_2, ancho_boton, alto_boton)
        if boton_volver.collidepoint(pos):
            tamaño_fuente_boton = 66
        else:
            tamaño_fuente_boton = 46
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_boton)
        texto = fuente.render("Volver al menu principal", True, "White")
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_2 + alto_boton // 2))
        pantalla.blit(texto, text_rect)         
        
        #mouse
        pantalla.blit(new_mousse, pos)

        pygame.display.update()
        

    pygame.quit()

# leaderbord((1800,900))