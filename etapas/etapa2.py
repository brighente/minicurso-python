import cv2
import mediapipe as mp

# Inicializa a câmera
camera = cv2.VideoCapture(0)

# Inicializa o MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

while True:
    sucesso, frame = camera.read()

    if not sucesso:
        print("Não foi possível acessar a câmera.")
        break

    # Espelha a imagem para ficar mais natural
    frame = cv2.flip(frame, 1)

    # Converte BGR para RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa a imagem procurando mãos
    resultado = hands.process(frame_rgb)

    # Se encontrou uma mão...
    if resultado.multi_hand_landmarks:

        # Percorre todas as mãos encontradas
        for hand_landmarks in resultado.multi_hand_landmarks:

            # Desenha os pontos e as conexões
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Detector de Numeros", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()
