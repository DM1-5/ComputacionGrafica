import pygame   #pip install pygame

#Configuración inicial de pygame 
pygame.init()  # Inicializa todos los módulos de Pygame

# Crea una ventana de 1280 x 720 píxeles
screen = pygame.display.set_mode((500, 500))

# Reloj para controlar los FPS (frames por segundo)
clock = pygame.time.Clock()

# Variable de control para mantener abierto el bucle del juego
running = True

COLOR = (40,110,190)

# Bucle principal
while running:
    # Revisa los eventos 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rellena la pantalla con blanco (limpia el frame anterior)
    screen.fill("white")
    
    # Línea: (superficie, color, (x1,y1), (x2,y2), grosor)
    #pygame.draw.line(screen, COLOR, (50,50), (100,400), 20)
    
    # Círculo: (superficie, color, (cx,cy), radio, grosor=0 relleno)
    #pygame.draw.circle(screen, "red", (100,100), 40, width=5)
    
    # Rectángulo: (superficie, color, (x,y,ancho,alto), grosor=0 relleno)
    pygame.draw.rect(screen, "green", (300, 300, 100, 100), width=4)
    
    # Polígono: (superficie, color, [(x1,y1), (x2,y2), (x3,y3), ...], grosor=0 relleno)
    #pygame.draw.polygon(screen, "yellow", [(400, 400), (500, 400), (450, 500)],width=4)
    
    # Elipse: (superficie, color, (x,y,ancho,alto), grosor=0 relleno)
    #pygame.draw.ellipse(screen, "orange", (300, 300, 100, 70),width=4)
    
    # Arco: (superficie, color, (x,y,ancho,alto), ang_inicio, ang_fin, grosor)
    # Ángulos en radianes (ejemplo: 0 a 3.14 ≈ semicírculo)
    #pygame.draw.arc(screen, "red", (200, 200, 100, 50), 0, 3.14/2, 5)

    # Actualiza la pantalla con lo que se ha dibujado
    pygame.display.flip()
    
    # Control de FPS: limita el bucle a 60 cuadros por segundo
    # dt = tiempo transcurrido entre frames en segundos
    dt = clock.tick(60)

# Cierra pygame correctamente cuando termina el bucle
pygame.quit()