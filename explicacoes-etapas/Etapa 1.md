## Etapa 0 - Antes de Codar

#### Comandos para preparar ambiente

-> Instalar o Python:
https://www.python.org/downloads/
Versão 3.15, durante a instalação marcar o 'Add Python to PATH'

-> Verificar se a instalação deu certo:

```bash
python --version

# caso não funcione
python3 --version
```

-> Criar uma pasta para o projeto e abrir ela no VS Code ou qualquer IDE

-> Em um terminal dentro da pasta, rodar:

```bash
python -m venv venv

# caso não funcione
python3 -m venv venv
```

-> Ativar o ambiente:

```bash
venv\Scripts\activate

# linux
source venv/bin/activate
```

- Deve aparecer no terminal, na frente do caminho da pasta, algo como '(venv)'

-> Instalar bibliotecas python

```bash
pip install "opencv-python<5" "mediapipe==0.10.21"
# ou
pip install -r requirements.txt
```

## Etapa 1 - Abrir a câmera

```python
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
```

#### Explicando o código:

- "Primeiro importamos o `cv2`, que é o OpenCV. Ele vai ser responsável por conversar com a câmera e mostrar a imagem para nós"
- "Depois criamos a variável `camera` usando `cv2.VideoCapture(0)`. Esse `0` representa a câmera padrão do computador. Se a pessoa tiver mais de uma câmera, poderia ser `1`, `2` e assim por diante."
- "Em seguida criamos um `while True`, porque vídeo nada mais é do que várias imagens passando muito rápido. Cada repetição desse loop pega uma nova imagem da câmera."
- "A linha `sucesso, frame = camera.read()` tenta capturar uma imagem. O `sucesso` diz se deu certo ou não, e o `frame` é a imagem capturada naquele momento."
- "Depois usamos `cv2.imshow()` para mostrar esse frame em uma janela."
- "A linha com `cv2.waitKey(1)` fica verificando se alguma tecla foi pressionada. Nesse caso, se a tecla for `ESC`, o programa fecha."
- "Por fim, usamos `camera.release()` para liberar a câmera e `cv2.destroyAllWindows()` para fechar as janelas abertas pelo OpenCV."
