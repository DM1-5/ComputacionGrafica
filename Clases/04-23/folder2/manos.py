# Importar las bibliotecas necesarias

#pip install opencv-python

import cv2  # Para el manejo de imágenes y video
import mediapipe as mp  # Para la detección de manos

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()  # Crear un objeto Hands
mp_drawing = mp.solutions.drawing_utils  # Utilidades para dibujar

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)  # 0 para la cámara predeterminada

while cap.isOpened():  # Mientras la cámara esté abierta
    ret, frame = cap.read()  # Leer un frame de la cámara
    if not ret:  # Si no se pudo leer el frame
        break  # Salir del bucle

    #frame = cv2.flip(frame, 1)  # Voltear el frame horizontalmente
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir el frame a RGB
    results = hands.process(rgb_frame)  # Procesar el frame para detectar manos

    # Si se detectan manos
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:  # Para cada mano detectada
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)  # Dibujar los puntos de la mano

    cv2.imshow('Hand Detection', frame)  # Mostrar el frame con la detección de manos

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Salir si se presiona 'q'
        break

# Liberar la captura y cerrar las ventanas
cap.release()  # Liberar la cámara
cv2.destroyAllWindows()  # Cerrar todas las ventanas