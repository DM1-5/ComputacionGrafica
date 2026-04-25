import pygame
import sys

pygame.init()  # inicializa todos los módulos de pygame

# VENTANA Y RELOJ 
WIDTH, HEIGHT = 1200, 500                  # tamaño de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # crea la ventana
clock = pygame.time.Clock()                # reloj para limitar FPS

# CARGA DEL GATO 
idle = pygame.image.load("gato_frontal.png").convert_alpha()
# imagen del gato cuando está quieto (de frente), convert_alpha para respetar transparencia

# lista de imágenes del gato caminando hacia la IZQUIERDA (las originales tuyas)
walk_left = [
    pygame.image.load("gato1.png").convert_alpha(),
    pygame.image.load("gato2.png").convert_alpha(),
    pygame.image.load("gato3.png").convert_alpha(),
    pygame.image.load("gato4.png").convert_alpha(),
    pygame.image.load("gato5.png").convert_alpha(),
]

# generamos las mismas imágenes pero volteadas horizontalmente para caminar a la DERECHA
walk_right = [pygame.transform.flip(img, True, False) for img in walk_left]

#CARGA DEL FONDO 
bg = pygame.image.load("fondo.png").convert()  # cargamos el fondo
bg = pygame.transform.scale(bg, (bg.get_width(), HEIGHT))  # lo ajustamos a la altura de la ventana
BG_WIDTH = bg.get_width()  # ancho del fondo, necesario para el scroll

#ESTADO DEL GATO Y DEL MUNDO
cat_y = HEIGHT - 10        # posición vertical donde apoyaremos al gato
cat_screen_x = WIDTH // 2  # el gato se dibuja centrado en x en la pantalla
speed = 8                  # velocidad de movimiento
direction = "right"        # dirección inicial del gato
moving = False             # indica si el gato se está moviendo

# ANIMACIÓN
current_frame = 0          # índice del frame actual de caminar
ANIM_INTERVAL = 120        # tiempo en ms entre cambios de frame
last_anim_time = pygame.time.get_ticks()  # momento en que cambiamos de frame por última vez

scroll_x = 0               # cuánto se ha desplazado el fondo (scroll)

# BUCLE PRINCIPAL
running = True
while running:
    dt = clock.tick(60)    # limita a 60 FPS y devuelve ms desde el frame anterior

    #MANEJO DE EVENTOS
    for e in pygame.event.get():
        if e.type == pygame.QUIT:  # si se cierra la ventana
            pygame.quit()
            sys.exit()

    # ENTRADA DE TECLADO 
    keys = pygame.key.get_pressed()  # estado de todas las teclas
    moving = False                   # por defecto no se mueve

    if keys[pygame.K_RIGHT]:
        # si se presiona derecha: queremos que el gato avance a la derecha
        # para dar esa sensación movemos el FONDO hacia la izquierda
        scroll_x += speed
        direction = "right"
        moving = True
    elif keys[pygame.K_LEFT]:
        # si se presiona izquierda: fondo hacia la derecha
        scroll_x -= speed
        direction = "left"
        moving = True

    # hacemos que el scroll sea cíclico: cuando pasa el ancho del fondo, vuelve a 0
    scroll_x = scroll_x % BG_WIDTH

    # ACTUALIZAR ANIMACIÓN DEL GATO 
    if moving:
        now = pygame.time.get_ticks()  # tiempo actual en ms
        # si ya pasó ANIM_INTERVAL desde el último cambio de frame
        if now - last_anim_time > ANIM_INTERVAL:
            # El modulo detecta cuando se llega al último frame y vuelve al primero, creando un ciclo de animación 5%5=0
            current_frame = (current_frame + 1) % len(walk_right)  # siguiente frame
            last_anim_time = now

        # elegimos la lista correcta según la dirección
        if direction == "right":
            img = walk_right[current_frame]
        else:
            img = walk_left[current_frame]

        # pequeño salto vertical alternado para que se note el paso
        bob = -4 if current_frame % 2 == 1 else 0
    else:
        # si no se mueve, mostrar imagen quieta
        img = idle
        current_frame = 0
        bob = 0
        # reiniciamos el contador de tiempo para que la animación no “salte” al volver a moverse
        last_anim_time = pygame.time.get_ticks()

    #  DIBUJO DEL FONDO 
    # primer fondo desplazado según scroll_x
    screen.blit(bg, (-scroll_x, 0))
    # segundo fondo pegado al primero para rellenar cuando el primero se desplaza
    screen.blit(bg, (-scroll_x + BG_WIDTH, 0))

    # DIBUJO DEL GATO 
    rect = img.get_rect()                     # rectángulo de la imagen actual
    rect.midbottom = (cat_screen_x, cat_y + bob)  # lo colocamos centrado y apoyado en el “piso”
    screen.blit(img, rect)                    # dibujar gato

    pygame.display.flip()                     # actualizar pantalla
