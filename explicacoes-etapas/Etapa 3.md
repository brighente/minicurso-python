## Etapa 3 - Contar os Dedos

#### Explicando o código:

```python
pontos = []
```

- Primeiro vamos guardar todos os 21 landmarks em uma lista. Assim, fica muito mais fácil acessar qualquer ponto da mão quando precisarmos.

```python
for landmark in hand_landmarks.landmark:
    x = int(landmark.x * largura)
    y = int(landmark.y * altura)

    pontos.append((x, y))
```

- Cada landmark possui uma posição X e Y. Nós convertemos essas coordenadas para pixels e armazenamos tudo na lista `pontos`.
- No final teremos algo como:
  - pontos[0] = (320, 420)
  - pontos[1] = (315, 390)
  - pontos[20] = (500, 180)

```python
dedos = 0
```

- Essa variável vai armazenar quantos dedos encontramos levantados.

-> Antes de seguir, vale explicar que 4, 8, 12, 16, 20 são as posições das bolinhas (dos pontos) do topo de cada dedo, sendo 4 a do polegar, e as demais dos demais dedos (indicador, médio, anelar e mindinho)

```python
if pontos[4][0] > pontos[3][0]:
    dedos += 1
```

- Vocês lembram que eu comentei que o polegar seria diferente?
- Diferente dos outros dedos, ele aponta para o lado. Então, ao invés de comparar a altura (`Y`), comparamos a posição horizontal (`X`).
- Se a ponta estiver mais para a direita (na mão direita), consideramos que ele está levantado.

```python
pontas = [8, 12, 16, 20]

for ponta in pontas:
```

- Aqui colocamos apenas os IDs das pontas dos outros quatro dedos.
- 8, 12, 16, 20 são as posições dos pontos do topo dos dedos (exceto do dedão, que é 4)
- O for, a lógica de verificar se está levantado ou não vai se repetir para cada dedo

```python
if pontos[ponta][1] < pontos[ponta - 2][1]:
    dedos += 1
```

- Lembram do slide em que vimos que um dedo levantado tem a ponta acima da articulação? É exatamente isso que essa linha faz.
- No OpenCV o eixo Y (altura) cresce para baixo, ou seja, quanto menor o número, mais alto está
- Ou seja, exemplo com o dedo indicador (8):
  - Pegamos a ponta (`pontos[8][1]`)
  - Vemos se é menor do que a articulação, que é sempre o ponto - 2 do topo do dedo (`pontos[ponta - 2][1])
  - Esse `[1]` que temos em ambas as partes da comparação é para pegarmos apenas o valor da posição vertical (`Y`)

```python
print(f"Dedos levantados: {dedos}")
```

- Por enquanto, vamos apenas imprimir no terminal. Na próxima etapa, vamos deixar isso mais bonito e mostrar diretamente na imagem da câmera.
