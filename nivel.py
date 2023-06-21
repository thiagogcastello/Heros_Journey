import pygame
from configuraciones import *
from pygame.locals import *
from class_personaje import *
from modo import *
from class_plataforma import *
from class_proyectil import *
from class_enemigo import *
from class_portal import *

def nivel_1():
    pygame.init()

    #PANTALLA
    ancho_pantalla = 1800
    alto_pantalla = 900
    medidas_pantalla = (ancho_pantalla, alto_pantalla)
    pantalla = pygame.display.set_mode(medidas_pantalla)
    #FONDO
    fondo = pygame.image.load("Heros_journey\\recursos\\bg.png")
    fondo = pygame.transform.scale(fondo,medidas_pantalla)
    
    #RELOJ
    FPS = 60
    reloj = pygame.time.Clock()

    #ICONO
    pygame.display.set_caption("Heroe's Journey")


    #MUSICA
    pygame.mixer.music.load("Heros_journey\\recursos\sonidos\Adventure.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.01)
    musica_pausada = False


    #SCORE
    timer = pygame.USEREVENT
    pygame.time.set_timer(timer, 1000)
    secs_in_game = 0
    puntaje = 0
    ruta_fuente = 'Heros_journey\\recursos\Planes_ValMore.ttf'
    nivel_terminado = False

    #PAUSA
    ultima_imagen = None
    pausa = False

    #ITEMS
    medidas_moneda = (20,20)
    lista_monedas = []
    medidas_portal = (100,100)
    posicion_portal = (1700, 70)
    portal_terminar_nivel = Portal(medidas_portal, posicion_portal)

    #PLATAFORMAS
    medidas_base = (ancho_pantalla, 50)
    path_base = "Heros_journey\\recursos\plataformas\\tiles.png"
    #base
    lugar_base = (ancho_pantalla/2, alto_pantalla)
    base = Plataforma(medidas_base, path_base ,lugar_base)
    #plataforma 1
    medidas_plataformas = (300,30)
    lugar_p1 = (300, 770)
    p_1 = Plataforma(medidas_plataformas, path_base, lugar_p1)
    #plataforma 2
    medidas_plataformas_2 = (350,30)
    lugar_p2 = (559, 660)
    p_2 = Plataforma(medidas_plataformas_2, path_base, lugar_p2)
    #plataforma 3
    medidas_plataformas_3 = (150,30)
    lugar_p3 = (750, 541)
    p_3 = Plataforma(medidas_plataformas_3, path_base, lugar_p3)
    #plataforma 4
    medidas_plataformas_4 = (150,40)
    lugar_p4 = (863, 760)
    p_4 = Plataforma(medidas_plataformas_4, path_base, lugar_p4)
    #plataforma 5
    medidas_plataformas_5 = (550,40)
    lugar_p5 = (1311, 626)
    p_5 = Plataforma(medidas_plataformas_5, path_base, lugar_p5)
    #plataforma 6
    medidas_plataformas_6 = (300,30)
    lugar_p6 = (1574, 500)
    p_6 = Plataforma(medidas_plataformas_6, path_base, lugar_p6)
    #plataforma 7
    medidas_plataformas_7 = (600,30)
    lugar_p7 = (350, 449)
    p_7 = Plataforma(medidas_plataformas_7, path_base, lugar_p7)
    #plataforma 8
    medidas_plataformas_8 = (330,30)
    lugar_p8 = (371, 320)
    p_8 = Plataforma(medidas_plataformas_8, path_base, lugar_p8)
    #plataforma 9
    medidas_plataformas_9 = (100,30)
    lugar_p9 = (71, 235)
    p_9 = Plataforma(medidas_plataformas_9, path_base, lugar_p9)
    #plataforma 10
    medidas_plataformas_10 = (150,30)
    lugar_p10 = (1700, 130)
    p_10 = Plataforma(medidas_plataformas_10, path_base, lugar_p10)
    #plataforma 11
    medidas_plataformas_11 = (400,35)
    lugar_p11 = (1200, 419)
    p_11 = Plataforma(medidas_plataformas_11, path_base, lugar_p11)
    #plataforma 12
    medidas_plataformas_12 = (250,35)
    lugar_p12 = (800, 190)
    p_12 = Plataforma(medidas_plataformas_12, path_base, lugar_p12)

    lista_plataformas_con_monedas = [p_1, p_2,p_3,p_4,p_5, p_6, p_7, p_8,p_11]

    for plataforma in lista_plataformas_con_monedas:
        monedas_plataforma = plataforma.generar_monedas(medidas_moneda)
        lista_monedas.extend(monedas_plataforma)

    lista_plataformas = [base,p_1, p_2,p_3,p_4,p_5, p_6, p_7, p_8, p_9, p_10,p_11, p_12]


    #PERSONAJE
    posicion_inicial = (0,alto_pantalla-medidas_base[1] - 100)
    tamaño_personaje = (55,65)
    diccionario_animaciones = {}
    diccionario_animaciones["quieto_derecha"] = lista_quieto_derecha
    diccionario_animaciones["quieto_izquierda"] = lista_quieto_izquierda
    diccionario_animaciones["salta_derecha"] = lista_saltar
    diccionario_animaciones["salta_izquierda"] = lista_saltar_izquierda
    diccionario_animaciones["camina_derecha"] = lista_caminar_derecha
    diccionario_animaciones["camina_izquierda"] = lista_caminar_izquierda
    diccionario_animaciones["dispara_derecha"] = lista_disparar_derecha
    diccionario_animaciones["dispara_izquierda"] = lista_disparar_izquierda
    diccionario_animaciones["corre_derecha"] = lista_correr_derecha
    diccionario_animaciones["corre_izquierda"] = lista_correr_izquierda
    diccionario_animaciones["recibe_daño"] = lista_recibir_daño
    diccionario_animaciones["recibe_daño_izquierda"] = lista_recibir_daño_izquierda

    diccionarios_sonidos_personaje = sonidos_personaje

    velocidad_personaje = 6
    
    mi_personaje = Personaje(tamaño_personaje,diccionario_animaciones,posicion_inicial, velocidad_personaje, diccionarios_sonidos_personaje)

    #PROYECTIL
    path_proyectil = "Heros_journey\\recursos\piedra.png"
    lista_proyectiles = []


    #ENEMIGOS
    diccionario_animaciones_enemigo = {}
    diccionario_animaciones_enemigo["camina_derecha"] = lista_enemigo_caminar_derecha
    diccionario_animaciones_enemigo["camina_izquierda"] = lista_enemigo_caminar_izquierda
    diccionario_animaciones_enemigo["recibir_daño"] = lista_enemigo_recibir_daño
    diccionario_animaciones_enemigo["recibir_daño_izquierda"] = lista_enemigo_recibir_daño_izquierda = girar_imagen(lista_enemigo_recibir_daño, True, False)
    diccionario_animaciones_enemigo["atacar"] = lista_enemigo_atacar
    diccionario_animaciones_enemigo["atacar_izquierda"] = lista_enemigo_atacar_izquierda 
    diccionario_animaciones_enemigo["muere"] = lista_enemigo_muerto
    diccionario_animaciones_enemigo["muere_izquierda"] = lista_enemigo_muerto_izquierda

    velocidad_enemigo_1 = 6
    tamaño_enemigo_1 = (85,65)
    puntuacion_enemigo_1 = 20
    vida_enemigo_1 = 16
    enemigo_1 = Enemigo(tamaño_enemigo_1, diccionario_animaciones_enemigo,velocidad_enemigo_1, p_1, puntuacion_enemigo_1, vida_enemigo_1)
    
    velocidad_enemigo_2 = 8
    tamaño_enemigo_2 = (85,65)
    puntuacion_enemigo_2 = 45
    vida_enemigo_2 = 20
    enemigo_2 = Enemigo(tamaño_enemigo_2,diccionario_animaciones_enemigo,velocidad_enemigo_2, p_8, puntuacion_enemigo_2, vida_enemigo_2)

    velocidad_enemigo_3 = 4
    tamaño_enemigo_3 = (85,65)
    puntuacion_enemigo_3 = 25
    vida_enemigo_3 = 26
    enemigo_3 = Enemigo(tamaño_enemigo_3,diccionario_animaciones_enemigo,velocidad_enemigo_3, p_5, puntuacion_enemigo_3, vida_enemigo_3)
    
    lista_enemigos = [enemigo_1, enemigo_2, enemigo_3]

    pygame.mouse.set_visible(False)

    run = True
    while run:
        if not pausa:
            reloj.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F3:
                        cambiar_modo()
                    elif event.key == pygame.K_F8:
                        if musica_pausada:
                            pygame.mixer.music.unpause()
                            musica_pausada = False
                        else:
                            pygame.mixer.music.pause()
                            musica_pausada = True
                    elif event.key == pygame.K_ESCAPE:
                        pausa = not pausa
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print(pygame.mouse.get_pos())
                elif event.type == timer:
                    secs_in_game += 1
                    
            #ACTUALIZACION DE PANTALLA
            pantalla.blit(fondo,(0,0))
            for plataforma in lista_plataformas:
                pantalla.blit(plataforma.superficie,plataforma.rectangulo)
                p_12.mover_plataforma(1,'x', 1600, 600)

            mi_personaje.update(pantalla, lista_plataformas)
            nivel_terminado = portal_terminar_nivel.update(pantalla, mi_personaje)


            #MOVER PROYECTILES
            if mi_personaje.disparando and mi_personaje.puede_disparar:
                proyectil = Proyectil(path_proyectil, mi_personaje.direccion_disparo, mi_personaje)
                lista_proyectiles.append(proyectil)
                mi_personaje.disparando = False
                mi_personaje.puede_disparar = False

            for proyectil in lista_proyectiles:
                proyectil.mover()
                proyectil.detectar_piso(lista_plataformas)
                proyectil.desaparecer_proyectil()
                if not proyectil.ha_desaparecido:
                    pantalla.blit(proyectil.superficie, proyectil.rectangulo)
                else:
                    lista_proyectiles.remove(proyectil)

            #ENEMIGOS
            for enemigo in lista_enemigos:
                enemigo.update(pantalla, lista_proyectiles, mi_personaje)
                if enemigo.muerto == 'x':
                    lista_enemigos.remove(enemigo)
                    print('eliminado')


            #MODO HITBOX
            if get_modo():

                for plataforma in lista_plataformas:
                    plataforma.dibujar_hitbox(pantalla)
                mi_personaje.dibujar_hitbox(pantalla)
                enemigo_1.dibujar_hitbox(pantalla)

            #MONEDAS
            for moneda in lista_monedas:
                if not moneda.obtenida:
                    moneda.update(pantalla, mi_personaje)
            

            #PUNTAJE
            fuente = pygame.font.Font(ruta_fuente, 36)
            texto_puntaje = fuente.render("Puntaje: " + str(mi_personaje.score), True, (255, 255, 255))
            pantalla.blit(texto_puntaje, (20, 15))

            #CRONOMETRO
            minutos = secs_in_game // 60
            segundos = secs_in_game % 60

            minutos_str = str(minutos)
            segundos_str = str(segundos)

            minutos_str = minutos_str.zfill(2)
            segundos_str = segundos_str.zfill(2)

            tiempo_str = minutos_str + ":" + segundos_str

            # Renderiza el tiempo en la pantalla
            texto_tiempo = fuente.render("Tiempo: " + tiempo_str, True, (255, 255, 255))
            pantalla.blit(texto_tiempo, (20, 50))

            

            if mi_personaje.vida <= 0:
                nivel_terminado = True

            #NIVEL TERMINADO
            if nivel_terminado:
                bonus_tiempo = (mi_personaje.score / secs_in_game) * 10
                puntaje_total = mi_personaje.score + bonus_tiempo
                dict_puntaje = {}
                dict_puntaje["bonus_tiempo"] = bonus_tiempo
                dict_puntaje["puntaje_juego"] = mi_personaje.score
                dict_puntaje["puntaje_final"] = puntaje_total
                return "pantalla_puntaje", dict_puntaje

            pygame.display.flip()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pausa = not pausa

            fuente_pausa = pygame.font.Font(ruta_fuente, 72)
            texto_pausa = fuente_pausa.render("Pause", True, (255, 255, 255))
            pantalla.blit(texto_pausa, (ancho_pantalla // 2 -150, alto_pantalla // 2-150))
            pygame.display.flip()

    pygame.quit()

nivel_1()