import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PIL import Image
import numpy as np
# import matplotlib.pyplot as plt
from algorithms import intensity_transformations as it
from algorithms import histogram as hist
from algorithms.spatial_filtering import *

# Lendo a imagem e a convertendo para matriz de cores
image = Image.open("test_images/calopsita.jpg")
image = image.convert("L")
matriz_cores = np.array(image)
# matriz_cores2 = it.negative(matriz_cores)
# matriz_cores3 = it.thresholding(matriz_cores)
# matriz_cores4 = it.logarithm_transformation(matriz_cores)
# matriz_cores5 = it.power_law_transformation(matriz_cores, 2.2)
# matriz_cores6 = it.contrast_stretching(matriz_cores)
# matriz_cores7 = it.intensity_level_slicing(matriz_cores, 160, 250, "binary")
# matriz_cores8 = it.intensity_level_slicing(matriz_cores, 160, 250, "preserve")
# matriz_cores9 = it.bit_plane_slicing(matriz_cores, 6)
# matriz_cores10 = it.steganography_apply(matriz_cores, "Teste")
# matriz_cores11 = hist.histogram_equalization(matriz_cores)
# matriz_cores12 = convolution(matriz_cores, np.array([[-2, -1,  0],
#                           [-1,  1,  1],
#                           [ 0,  1,  2]], dtype=np.float32))
# matriz_cores13 = mean_filter(matriz_cores, 55)
matriz_cores14 = gaussian_smoothing(matriz_cores, 55, 23.0)
# matriz_cores2 = matriz_cores2.astype(np.uint8)
# matriz_cores3 = matriz_cores3.astype(np.uint8)
# matriz_cores4 = matriz_cores4.astype(np.uint8) 
# matriz_cores5 = matriz_cores5.astype(np.uint8)
# matriz_cores6 = matriz_cores6.astype(np.uint8)
# matriz_cores7 = matriz_cores7.astype(np.uint8)
# matriz_cores8 = matriz_cores8.astype(np.uint8)
# matriz_cores9 = matriz_cores9.astype(np.uint8)
# matriz_cores10 = matriz_cores10.astype(np.uint8)
# matriz_cores11 = matriz_cores11.astype(np.uint8)
# Convertendo novamente para imagem
# image = Image.fromarray(matriz_cores)
# image2 = Image.fromarray(matriz_cores2)
# image3 = Image.fromarray(matriz_cores3)
# image4 = Image.fromarray(matriz_cores4)
# image5 = Image.fromarray(matriz_cores5)
# image6 = Image.fromarray(matriz_cores6)
# image7 = Image.fromarray(matriz_cores7)
# image8 = Image.fromarray(matriz_cores8)
# image9 = Image.fromarray(matriz_cores9)
# image10 = Image.fromarray(matriz_cores10)
# image11 = Image.fromarray(matriz_cores11)
# image12 = Image.fromarray(matriz_cores12)
# image13 = Image.fromarray(matriz_cores13)
image14 = Image.fromarray(matriz_cores14)
# Mostrando o resultado
# image.show()
# image2.show()
# image3.show()
# image4.show()
# image5.show()
# image6.show()
# image7.show()
# image8.show()
# image11.show()
# image12.save("test_images/resultado12.bmp")
# image13.save("test_images/resultado13.bmp")
image14.save("test_images/imagem14.bmp")
# image10.save("test_images/imagem10.bmp")
# print(it.steganography_decoder(matriz_cores10))
