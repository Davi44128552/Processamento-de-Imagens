# Processamento-de-Imagens
Repositório dedicado a desenvolver códigos relacionado à disciplina de Processamento de Imagens (CK0167) da Universidade Federal do Ceará

# Trabalho 1
O trabalho 1 consiste em operações aplicadas na imagem de entrada. Na aplicação as seções são divididas da seguinte maneira:
 - Transformação de Intensidade
 - Histograma
 - Filtragem Espacial
 - Operações geométricas
 - Operações de domínio de frequência
 - Operações com cores

## Organização da aplicação
O código está organizado em duas pastas principais:
    - **algorithms**, contendo a lógica do programa, ou seja, onde os algoritmos de processamento de imagens estão sendo aplicados (O coração do trabalho)
    - **gui**, contendo os arquivos da interface gráfica, junto com a main, a qual roda a aplicação

## Como executar a aplicação?
Para executar a aplicação, deve-se seguir os seguintes passos:
1. Criar o ambiente env python e ativá-lo por meio dos comandos:
```python3 -m venv .venv```
```source .venv/bin/activate```

2. Instalar as dependências, através do comando abaixo:
```pip install -r requirements.txt```

3. Executar a aplicação, pelo comando abaixo:
```python3 gui/main.py```