# Importing the necessary libraries
import numpy as np

# Implementing intesity transfomation functions
# Thresholding
def thresholding(img_matrix: np.ndarray, T: int = 128) -> np.ndarray:

    # Checking if T is NOT between 0 and 255
    if (not(0 <= T <= 255)):
        print("O valor de T não está dentro do intervalo permitido! (Escolha um valor entre 0 e 255)")
        return img_matrix

    # Using numpy method "where" to apply the condition to change colors
    condition = img_matrix < T
    final_matrix = np.where(condition, 0, 255)

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
    return final_matrix.astype(img_matrix.dtype)

# Piecewise Linear Transformation Functions
    # Constrast stretching
def contrast_stretching(img_matrix: np.ndarray) -> np.ndarray:

    # This method consists of taking the rmin of the image and stretching it to imin, and take the rmax of the image and stretching it to imax
    # This method can be described by the formula s = (r - rmin) * ((Imax - Imin) / (rmax - rmin)) + Imin

    # Taking the values of Imax and Imin
    imax = float(np.iinfo(img_matrix.dtype).max)
    imin = float(np.iinfo(img_matrix.dtype).min)

    # Taking the values of rmax and rmin
    rmax = float(np.max(img_matrix))
    rmin = float(np.min(img_matrix))

    # If rmax = rmin, we just return the image
    if (rmax == rmin):
        return img_matrix

    # Applying the formula do define the new matrix
    final_matrix = (img_matrix.astype(float) - rmin) * ((imax - imin) / (rmax - rmin)) + imin

    # Returning the final result
    return final_matrix.astype(img_matrix.dtype)

    # Intensity-Level Slicing
def intensity_level_slicing(img_matrix: np.ndarray, min_value: int, max_value: int, alg_type: str) -> np.ndarray:

    # This method takes a range, and each pixel within that range has the value 255, while the others have the value 0
    # This method implementation logic is equal to thresholding

    # Checking if the min and max values are right
    if (not(0 <= min_value <= 255)):
        print("O valor mínimo não está dentro do intervalo permitido! (Escolha um valor entre 0 e 255)")
        return img_matrix

    if (not(0 <= max_value <= 255)):
        print("O valor máximo não está dentro do intervalo permitido! (Escolha um valor entre 0 e 255)")
        return img_matrix

    # Checking if the min value is greater than max
    if (min_value > max_value):
         print("O valor mínimo não pode ser maior que o valor máximo!")
         return img_matrix

    # Applying the condition in the image
    condition = (min_value <= img_matrix) & (img_matrix <= max_value)

    # Checking what type of level slicing is and applying the right function
    if (alg_type.lower() == "binary"):
        final_matrix = np.where(condition, 255, 0)

    elif (alg_type.lower() == "preserve"):
        final_matrix = np.where(condition, 255, img_matrix)

    else:
        print("Opção inválida! As opções são binary e preserve")
        final_matrix = img_matrix

    # Returning the final matrix
    return final_matrix.astype(img_matrix.dtype)

    # Bit-Plane slicing
def bit_plane_slicing(img_matrix: np.ndarray, bit_reference: int) -> np.ndarray:

    # Checking if the bit_reference is a valid value
    if (not(0 <= bit_reference <= 7)):
        print("O valor informado para o valor do bit não é válido! Escolha um valor entre 0 e 7 (0 <= n <= 7)")
        return img_matrix

    # Calculating the mask according to bit reference value
    mask = 2 ** bit_reference

    # Applying the mask value in the image. If the bit exists, its value will be the mask value, otherwise, the value will be 0
    mask_image = img_matrix & mask

    # With mask image, we just take the non-zero values ​​and set the new value to 255.
    condition = (mask_image != 0)
    final_image = np.where(condition, 255, 0)

    # Returning the final image
    return final_image.astype(np.uint8)
