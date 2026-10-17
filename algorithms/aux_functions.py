# Importing the necessary libraries
import numpy as np
from PIL import Image
import cv2
from functools import wraps

# Function that convert image into matrix
def conversion_to_matrix(file_path: str, matrix_type: str = "RGB") -> np.ndarray:
    image = Image.open(file_path)
    image = image.convert(matrix_type)
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