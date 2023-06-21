import pygame
from configuraciones import *
from class_monedas import *


class Plataforma:

    tipo = "Plataforma"

    def __init__(self, medidas, path_imagen, lugar) -> None:
        self.superficie = pygame.image.load(path_imagen)
        self.superficie = pygame.transform.scale(self.superficie, medidas)
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.center = lugar
        self.posicion = lugar
        self.lados = obtener_rectangulos(self.rectangulo)
        self.direccion = 1
        self.posicion_inicial = lugar[0]
        self.limite_derecha = False 
        
    def dibujar_hitbox(self,pantalla):
        for lado in self.lados:
            pygame.draw.rect(pantalla, "Blue", self.lados[lado], 3)

    def mover_plataforma(self, velocidad, eje_movimiento, limite_movimiento_derecha, limite_movimiento_izquierda):
        
        if eje_movimiento == 'x':

            if self.lados["main"].right >= limite_movimiento_derecha:
                self.limite_derecha = True
            elif self.lados["main"].left <= limite_movimiento_izquierda:
                self.limite_derecha = False

            if not self.limite_derecha:
                for lado in self.lados:
                    self.lados[lado].x += velocidad
            elif self.limite_derecha:
                for lado in self.lados:
                    self.lados[lado].x -= velocidad
        
        self.lados = obtener_rectangulos(self.rectangulo)
    
    def generar_monedas(self, medidas):
        cantidad_monedas = int(int(self.lados["main"].width / medidas[0]) / 4)
        distancia_entre_monedas = self.lados["main"].width / (cantidad_monedas + 1)
        posicion_x = self.rectangulo.left + distancia_entre_monedas

        monedas = []
        for i in range(cantidad_monedas):
            posicion = (posicion_x, self.rectangulo.centery - medidas[1]*2)
            moneda = Moneda(posicion, medidas)
            monedas.append(moneda)

            posicion_x += (distancia_entre_monedas)
        
        return monedas