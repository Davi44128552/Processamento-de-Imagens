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