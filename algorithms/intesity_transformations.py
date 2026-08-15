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

def negative(img_matrix: np.ndarray) -> np.darray:

    # Defining the value of L
    # L is defined by the image's bit depth and the formula is 2^k where k is the bit depth
    L = 2 ** (img_matrix.itemsize * 8) # if uint8, itemsize = 1; if uint16, itemsize = ; ...

    # Applying the formula given by the book
    final_matrix = L - 1 - img_matrix

    # Returning the final matrix
    return final_matrix