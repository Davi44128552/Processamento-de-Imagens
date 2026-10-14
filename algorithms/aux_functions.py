# Importing the necessary libraries
import numpy as np
from PIL import Image
import cv2

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

# Function to resize some image using another one as reference
def resize_image(img_matrix1: np.ndarray, img_matrix2: np.ndarray) -> np.ndarray:

    width = img_matrix1.shape[1]
    height = img_matrix1.shape[0]

    # Applying cv function to resize
    result_matrix = cv2.resize(img_matrix2, (width, height), interpolation = cv2.INTER_LINEAR)

    # Returning the result 
    return result_matrix.astype(np.uint8)