# Importing the necessary libraries
import numpy as np
from PIL import Image
import cv2
from functools import wraps

# Function that convert image into matrix
def conversion_to_matrix(file_path: str, matrix_type: str = "RGB") -> np.ndarray:
    image = Image.open(file_path)
    colors_matrix = np.array(image)
    if (matrix_type == "L"):
        from algorithms.colors_algorithms import gray_scale_weigthted_arithmetic_mean
        colors_matrix = gray_scale_weigthted_arithmetic_mean(colors_matrix)
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

    # Using scaling function
    from algorithms.geometric_operations import scaling
    sx = img_matrix2.shape[1] / img_matrix1.shape[1] 
    sy = img_matrix2.shape[0] / img_matrix1.shape[0] 

    result_matrix = scaling(img_matrix2, sx, sy, "bilinear")

    # Returning the result 
    return result_matrix.astype(np.uint8)

# Function to find the next power of two
def next_power_of_two(n: int) -> int:

    if (n == 0):
        return 1
    return 2 ** (n - 1).bit_length()

# Function that allows image processing algorithms that run on 2D matrices to run on color matrices.
def runs_rgb(function):

    @wraps(function)
    def wrapper(img_matrix: np.ndarray, *args, **kwargs):
        if len(img_matrix.shape) == 3:

            # Channels
            R = img_matrix[:, :, 0]
            G = img_matrix[:, :, 1]
            B = img_matrix[:, :, 2]

            # Applying the input function
            R_output = function(R, *args, **kwargs)
            G_output = function(G, *args, **kwargs)
            B_output = function(B, *args, **kwargs)

            # Merging the channels
            final_matrix = np.dstack((R_output, G_output, B_output))

        else:
            final_matrix = function(img_matrix, *args, **kwargs)

        # Returning the final matrix
        return final_matrix

    return wrapper

# Function to normalize
def normalize(matrix: np.ndarray) -> np.ndarray:

    min_value = np.min(matrix)
    max_value = np.max(matrix)

    if (max_value == min_value):
        return np.zeros(matrix.shape, dtype = np.uint8)

    return (matrix - min_value) / (max_value - min_value) * 255