import pygame
import numpy as np
from PIL import Image

# EL PONG HACE PARTE DE LA ENTREGA DE PYGAME 

# pong 

# Todo: 
# 1. movimiento del circulo (pelota)
# 2. colision con las paredes
# 3. colision con las jugadores
# 4. sistema de puntos


def menu():
    ancho, alto = 600, 400
    screen = pygame.display.set_mode((ancho, alto))
    imgMenu = pygame.image.load("bitMenu1.png")
    screen.blit(imgMenu, (0, 0))
    pygame.display.flip()
    running = True 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                
                # Pulsa el boton de jugar
                if pos[0] >= 240 and pos[0] <= 367 and pos[1] >= 144 and pos[1] <= 191:
                    juego()
                    running = False

                # Pulsa el boton de ayuda
                if pos[0] >= 240 and pos[0] <= 367 and pos[1] >= 225 and pos[1] <= 270:
                    ayuda()
                    running = False
                
                # Pulsa el boton de salir
                if pos[0] >= 240 and pos[0] <= 367 and pos[1] >= 305 and pos[1] <= 350:
                    running = False

def inicio():
    # CONFIGURACION 
    ancho, alto = 1280, 720
    screen = pygame.display.set_mode((ancho, alto))
    imgAyuda = pygame.image.load("presentacion.png")
    screen.blit(imgAyuda, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5000)

    menu()

def juego():
    ancho, alto = 600, 400
    screen = pygame.display.set_mode((ancho, alto))
    clock = pygame.time.Clock()

    # COLORES Gruvbox 
    textoColor = (251, 241, 199)
    fondo = (40, 40, 40)
    rojo = (251, 73, 52)
    verde = (184, 187, 38)
    azul = (131, 165, 152)

    # PUNTAJE 
    puntos1 = 0
    puntos2 = 0

    pygame.font.init()
    fuente = pygame.font.SysFont("m5x7", 60)  #Fuente
    puntaje1 = fuente.render(f"0{puntos1}", True ,  verde) 
    puntaje2 = fuente.render(f"0{puntos2}", True ,  azul) 
    #texto = fuente.render(f"{puntos1} vs {puntos2}", True ,  textoColor) #Renderizar

    # AUDIOS 
    # Los sonidos los generé con gemini 
    pygame.mixer.init()
    gol1 = pygame.mixer.Sound("gol1.wav")
    gol2 = pygame.mixer.Sound("gol2.wav")
    raqueta = pygame.mixer.Sound("raqueta.wav")
    rebote = pygame.mixer.Sound("rebote.wav")
    fin = pygame.mixer.Sound("fin.wav")

    # Jugador1
    pos1 = [10, alto/2 - 25]  # posición inicial
    # Jugador2
    pos2 = [ancho - 20, alto/2 - 25]  # posición inicial
    # pelota
    posc = [ancho/2, alto/2] # posición inicial
    vel = 20           # velocidad de movimiento
    running = True 

    pelota_x = ancho/2
    pelota_y =  ancho/2
    pelotaVel_x = 2
    pelotaVel_y = 2

    # Bucle pincipal, cierra el juego.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()
            # Esta es la posicion de jugador 1 (w para subir)
            if keys[pygame.K_w] and pos1[1] > 0:
                pos1[1] -= vel
            # Esta es la posicion de jugador 1 (s para bajar)
            if keys[pygame.K_s] and pos1[1] < alto - 50:
                pos1[1] += vel

            # Esta es la posicion del jugador 2 (flecha arriba para subir)
            if keys[pygame.K_UP] and pos2[1] > 0:
                pos2[1] -= vel
                # Esta es la posicion del jugador 2 (flecha abajo para bajar)
            if keys[pygame.K_DOWN] and pos2[1] < alto - 50:
                pos2[1] += vel

        # LIMITES DE PELOTA EN Y
        if posc[1] >= 390 or posc[1] <= 10:
            pelotaVel_y *= -1
            rebote.play()

        # PELOTA TOCA DERECHA
        if posc[0] > ancho:
            posc[0] = ancho/2
            posc[1] = ancho/2
            # Si sale de la pantalla, invierte direccion
            pelotaVel_x *= -1
            pelotaVel_y *= -1
            puntos1 += 1
            puntaje1 = fuente.render(f"0{puntos1}", True ,  verde) #Renderizar
            #texto = fuente.render(f"{puntos1} vs {puntos2}", True , textoColor) #Renderizar
            gol1.play()

        # PELOTA TOCA IZQUIERDA
        if posc[0] < 0:
            posc[0] = ancho/2
            posc[1] = alto/2
            # Si sale de la pantalla, invierte direccion
            pelotaVel_x *= -1
            pelotaVel_y *= -1
            puntos2 += 1
            puntaje2 = fuente.render(f"0{puntos2}", True ,  azul) 
            #texto = fuente.render(f"{puntos1} vs {puntos2}", True , textoColor) #Renderizar
            gol1.play()

        if puntos1 == 5:
            fin.play()
            screen.fill(fondo)
            texto = fuente.render("Jugador 1 gana!", True , verde) #Renderizar
            # Dibujar en la mitad de la pantalla
            screen.blit(texto, (ancho/2 - 100, alto/2 - 10))  #Dibujar en pantalla
            pygame.display.flip()
            pygame.time.delay(5000)
            running = False
            menu()

        if puntos2 == 5:
            fin.play()
            screen.fill(fondo)
            texto = fuente.render("Jugador 2 gana!", True , azul) #Renderizar
            # Dibujar en la mitad de la pantalla
            screen.blit(texto, (ancho/2 - 100, alto/2 - 10))  #Dibujar en pantalla
            pygame.display.flip()
            pygame.time.delay(5000)
            running = False
            menu()
            

        posc[0] += pelotaVel_x
        posc[1] += pelotaVel_y

        screen.fill(fondo)
        # Dibujar el puntaje en la parte superior centrado
        screen.blit(puntaje1, (10, 10))
        screen.blit(puntaje2, (ancho - 10 - puntaje2.get_width(), 10))
        #screen.blit(texto, (ancho/2 - 100/2, 10))  #Dibujar en pantalla

        # Rectángulo: (superficie, color, (x,y,ancho,alto), grosor=0 relleno)
        # jugador 1
        jugador1 = pygame.draw.rect(screen, verde, (pos1[0], pos1[1], 10, 50))

        # Rectángulo: (superficie, color, (x,y,ancho,alto), grosor=0 relleno)
        # jugador 2
        jugador2 = pygame.draw.rect(screen, azul, (pos2[0], pos2[1], 10, 50))

        # Circulo: (superficie, color, (x,y), radio)
        # pelota
        pelota = pygame.draw.circle(screen, rojo, (posc[0], posc[1]), 10)

        if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
            pelotaVel_x *= -1
            raqueta.play()

        pygame.display.flip()
        clock.tick(60)

def ayuda():
    ancho, alto = 600, 400
    screen = pygame.display.set_mode((ancho, alto))
    imgAyuda = pygame.image.load("HELP_textos.png")
    screen.blit(imgAyuda, (0, 0))
    pygame.display.flip()
    
    running = True 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                
                # Pulsa el boton de jugar
                if pos[0] >= 50 and pos[0] <= 160 and pos[1] >= 320 and pos[1] <= 367:
                    menu()
                    running = False
    #menu()

if __name__ == "__main__":
    #inicio()
    menu()
    #juego()
    #ayuda()
    pygame.quit()
    