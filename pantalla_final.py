import pygame
from pygame.locals import *
import math
from configuraciones import teclas_letras
from base_datos import *

pygame.init()


def mostrar_pantalla_final(medidas_pantalla, dict_puntaje:dict):

    pantalla = pygame.display.set_mode(medidas_pantalla)
    pygame.display.set_caption("Hero's Journey")
    clock = pygame.time.Clock()

    fondo = pygame.image.load("Heros_journey\\recursos\\RockBG.png")
    fondo = pygame.transform.scale(fondo,medidas_pantalla)

    ruta_fuente = 'Heros_journey\\recursos\Planes_ValMore.ttf'
    fuente_titulo = pygame.font.Font(ruta_fuente, 40)
    fuente_puntaje = pygame.font.Font(ruta_fuente, 30)

    #musica
    pygame.mixer.music.load("Heros_journey\\recursos\sonidos\Adventure.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.02)

    #mousse
    new_mousse = pygame.image.load("Heros_journey\\recursos\mouse.png")
    new_mousse = pygame.transform.scale(new_mousse,(30,30))

    #botones
    ancho_boton = 300
    alto_boton = 30
    separacion_botones = 50
    posicion_x = (medidas_pantalla[0] - ancho_boton) // 2
    posicion_1 = ((medidas_pantalla[1] - (alto_boton + separacion_botones) * 3) // 2) + separacion_botones * 3
    posicion_2 = posicion_1 + alto_boton + separacion_botones
    posicion_3 = posicion_2 + alto_boton +separacion_botones

    #letras
    letra_1 = None
    letra_2 = None
    letra_3 = None

    puede_guardar = False
    boton_2_apretado = False
    carga = False
    volvio_a_cargar =False

    pygame.mouse.set_visible(False)

    running = True
    while running:

        clock.tick(60)

        #fondo
        pantalla.blit(fondo,(0,0))

        #guardado base de datos
        if letra_1 != None and letra_2 != None and letra_3 != None:
            puede_guardar = True

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if boton_1.collidepoint(mouse_pos):
                    return "nivel_1"
                if boton_2.collidepoint(mouse_pos) and not volvio_a_cargar:
                    boton_2_apretado = True
                if boton_3.collidepoint(mouse_pos):
                    return "menu_principal"
            elif event.type == pygame.KEYDOWN:
                for tecla, letra in teclas_letras.items():
                    if event.key == tecla:
                        if letra_1 == None:
                            letra_1 = letra
                        elif letra_2 == None:
                            letra_2 = letra
                        elif letra_3 == None:
                            letra_3 = letra
                    elif event.key == pygame.K_BACKSPACE:
                        if letra_3 is not None:
                            letra_3 = None
                            puede_guardar = False
                        elif letra_2 is not None:
                            letra_2 = None
                        elif letra_1 is not None:
                            letra_1 = None

        bonus_tiempo = int(math.ceil(dict_puntaje['bonus_tiempo']))
        puntaje_juego = dict_puntaje['puntaje_juego']
        puntaje_final = bonus_tiempo + puntaje_juego

        texto_bonus_tiempo = fuente_puntaje.render(f"Bonus por tiempo: {bonus_tiempo}", True, (255, 255, 255))
        texto_puntaje_juego = fuente_puntaje.render(f"Puntaje del juego: {puntaje_juego}", True, (255, 255, 255))
        texto_puntaje_total = fuente_titulo.render(f"Puntaje total: {puntaje_final}", True, (255, 255, 255))


        pantalla.blit(texto_bonus_tiempo, ((medidas_pantalla[0] // 2) - 160, 50))
        pantalla.blit(texto_puntaje_juego, ((medidas_pantalla[0] / 2) - 170, 100))
        pantalla.blit(texto_puntaje_total, ((medidas_pantalla[0] / 2) - 180, 200))


        texto_ingresar_nombre = fuente_puntaje.render("Ingrese nombre:", True, (255, 255, 255))
        pantalla.blit(texto_ingresar_nombre, ((medidas_pantalla[0] // 2) - 120, 300))

    
        texto_letras = fuente_puntaje.render(f"{letra_1 or '_'} {letra_2 or '_'} {letra_3 or '_'}", True, (255, 255, 255))
        pantalla.blit(texto_letras, ((medidas_pantalla[0] // 2) - 50, 390))


        

        #boton 1
        boton_1 = pygame.Rect(posicion_x, posicion_1, ancho_boton, alto_boton)
        if boton_1.collidepoint(mouse_pos):
            tamaño_fuente_boton = 66
        else:
            tamaño_fuente_boton = 46
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_boton)
        texto = fuente.render("Volver a jugar", True, (255, 255, 255))
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_1 + alto_boton // 2))
        pantalla.blit(texto, text_rect)

        #boton 2
        boton_2 = pygame.Rect(posicion_x, posicion_2, ancho_boton, alto_boton)
        if boton_2.collidepoint(mouse_pos):
            tamaño_fuente_boton = 66
        else:
            tamaño_fuente_boton = 46
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_boton)
        texto = fuente.render("Guardar puntaje", True, (255, 255, 255))
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_2 + alto_boton // 2))
        pantalla.blit(texto, text_rect)

        #boton 3
        boton_3 = pygame.Rect(posicion_x, posicion_3, ancho_boton, alto_boton)
        if boton_3.collidepoint(mouse_pos):
            tamaño_fuente_boton = 66
        else:
            tamaño_fuente_boton = 46
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_boton)
        texto = fuente.render("Volver al menu principal", True, (255, 255, 255))
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_3 + alto_boton // 2))
        pantalla.blit(texto, text_rect)

        if boton_2_apretado:
            if puede_guardar:
                nombre = letra_1 + letra_2 + letra_3
                carga = cargar_campo_bd(nombre, puntaje_final)
                boton_2_apretado = False
            else:
                boton_2_apretado = False
        
        if carga:
            texto = fuente_puntaje.render("Se cargo correctamente", True, (255, 255, 255))
            pantalla.blit(texto, ((medidas_pantalla[0] // 2) - 160, 750))
            volvio_a_cargar = True
        else:
            texto = fuente_puntaje.render("Se deben ingresar las 3 letras para poder guardar.", True, (255, 255, 255))
            pantalla.blit(texto, ((medidas_pantalla[0] // 2) - 360, 750))
        
        
        #mouse
        pos = pygame.mouse.get_pos()
        pantalla.blit(new_mousse, pos)

        pygame.display.update()
        

    pygame.quit()



# ancho_pantalla = 1800
# alto_pantalla = 900
# medidas_pantalla = (ancho_pantalla, alto_pantalla)
# dict_puntaje = {}
# dict_puntaje["bonus_tiempo"] = 20
# dict_puntaje["puntaje_juego"] = 360
# dict_puntaje["puntaje_final"] = 380
# mostrar_pantalla_final(medidas_pantalla, dict_puntaje)