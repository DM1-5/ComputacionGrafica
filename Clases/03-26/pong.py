import pygame

pygame.init()
ancho, alto = 500, 500
screen = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()

pos1 = [0, 0]
pos2 = [ancho - 10, 0]  # posición inicial

vel = 10           # velocidad de movimiento
running = True


# Bucle pincipal, cierra el juego.
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

    keys = pygame.key.get_pressed()
    # Esta es la posicion de y (w para subir)
    if keys[pygame.K_w] and pos1[1] > 0:
        pos1[1] -= vel
    # Esta es la posicion de y (s para bajar)
    if keys[pygame.K_s] and pos1[1] < 500 - 50:
        pos1[1] += vel

    # Esta es la posicion del jugador 1 y (w para subir)
    if keys[pygame.K_UP] and pos2[1] > 0:
        pos2[1] -= vel
        # Esta es la posicion del jugador 2 y (s para bajar)
    if keys[pygame.K_DOWN] and pos2[1] < 500 - 50:
        pos2[1] += vel


    screen.fill((0, 0, 0))


    # Rectángulo: (superficie, color, (x,y,ancho,alto), grosor=0 relleno)
    # jugador 1
    pygame.draw.rect(screen, "red", (pos1[0], pos1[1], 10, 50), width=4)

    # Rectángulo: (superficie, color, (x,y,ancho,alto), grosor=0 relleno)
    # jugador 2
    pygame.draw.rect(screen, "red", (pos2[0], pos2[1], 10, 50), width=4)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()