import cv2                          # Librería para manejo de video e imágenes
import mediapipe as mp              # Librería de visión por computador de Google

# INICIALIZACIÓN MEDIAPIPE

# Accedemos al módulo de Face Mesh dentro de MediaPipe
mp_face_mesh = mp.solutions.face_mesh

# Creamos el objeto FaceMesh con configuración
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,        # False = modo video (mejor rendimiento con tracking)
    max_num_faces=1,                # número máximo de caras a detectar
    refine_landmarks=True,          # mejora precisión en ojos y labios (más puntos)
    min_detection_confidence=0.5,   # confianza mínima para detectar rostro
    min_tracking_confidence=0.5     # confianza mínima para hacer tracking entre frames
)

# Utilidad para dibujar (líneas, puntos, etc.)
mp_drawing = mp.solutions.drawing_utils


# INICIALIZACIÓN CÁMARA

# Abrir la cámara (CAP_DSHOW mejora compatibilidad en Windows)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Verificamos si la cámara se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

# Configuración del formato de video (MJPG reduce carga en CPU)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Configuración de resolución
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Presiona 'q' para salir.")


# BUCLE PRINCIPAL (VIDEO)

while True:

    # Leer un frame de la cámara
    ret, frame = cap.read()

    # Si no se pudo leer, se rompe el bucle
    if not ret:
        print("Error al leer frame.")
        break

    # Voltear horizontalmente (efecto espejo)
    frame = cv2.flip(frame, 1)

    # PREPROCESAMIENTO PARA MEDIAPIPE

    # MediaPipe trabaja en RGB, OpenCV en BGR → conversión necesaria
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesamos el frame para detectar cara y landmarks
    results = face_mesh.process(rgb_frame)


    # DIBUJO DE LANDMARKS

    # Verifica si detectó al menos una cara
    if results.multi_face_landmarks:

        # Recorremos cada cara detectada (aunque aquí solo usamos 1)
        for face_landmarks in results.multi_face_landmarks:

            # OPCIÓN 1: Dibujar malla completa

            # Dibuja los puntos y las conexiones (triángulos)
            mp_drawing.draw_landmarks(
                image=frame,                         # imagen donde dibujar
                landmark_list=face_landmarks,        # lista de puntos faciales
                connections=mp_face_mesh.FACEMESH_TESSELATION,  # malla triangular
                landmark_drawing_spec=None,          # no dibuja puntos individuales grandes
                connection_drawing_spec=mp_drawing.DrawingSpec(
                    color=(0, 255, 0),               # color verde
                    thickness=1,                     # grosor de líneas
                    circle_radius=1                  # radio de puntos
                )
            )

            # OPCIÓN 2: Dibujar SOLO puntos

            """
            h, w, _ = frame.shape   # obtener dimensiones del frame

            for lm in face_landmarks.landmark:
                # lm.x y lm.y están normalizados [0,1]
                x = int(lm.x * w)   # convertir a coordenadas reales
                y = int(lm.y * h)

                # Dibujar cada punto como círculo
                cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
            """


            # EXTRAER COORDENADAS NUMÉRICAS
            """
            puntos = []

            for lm in face_landmarks.landmark:
                puntos.append((lm.x, lm.y, lm.z))

            # Aquí se tienen los 468 puntos en formato numérico
            # Para:
            # - calcular distancias
            # - alimentar un modelo
            # - guardar en CSV
            """


    # MOSTRAR RESULTADO

    cv2.imshow("Puntos Faciales - MediaPipe", frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# CIERRE SEGURO

cap.release()               # liberar cámara
cv2.destroyAllWindows()     # cerrar ventanas