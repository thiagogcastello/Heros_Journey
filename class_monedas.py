import pygame
from configuraciones import *
from class_personaje import *
import math
import random

class Moneda():
    def __init__(self, posicion, medidas):
        self.lista_animacion = lista_animacion_moneda
        self.valor = 10
        self.superficie = self.lista_animacion[0]
        self.superficie = pygame.transform.scale(self.superficie, medidas)
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.center = posicion
        self.contador_animacion = random.uniform(0,4)
        self.obtenida = False


    def animar(self, pantalla):
        animacion = self.lista_animacion
        largo = len(animacion)

        if self.contador_animacion >= largo:
            self.contador_animacion = 0

        aux_animacion = math.floor(self.contador_animacion)

        pantalla.blit(animacion[aux_animacion], self.rectangulo)

        self.contador_animacion += 0.3

    def update(self, pantalla, jugador):

        self.animar(pantalla)
        self.colision_con_jugador(jugador)
        

    def colision_con_jugador(self,jugador:Personaje):
        if self.rectangulo.colliderect(jugador.lados["main"]):
            sonido_moneda.set_volume(0.5)
            sonido_moneda.play()
            jugador.score += self.valor
            self.obtenida = True


