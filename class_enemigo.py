import pygame, math, time
from configuraciones import *
from class_plataforma import *
from class_personaje import *
from class_enemigo import *


class Enemigo():
    def __init__(self,tamaño, animaciones, velocidad, plataforma_base, valor_puntuacion, vida) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.plataforma_base = plataforma_base
        #animaciones
        self.contador_pasos = 0
        self.que_hace = "camina_derecha"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.atacando = False
        #rectangulos
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = plataforma_base.rectangulo.left
        self.rectangulo.bottom = plataforma_base.rectangulo.top
        self.lados = obtener_rectangulos(self.rectangulo)
        #stats
        self.velocidad = velocidad
        self.vida = vida
        self.daño_ataque = 1
        self.valor_puntuacion = valor_puntuacion
        self.muerto = False
        self.cool_down_ataque = 0

    #METODOS

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], (self.ancho,self.alto))

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        aux_pasos = math.floor(self.contador_pasos)

        pantalla.blit(animacion[aux_pasos], self.lados["main"])

        self.contador_pasos += 0.3

    
    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def detectar_colision_proyectiles(self, lista_proyectiles):
        for proyectil in lista_proyectiles:
            if self.lados["main"].colliderect(proyectil.rectangulo):
                if proyectil.daño:
                    self.que_hace = "recibir_daño"
                    self.vida -= 2
                    self.velocidad = self.velocidad * 1.05
                    proyectil.daño = False
                   
            
    def detectar_borde_plataformas(self):
        if self.rectangulo.right >= self.plataforma_base.rectangulo.right:
            self.que_hace = "camina_izquierda"
            self.velocidad = abs(self.velocidad) * (-1)
        elif self.rectangulo.left <= self.plataforma_base.rectangulo.left:
            self.que_hace = "camina_derecha"
            self.velocidad = abs(self.velocidad)

    def detectar_colision_con_personaje(self,personaje:Personaje):
        self.cooldown()

        if self.cool_down_ataque == 0:
            
            if self.lados["main"].colliderect(personaje.lados["main"]) and not self.atacando:
                personaje.atacado = True
                self.atacando = True
                personaje.daño_realizado = self.daño_ataque
                self.cool_down_ataque = 1
                self.que_hace = "atacar"
            # elif self.lados["left"].colliderect(personaje.lados["main"]) and not self.atacando:
            #     self.que_hace = "atacar_izquierda"
            #     personaje.atacado = True
            #     personaje.daño_realizado = self.daño_ataque
            #     self.atacando = True
            #     self.cool_down_ataque = 1
            else:
                self.atacando = False
        else:
            self.atacando = False
        
    def cooldown(self):
        if self.cool_down_ataque >= 10:
            self.cool_down_ataque = 0
        elif self.cool_down_ataque > 0:
            self.cool_down_ataque += 1 
        
    def update(self, pantalla, lista_proyectiles, personaje):

        if self.que_hace == "camina_derecha":
            self.animar(pantalla, "camina_derecha")
        if self.que_hace == "camina_izquierda":
            self.animar(pantalla, "camina_izquierda")
        if self.que_hace == "recibir_daño":
            if self.velocidad >= 0:
                self.animar(pantalla, "recibir_daño")
            else:
                self.animar(pantalla, "recibir_daño_izquierda")
        if self.que_hace == "atacar":
            self.animar(pantalla,"atacar")
        # if self.que_hace == "atacar_izquierda":
        #     self.animar(pantalla,"atacar_izquierda")
        if self.que_hace == "muere":
            if self.velocidad >= 0:
                self.que_hace = "muere"
                self.animar(pantalla, "muere")
                print('muere')
            else:
                self.que_hace = "muere_izquierda"
                self.animar(pantalla, "muere_izquierda")
                print('muere')


        if self.vida <= 0:
            self.muerto = True

            
        if not self.muerto:
            self.mover(self.velocidad)
            self.detectar_borde_plataformas()
            self.detectar_colision_proyectiles(lista_proyectiles)
            self.detectar_colision_con_personaje(personaje)
        elif self.muerto:
            self.matar_enemigo(personaje, pantalla)
            print('muere 1212')

        

    def dibujar_hitbox(self, pantalla):
        for lado in self.lados:
            pygame.draw.rect(pantalla,"Red",self.lados[lado],1)

    def matar_enemigo(self, personaje, pantalla):
        personaje.sumar_puntuacion(self.valor_puntuacion)
        self.muerto = 'x'

            
        