import pygame
import cv2
import mediapipe as mp
import numpy as np

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mover cuadro con la mano")

# --- configuración ---
hand_size = (64, 64)
open_hand_img = pygame.image.load("open_hand.png").convert_alpha()
closed_hand_img = pygame.image.load("closed_hand.png").convert_alpha()
open_hand_img = pygame.transform.smoothscale(open_hand_img, hand_size)
closed_hand_img = pygame.transform.smoothscale(closed_hand_img, hand_size)

# mano y cuadro
hand_rect = pygame.Rect(0, 0, hand_size[0], hand_size[1])
hand_rect.center = (W // 2, H // 2)

box_rect = pygame.Rect(W // 2 - 50, H // 2 - 50, 100, 100)
dragging = False  # indica si el cuadro se está moviendo

# --- mediapipe ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

running = True
is_pinching = False

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        thumb_tip = hand_landmarks.landmark[4]
        index_tip = hand_landmarks.landmark[8]

        # distancia para detectar click
        dist = np.hypot(thumb_tip.x - index_tip.x, thumb_tip.y - index_tip.y)
        is_pinching = dist < 0.05

        # actualizar posición de la mano
        px = int(index_tip.x * W)
        py = int(index_tip.y * H)
        hand_rect.center = (px, py)

        # detectar si toca el cuadro
        if is_pinching and hand_rect.colliderect(box_rect):
            dragging = True
        elif not is_pinching:
            dragging = False

        # si se está moviendo, seguir la mano
        if dragging:
            box_rect.center = hand_rect.center

        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # --- dibujar pygame ---
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 0, 0), box_rect)  # cuadro rojo

    img = closed_hand_img if is_pinching else open_hand_img
    pygame.draw.rect(screen, (0, 255, 0), hand_rect, 2)
    screen.blit(img, hand_rect)

    pygame.display.flip()

    cv2.imshow("Camara", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.quit()
