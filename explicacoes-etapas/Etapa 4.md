## Etapa 4 - Mostrar o Número

#### Explicando o código:

```python
cv2.putText(
    frame,
    f"Numero: {dedos}",
    (50, 80),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    (0, 255, 0),
    4
)
```

- O `putText` serve para escrever um texto em cima da imagem. No nosso caso vamos escrever o número de dedos levantados.
- Agora explicando os parâmetros:
  - `frame` é a imagem onde o texto será desenhado
  - `f"Número: {dedos}"` é o texto que será mostrado
  - `(50, 80)` é a posição onde o texto aparece na tela, o primeiro valor é o eixo X (distância da esquerda da tela) e o segundo valor o eixo Y (distância do topo da tela)
  - `cv2.FONT_HERSHEY_SIMPLEX` é o estilo da fonte do texto que escolhemos
  - `2` é o tamanho da fonte
  - `(0, 255, 0)` é a cor do texto em RGB (nesse caso colocamos verde)
  - `4` é a grossura da letra

- Na etapa anterior printavamos o numero no terminal, agora temos ele exibido na tela

#### Sugestão de desafios

Desafios para evoluir:

- Detectar duas mãos
- Reconhecer números de 0 a 10
- Mudar a cor do texto conforme o número
- Criar gestos especiais
