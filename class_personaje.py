import pygame
from configuraciones import *
import math

class Personaje():
    
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad, sonidos):
        #CONSTRUCTOR
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #gravedad
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        #animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.sentido_eje_x = False
        #rectangulos
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        #movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #disparo
        self.disparando = False
        self.direccion_disparo = False
        self.puede_disparar = True
        self.cool_down_disparo = 0
        #salud
        self.vida = 7
        self.atacado = True
        self.daño_realizado = 0
        self.img_corazon = pygame.image.load('Heros_journey\\recursos\corazon.png')
        self.img_corazon = pygame.transform.scale(self.img_corazon, (50,50))
        #puntaje
        self.score = 0
        #sonidos
        self.diccionario_sonidos = sonidos


    #METODOS

    def reproducion_sonido(self, clave, volumen):
        if clave in self.diccionario_sonidos:
            sonido = self.diccionario_sonidos.get(clave)
            sonido.set_volume(volumen)
            sonido.play()
    
    def cooldown(self):
        if self.cool_down_disparo >= 15:
            self.cool_down_disparo = 0
        elif self.cool_down_disparo >0:
            self.cool_down_disparo += 1  

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

        self.contador_pasos += 0.4

    def aplicar_gravedad(self, pantalla):
        if self.esta_saltando:
            self.sonido_reproducido = False
            if self.sentido_eje_x == "izquierda":
                self.animar(pantalla,"salta_izquierda")
            else:
                self.animar(pantalla,"salta_derecha")

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

    def detectar_colision(self,plataformas):
        for plataforma in plataformas:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = plataforma.lados["main"].top + 1
                if not self.sonido_reproducido:
                    self.reproducion_sonido("caer", 0.03)
                    self.sonido_reproducido = True
                break
            else:
                self.esta_saltando = True

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def update(self, pantalla, piso):

        keys = pygame.key.get_pressed()
        self.cooldown()

        self.que_hace = "quieto"

        if keys[pygame.K_d]:
            self.que_hace = "derecha"
            self.sentido_eje_x = "derecha"
            self.mover(self.velocidad)
            if not self.esta_saltando:
                if keys[pygame.K_LSHIFT]:
                    self.que_hace = "corre_derecha"
        elif keys[pygame.K_a]:
            self.que_hace = "izquierda"
            self.sentido_eje_x = "izquierda"
            self.mover((self.velocidad)*-1)
            if not self.esta_saltando:
                if keys[pygame.K_LSHIFT]:
                    self.que_hace = "corre_izquierda"
        
        if keys[pygame.K_w]:
            self.que_hace = "salta"            

        if self.cool_down_disparo == 0:

            if keys[pygame.K_RIGHT] and not self.disparando:
                self.que_hace = "dispara"
                self.disparando = True
                self.direccion_disparo = "derecha"
                self.cool_down_disparo = 1
                self.reproducion_sonido("tirar", 0.03)
            elif keys[pygame.K_LEFT] and not self.disparando:
                self.que_hace = "dispara"
                self.disparando = True
                self.direccion_disparo = "izquierda"
                self.cool_down_disparo = 1
                self.reproducion_sonido("tirar", 0.03)

        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.disparando = False
            self.puede_disparar = True

        if self.atacado:
            self.recibir_daño(self.daño_realizado)

        self.aplicar_gravedad(pantalla)
        self.detectar_colision(piso)
        self.detectar_bordes_pantalla(pantalla)
        self.ejecutar_animaciones(pantalla)
        self.dibujar_vida_en_pantalla(pantalla)
        self.lados = obtener_rectangulos(self.rectangulo)

    def recibir_daño(self, ataque):
        self.que_hace = "recibe_daño"
        self.vida -= ataque
        self.atacado = False


    def ejecutar_animaciones(self, pantalla):
        if self.que_hace == "dispara":
            if self.direccion_disparo == "derecha":
                self.animar(pantalla,"dispara_derecha")
            else:
                self.animar(pantalla,"dispara_izquierda")
        if self.que_hace == "derecha":
            if not self.esta_saltando:
                self.animar(pantalla,"camina_derecha")
        if self.que_hace == "izquierda":
            if not self.esta_saltando:
                self.animar(pantalla,"camina_izquierda")
        if self.que_hace == "salta":
            if not self.esta_saltando:
                self.esta_saltando = True
                self.desplazamiento_y = self.potencia_salto
        if self.que_hace == "quieto":
            if not self.esta_saltando:
                if self.sentido_eje_x == "izquierda":
                    self.animar(pantalla,"quieto_izquierda")
                else:
                    self.animar(pantalla,"quieto_derecha")
        if self.que_hace == "corre_izquierda":
            if not self.esta_saltando:
                self.animar(pantalla,"corre_izquierda")
            self.mover(self.velocidad * (-1.5))
        if self.que_hace == "corre_derecha":
            if not self.esta_saltando:
                self.animar(pantalla,"corre_derecha")
            self.mover(self.velocidad * 1.5)
        if self.que_hace == "recibe_daño":
            if self.sentido_eje_x == "derecha":
                self.animar(pantalla, "recibe_daño")
            else:
                self.animar(pantalla, "recibe_daño_izquierda")

    def detectar_bordes_pantalla(self,pantalla):
        if self.rectangulo.right >= pantalla.get_size()[0] - 1:
            self.rectangulo.right = pantalla.get_size()[0] - 1
            self.velocidad_x = 0
        elif self.rectangulo.left <= 0:
            self.rectangulo.left = 0
            self.velocidad_y = 0

        if self.rectangulo.top <= 0:
            self.rectangulo.top = 0
        elif self.rectangulo.bottom >= pantalla.get_size()[1] - 1:
            self.rectangulo.bottom = pantalla.get_size()[1] - 1

    
    def dibujar_hitbox(self,pantalla):
        for lado in self.lados:
            pygame.draw.rect(pantalla,"Red",self.lados[lado],1)

    
    def sumar_puntuacion(self, puntos):
        self.score += puntos
        print(self.score)

    def dibujar_vida_en_pantalla(self, pantalla):
        x = (pantalla.get_width() // 2) - 300
        for i in range(self.vida):
            pantalla.blit(self.img_corazon,(x,10))
            x += 75
        