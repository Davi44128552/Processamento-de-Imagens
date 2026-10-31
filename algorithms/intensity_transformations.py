# Importing the necessary libraries
import numpy as np
from .aux_functions import runs_rgb

# Implementing intesity transfomation functions
# Thresholding
@runs_rgb
def thresholding(img_matrix: np.ndarray, T: int = 128) -> np.ndarray:

    # Checking if T is NOT between 0 and 255
    if (not(0 <= T <= 255)):
        print("O valor de T não está dentro do intervalo permitido! (Escolha um valor entre 0 e 255)")
        return img_matrix

    # Using numpy method "where" to apply the condition to change colors
    condition = img_matrix < T
    final_matrix = np.where(condition, 0, 255)

    # Returning the final matrix
    return final_matrix.astype(np.uint8)

# Negative
def negative(img_matrix: np.ndarray, L = None) -> np.ndarray:

    # Defining the value of L
    # L is defined by the image's bit depth and the formula is 2^k where k is the bit depth
    if L is None:
        L = 2 ** (img_matrix.itemsize * 8) # if uint8, itemsize = 1; if uint16, itemsize = ; ...

    # Applying the formula given by the book
    final_matrix = L - 1 - img_matrix

    # Returning the final matrix
    return final_matrix

# Brightness
@runs_rgb
def brightness(img_matrix: np.ndarray, k: float = 1) -> np.ndarray:

    # Just mutiply the matrix by the constant k
    # Adding 0 and 255 to avoid overflow errors
    final_matrix = np.clip(img_matrix * k, 0, 255)

    # Returning the final matrix
    return final_matrix.astype(np.uint8)

# Logarithm
@runs_rgb
def logarithm_transformation(img_matrix: np.ndarray, c = None) -> np.ndarray:

    # According to the book, the logarithm transformation is defined by c log (1 + r)
    # We define the constant c by the formula c = 255 / (log(1 + rmax))

    # Taking the rmax
    rmax = float(np.max(img_matrix)) # Converting to float to avoid overflow errors

    # Calculating c value
    if (c is None):
        c = 255 / (np.log(1 + rmax))

    # Applying the formula to generate the new matrix
    final_matrix = c * np.log(1 + img_matrix.astype(float))

    # Returning the final matrix
    return final_matrix.astype(np.uint8)

# Power-law (gamma)
@runs_rgb
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
    # piecewise linear transformation
@runs_rgb
def piecewise_linear(img_matrix: np.ndarray, control_points: list) -> np.ndarray:

    # Sorting the tuple according to r values
    sorted_list = sorted(control_points, key = lambda x : x[0])

    # Checking if the values are valid
    if ((sorted_list[0][0] != 0) or (sorted_list[len(sorted_list) - 1][0] != 255)):
        print("Faltam os pontos inicial e final!")
        return

    # Constructing the Look-Up Table
    LUT = np.zeros(256, dtype = np.float64)

    for i in range(0, len(sorted_list) - 1):

        # Taking the adjacent points
        point_one = sorted_list[i]
        point_two = sorted_list[i + 1]

        # Calculating slope according to formula: m = (s_k - s_(k-1)) / (r_k - r_(k-1))
        # If rk and r_(k+1) are equal, we avoid division by 0 defining slope as 0
        if (point_two[0] == point_one[0]):
            slope = 0.0
        else:
            # Applying the formula
            slope = (point_two[1] - point_one[1]) / (point_two[0] - point_one[0])

        # Applying linear mapping in each element of LUT
        for j in range(point_one[0], point_two[0] + 1):
            LUT[j] = point_one[1] + slope * (j - point_one[0])

    # Applying the Look-Up Table into the image
    final_matrix = np.round(LUT[img_matrix])
    final_matrix = np.clip(final_matrix, 0, 255)

    # Returning the final matrix
    return final_matrix.astype(np.uint8)

    # Constrast stretching
@runs_rgb
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
@runs_rgb
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
@runs_rgb
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
    final_matrix = np.where(condition, 255, 0)

    # Returning the final image
    return final_matrix.astype(np.uint8)

# Steganography
def steganography_apply(img_matrix: np.ndarray, message: str) -> np.ndarray:
    
    # Steganography involves converting a message into binary and adding it to the least significant bit (LSB) of the image

    # Adding a terminator to the message (this will be important for decode)
    message += '\x00'

    # Converting the string message into binary
    binary_list = []
    for char in message:
        ascii_code = ord(char)
        binary_code = format(ascii_code, '08b')

        for bit in binary_code:
            binary_list.append(int(bit))

    # Converting the matrix to 1D to facilitate the message addition process
    img_oned = img_matrix.flatten()

    # Checking if the message fits in the image
    if (len(img_oned) < len(binary_list)):
        print("Erro! A mensagem é muito grande para a imagem requisitada!")
        return img_matrix

    # Taking the first n pixels and changing them
    pixels_changed = img_oned[0:len(binary_list)]
    pixels_changed = (pixels_changed & 254) | np.array(binary_list)

    # Changing the original bits to the new ones
    img_oned[0:len(binary_list)] = pixels_changed

    # Converting the matrix to 2D
    final_matrix = img_oned.reshape(img_matrix.shape)

    # Returning the result
    return final_matrix.astype(np.uint8)

def steganography_decoder(img_matrix: np.ndarray) -> str:

    # In this function, we will take the LSB from the image and try to find the message
    message = ""

    # Converting the matrix into 1D (again)
    img_oned = img_matrix.flatten()

    # Extracting the LSB from the image
    matrix_lsb = img_oned & 1

    # traversing the pixels of the image to obtain the message
    for i in range(0, len(matrix_lsb), 8): # each pixel has 8 bits

        # Converting the 8 bits into string
        char_list = matrix_lsb[i:i+8]
        char_string = "".join(char_list.astype(str))

        # Converting the char into ascii code
        ascii_char = int(char_string, 2)

        # Checking if there's more hidden message or don't
        if (ascii_char == 0): # if char = \x00, then we got the whole message
            break

        # Otherwise, we add the string to the message
        message += chr(ascii_char)

    # Returning the final message
    return message