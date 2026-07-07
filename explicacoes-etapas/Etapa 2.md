## Etapa 2 - Detectando a mão

#### Explicando o código:

```python
import mediapipe as mp
```

- Além do OpenCV, agora vamos usar o MediaPipe.
- Ele já possui um modelo de IA treinado e é exatamente esse modelo que vamos utilizar agora.

```python
mp_hands = mp.solutions.hands
```

- O MediaPipe possui vários módulos.
- Existe um para rosto, outro para corpo, outro para pose
- Nós vamos utilizar apenas o módulo de mãos.

```python
mp_draw = mp.solutions.drawing_utils
```

- O MediaPipe consegue detectar os pontos, mas quem desenha esses pontos na tela é essa biblioteca auxiliar.

```python
hands = mp_hands.Hands(
max_num_hands=1,
min_detection_confidence=0.7,
min_tracking_confidence=0.7
)
```

- Aqui estamos criando nosso detector de mãos.
  `max_num_hands=1` - Queremos detectar apenas uma mão.
  `min_detection_confidence` - É a confiança mínima para considerar que realmente encontrou uma mão.
  `min_tracking_confidence` - Depois que a mão foi encontrada, qual a confiança mínima para continuar acompanhando ela. - Esses valores de confidence variam de 0 até 1. Quanto maior, mais exigente o detector fica

```python
frame = cv2.flip(frame, 1)
```

- Quando olhamos no espelho, levantamos a mão direita e ela continua sendo a direita, certo?"
- Sem essa linha, a câmera fica invertida.
- Então espelhamos a imagem para ficar natural para quem está usando.

```python
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
```

- O OpenCV trabalha com um formato chamado BGR.
- Já o MediaPipe espera receber uma imagem em RGB.
- Então fazemos apenas uma tradução entre esses dois formatos.
- É como se fosse duas pessoas falando idiomas diferentes.

```python
resultado = hands.process(frame_rgb)
```

- Aqui acontece toda a "mágica".
- Enviamos a imagem para o MediaPipe, e ele responde dizendo se encontrou ou não uma mão.

```python
if resultado.multi_hand_landmarks:
```

- Aqui verificamos se existe uma mão na camêra
- Se não existe, não tem nada para desenhar

```python
for hand_landmarks in resultado.multi_hand_landmarks:
```

- Como configuramos apenas uma mão, esse `for` normalmente executa apenas uma vez.
- Mas se permitíssemos duas mãos, ele passaria por cada uma delas.

```python
mp_draw.draw_landmarks(...)
```

- Aqui não estamos detectando nada.
- Apenas desenhando os pontos que o MediaPipe encontrou.
- Esses pontos não são desenhados pela câmera. Eles são desenhados por nós, usando as informações que o MediaPipe devolveu.
