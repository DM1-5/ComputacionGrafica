import pygame

pygame.init()
ancho, alto = 500, 500
screen = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()
radio = 15
posR = [0, 0]
pos = [50, 50]  # posición inicial
vel = 10           # velocidad de movimiento
running = True


# Bucle pincipal, cierra el juego.
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

    keys = pygame.key.get_pressed()
    # Esta es la posicion de y (w para subir)
    if keys[pygame.K_w] and posR[1] > 0:
        posR[1] -= vel
    # Esta es la posicion de y (s para bajar)
    if keys[pygame.K_s] and posR[1] < 400:
        posR[1] += vel
    # Esta es la posicion de x (a para izquierda)
    if keys[pygame.K_a] and posR[0] > 0:
        posR[0] -= vel
    # Esta es la posicion de x (d para derecha)
    if keys[pygame.K_d] and posR[0] < 400:
        posR[0] += vel

    if keys[pygame.K_UP] and pos[1] > 0 + radio:
        pos[1] -= vel
    if keys[pygame.K_DOWN] and pos[1] < 500 - radio:
        pos[1] += vel
    if keys[pygame.K_LEFT] and pos[0] > 0 + radio:
        pos[0] -= vel
    if keys[pygame.K_RIGHT] and pos[0] < 500 - radio:
        pos[0] += vel

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), pos, radio)
    # Rectángulo: (superficie, color, (x,y,ancho,alto), grosor=0 relleno)
    pygame.draw.rect(screen, "red", (posR[0], posR[1], 100, 100), width=4)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()