import pygame
from configuraciones import *
from class_personaje import *
import math
import random

class Portal():

    def __init__(self,medidas, posicion):
        self.lista_animacion = lista_portal
        reescalar_imagen(self.lista_animacion, medidas)
        self.superficie = self.lista_animacion[0]
        self.superficie = pygame.transform.scale(self.superficie, medidas)
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.center = posicion
        self.contador_animacion = 0

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
        retorno = self.colision_con_jugador(jugador)

        return retorno

    def colision_con_jugador(self, jugador:Personaje):
        if self.rectangulo.colliderect(jugador.lados["left"]):
            return True
        else:
            return False
