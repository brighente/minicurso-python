# Detector de Números com as Mãos

Projeto desenvolvido como demonstração prática para um minicurso de Python, utilizando Visão Computacional para reconhecer números feitos com a mão em tempo real.

O projeto utiliza a webcam do computador para detectar uma mão, identificar os dedos levantados e exibir na tela o número correspondente.

## Tecnologias utilizadas

- Python 3.12+
- OpenCV
- MediaPipe

## Como funciona

O funcionamento da aplicação pode ser resumido em quatro etapas:

1. Captura da imagem da webcam utilizando o OpenCV.
2. Detecção da mão e dos seus 21 landmarks através do MediaPipe.
3. Comparação das coordenadas dos dedos para identificar quais estão levantados.
4. Exibição do número detectado sobre a imagem da câmera.

## Preparando o ambiente

### Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd minicurso-python
```

### Crie um ambiente virtual

#### Windows

```bash
python -m venv venv
```

#### Linux / macOS

```bash
python3 -m venv venv
```

### Ative o ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

## Executando o projeto

Cada etapa pode ser executada individualmente.

Exemplo:

```bash
python etapa1.py
```

ou

```bash
python etapa4.py
```

## Dependências

Arquivo `requirements.txt`:

```txt
opencv-python<5
mediapipe==0.10.21
```

## Limitações

Este projeto foi desenvolvido com fins didáticos para um minicurso e utiliza uma lógica simplificada para identificar os dedos levantados.

Algumas limitações conhecidas:

- A lógica do polegar foi simplificada e funciona corretamente apenas para uma orientação específica da mão.
- O reconhecimento considera apenas uma mão por vez.
- O sistema reconhece números de **0 a 5**.

## Possíveis melhorias

Algumas evoluções possíveis para o projeto:

- Reconhecimento correto de mão direita e esquerda.
- Reconhecimento de duas mãos simultaneamente.
- Reconhecimento de gestos personalizados.
- Contagem de números até 10 utilizando ambas as mãos.
- Interface gráfica mais elaborada.

## Licença

Este projeto foi desenvolvido exclusivamente para fins educacionais e de demonstração.
