import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PIL import Image
import numpy as np
from algorithms import intesity_transformations as it

# Lendo a imagem e a convertendo para matriz de cores
image = Image.open("test_images/calopsita.jpg")
image = image.convert("RGB")
image.show()
matriz_cores = np.array(image)
matriz_cores = it.negative(matriz_cores)
# matriz_cores = it.thresholding(matriz_cores, 128)
matriz_cores = matriz_cores.astype(np.uint8)
# Convertendo novamente para imagem
image = Image.fromarray(matriz_cores)
# Mostrando o resultado
image.show()