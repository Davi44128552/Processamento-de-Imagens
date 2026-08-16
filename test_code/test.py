import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PIL import Image
import numpy as np
from algorithms import intesity_transformations as it

# Lendo a imagem e a convertendo para matriz de cores
image = Image.open("test_images/calopsita.jpg")
image = image.convert("L")
matriz_cores = np.array(image)
matriz_cores2 = it.negative(matriz_cores)
matriz_cores3 = it.thresholding(matriz_cores)
matriz_cores4 = it.logarithm_transformation(matriz_cores)
matriz_cores5 = it.power_law_transformation(matriz_cores, 2.2)
# matriz_cores = it.thresholding(matriz_cores, 128)
matriz_cores2 = matriz_cores2.astype(np.uint8)
matriz_cores3 = matriz_cores3.astype(np.uint8)
matriz_cores4 = matriz_cores4.astype(np.uint8)
matriz_cores5 = matriz_cores5.astype(np.uint8)
# Convertendo novamente para imagem
image = Image.fromarray(matriz_cores)
image2 = Image.fromarray(matriz_cores2)
image3 = Image.fromarray(matriz_cores3)
image4 = Image.fromarray(matriz_cores4)
image5 = Image.fromarray(matriz_cores5)
# Mostrando o resultado
image.show()
image2.show()
image3.show()
image4.show()
image5.show()
