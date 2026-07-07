import cv2

# Passo 1: acessar a câmera do computador
camera = cv2.VideoCapture(0)

while True:
    # Captura um frame da câmera
    sucesso, frame = camera.read()

    # Se não conseguiu capturar imagem, encerra o loop
    if not sucesso:
        print("Não foi possível acessar a câmera.")
        break

    # Mostra a imagem da câmera em uma janela
    cv2.imshow("Detector de Numeros com as Maos", frame)

    # Se apertar ESC, fecha o programa
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Libera a câmera e fecha as janelas
camera.release()
cv2.destroyAllWindows()