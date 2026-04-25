import pygame, random  

#Parámetros globales 
W, H = 900, 600          # Tamaño de ventana
GRAVEDAD = 2000.0        # Aceleración vertical px/s^2
RESTITUCION = 0.6       # Coeficiente de rebote
ROZAMIENTO_AIRE = 0.5   # Factor por segundo (1 = sin rozamiento)

pygame.init()
screen = pygame.display.set_mode((W, H))
clock  = pygame.time.Clock()
pygame.display.set_caption("Gravedad Pygame")
font = pygame.font.SysFont(None, 22)

# Lista de bolas, cada una es un diccionario 
bolas = []

def crear_bola(x, y, vx, vy, r=14):
    """Crea una bola con posición (x,y), velocidad (vx,vy) y radio r."""
    color = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
    bolas.append({
        "x": float(x), "y": float(y),   # posición en float para precisión
        "vx": float(vx), "vy": float(vy),  # velocidad
        "r": r, "color": color
    })

def actualizar_bolas(dt):
    """Integra la física de todas las bolas en dt segundos."""
    # Rozamiento aplicado como decaimiento exponencial por segundo
    drag = ROZAMIENTO_AIRE ** dt
    for b in bolas:
        # 1) fuerzas -> aceleraciones: solo gravedad en Y
        b["vy"] += GRAVEDAD * dt        # [m/s] = [m/s^2]*[s]            v = v_0 +a*t

        # 2) rozamiento (reduce gradualmente la velocidad)
        b["vx"] *= drag
        b["vy"] *= drag

        # 3) integración de posición
        b["x"]  += b["vx"] * dt    
        b["y"]  += b["vy"] * dt    #[m] = [m/s]*[s]       y = y_0 + vt 

        r = b["r"]

        # 4) colisiones con paredes izquierda y derecha
        if b["x"] - r < 0:
            b["x"] = r                     # corrige visualmente
            b["vx"] = -b["vx"] * RESTITUCION  # invierte y amortigua
        if b["x"] + r > W:
            b["x"] = W - r
            b["vx"] = -b["vx"] * RESTITUCION     #pierde velocidad  amortigua

        # 5) colisión con piso
        if b["y"] + r > H:
            b["y"] = H - r
            b["vy"] = -b["vy"] * RESTITUCION        #pierde velocidad  amortigua
            # Umbral para evitar vibración cuando casi se detiene
            if abs(b["vy"]) < 20:
                b["vy"] = 0

        # 6) colisión con techo
        if b["y"] - r < 0:
            b["y"] = r
            b["vy"] = -b["vy"] * RESTITUCION      #pierde velocidad  amortigua

def dibujar():
    """Dibuja fondo, piso, bolas"""
    screen.fill((18,18,22))                      # fondo
    pygame.draw.rect(screen, (200,50,60), (0, H-6, W, 6))  # piso visual
    # bolas
    for b in bolas:
        pygame.draw.circle(screen, b["color"], (int(b["x"]), int(b["y"])), b["r"])

    # HUD con instrucciones
    lines = [
        "ESPACIO: lanzar bola hacia arriba desde el centro inferior",
        "Click IZQ y arrastrar: tirachinas | Click DER: impulso vertical",
        "R: reiniciar | ESC/cerrar: salir",
        f"Bolas: {len(bolas)}"
    ]
    y = 8
    for s in lines:
        img = font.render(s, True, (230,230,230))
        screen.blit(img, (10, y))
        y += 18
    pygame.display.flip()

# Variables para lanzamiento tipo tirachinas
arrastrando = False
p_inicio = (0, 0)

# Bucle principal
while True:
    dt = clock.tick(120) / 1000.0  # delta tiempo en segundos a 120 FPS máx

    # Entrada de usuario / eventos 
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit
            if e.key == pygame.K_r:
                bolas.clear()  # limpia todas las bolas
            if e.key == pygame.K_SPACE:
                # Lanza una bola vertical desde el centro inferior
                x0, y0 = W//2, H-16
                crear_bola(x0, y0, 0, -900)  # velocidad inicial hacia arriba

        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            # Inicio de arrastre para tirachinas
            arrastrando = True
            p_inicio = pygame.mouse.get_pos()

        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            # Fin del arrastre: calcula vector de lanzamiento
            p_fin = pygame.mouse.get_pos()
            dx = p_inicio[0] - p_fin[0]  # invertir para que arrastrar hacia abajo lance hacia arriba
            dy = p_inicio[1] - p_fin[1]
            fuerza = 3.0                 # factor de escala
            vx0 = dx * fuerza
            vy0 = dy * fuerza
            # Si el arrastre fue mínimo, usa un tiro vertical estándar
            if abs(vx0) + abs(vy0) < 50:
                vy0 = -900
            crear_bola(p_inicio[0], p_inicio[1], vx0, vy0)
            arrastrando = False

        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 3:
            # Click derecho: crea bola en el cursor con impulso vertical
            mx, my = pygame.mouse.get_pos()
            crear_bola(mx, my, 0, -900)

        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 2:
            # Click derecho: crea bola en el cursor con impulso vertical
            mx, my = pygame.mouse.get_pos()
            crear_bola(mx, my, 0, 900)


    #  Actualización de física 
    actualizar_bolas(dt)

    #  Render básico 
    dibujar()

    # Línea guía del tirachinas mientras se arrastra
    if arrastrando:
        mx, my = pygame.mouse.get_pos()
        pygame.draw.line(screen, (180,180,180), p_inicio, (mx, my), 2)
        pygame.draw.circle(screen, (180,180,180), p_inicio, 5, 1)
        pygame.display.flip()


# Analizar el codigo para implementar luego fisicas en el juego de proyecto final.