# Importing the necessary libraries
import numpy as np
from PIL import Image

# Function that convert image into matrix
def conversion_to_matrix(file_path: str) -> np.ndarray:
    image = Image.open(file_path)
    image = image.convert("L")
    colors_matrix = np.array(image)
    return colors_matrix

# Function that convert matrix to image
def conversion_to_image(matrix: np.ndarray):
    matrix = matrix.astype(np.uint8)
    image = Image.fromarray(matrix)
    return image

# Function to convert [0, 255] to [0, 1]
def convert_scales1(matrix: np.ndarray):
    final_matrix = matrix / 255
    return final_matrix

# Function to convert [0, 1] to [0, 255]
def convert_scales2(matrix: np.ndarray):
    final_matrix = matrix * 255
    return final_matrix