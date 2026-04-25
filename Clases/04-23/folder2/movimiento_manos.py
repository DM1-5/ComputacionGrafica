import pygame
import cv2
import mediapipe as mp
import numpy as np

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Control de cubo con gestos")

# Configurar el cubo
cube_size = 50
cube_x = WINDOW_WIDTH // 2
cube_y = WINDOW_HEIGHT // 2
cube_color = (255, 0, 0)  # Rojoq

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Variable para controlar si el cubo está siendo movido
is_pinching = False

running = True
while running:
    # Manejo de eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar frame de la cámara
    ret, frame = cap.read()
    if not ret:
        continue

    # Voltear el frame horizontalmente para una vista tipo espejo
    frame = cv2.flip(frame, 1)
    
    # Convertir la imagen a RGB (MediaPipe requiere RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Procesar el frame para detectar manos
    results = hands.process(rgb_frame)

    # Si se detectan manos
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Obtener las coordenadas de los dedos pulgar e índice
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]

            # Calcular la distancia entre los dedos
            distance = np.sqrt(
                (thumb_tip.x - index_tip.x)**2 + 
                (thumb_tip.y - index_tip.y)**2
            )

            # Si los dedos están cerca (pinching)
            if distance < 0.05:  # Ajusta el valor
                is_pinching = True
                # Mover el cubo según la posición del dedo índice
                cube_x = int(index_tip.x * WINDOW_WIDTH)
                cube_y = int(index_tip.y * WINDOW_HEIGHT)
            else:
                is_pinching = False

            # Dibujar los puntos de referencia de la mano
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Limpiar la pantalla de Pygame
    screen.fill((255, 255, 255))  # Fondo blanco

    # Dibujar el cubo
    pygame.draw.rect(screen, cube_color, (cube_x - cube_size//2, cube_y - cube_size//2, cube_size, cube_size))

    # Actualizar la pantalla
    pygame.display.flip()

    # Mostrar el frame de la cámara
    cv2.imshow("Camara", frame)
    
    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpieza
cap.release()
cv2.destroyAllWindows()
pygame.quit()