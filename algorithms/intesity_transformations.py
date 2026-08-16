# Importing the necessary libraries
import numpy as np

# Implementing intesity transfomation functions
# Thresholding
def thresholding(img_matrix: np.ndarray, T: int = 128) -> np.ndarray:

    # Checking if T is NOT between 0 and 255
    if (not(0 <= T <= 255)):
        print("O valor de T não está dentro do intervalo permitido! (Escolha um valor entre 0 e 255)")

    # Using numpy method "where" to apply the condition to change colors
    final_matrix = np.where(img_matrix < T, 0, 255)

    # Returning the final matrix
    return final_matrix

# Negative
def negative(img_matrix: np.ndarray) -> np.ndarray:

    # Defining the value of L
    # L is defined by the image's bit depth and the formula is 2^k where k is the bit depth
    L = 2 ** (img_matrix.itemsize * 8) # if uint8, itemsize = 1; if uint16, itemsize = ; ...

    # Applying the formula given by the book
    final_matrix = L - 1 - img_matrix

    # Returning the final matrix
    return final_matrix

# Logarithm
def logarithm_transformation(img_matrix: np.ndarray) -> np.ndarray:

    # According to the book, the logarithm transformation is defined by c log (1 + r)
    # We define the constant c by the formula c = 255 / (log(1 + rmax))

    # Taking the rmax
    rmax = float(np.max(img_matrix)) # Converting to float to avoid overflow errors

    # Calculating c value
    c = 255 / (np.log(1 + rmax))

    # Applying the formula to generate the new matrix
    final_matrix = c * np.log(1 + img_matrix.astype(float))

    # Returning the final matrix
    return final_matrix.astype(np.uint8)

# Power-law (gamma)
def power_law_transformation(img_matrix: np.ndarray, gamma: float = 1) -> np.ndarray:

    # According to the book, the power-law (gamma) transformation is defined by c r^gamma

    # Taking the rmax
    rmax = float(np.max(img_matrix)) # Converting to float to avoid overflow errors

    # If rmax = 0, we just return the input image
    if (rmax == 0):
        return img_matrix

    # Calculating c value
    c = 255 / (rmax ** gamma)

    # Applying the formula
    final_matrix = c * (img_matrix.astype(float) ** gamma)

    # Returning the final matrix
    return final_matrix.astype(np.uint8)
