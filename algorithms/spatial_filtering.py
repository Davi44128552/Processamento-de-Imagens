# Spatial filtering functions

# Importing the necessary libraries
import numpy as np
from algorithms.intensity_transformations import *
from .aux_functions import runs_rgb

# Convolution
@runs_rgb
def convolution(img_matrix: np.ndarray, filter: np.ndarray, float_result: bool = False) -> np.ndarray:

    # Checking if the filter dimensions are valid
    if ((filter.shape[0] % 2 == 0) or (filter.shape[1] % 2 == 0)):
        print("As dimensões do kernel devem ser ímpares!")
        return img_matrix

    # Creating a new matrix with padding
    new_rows = (filter.shape[0] - 1) // 2
    new_columns = (filter.shape[1] - 1) // 2
    new_matrix = np.pad(img_matrix, ((new_rows, new_rows), (new_columns, new_columns)), mode = 'edge')

    # Rotating the filter 
    convolution_filter = np.flip(filter)

    # Applying the filter in the image
    final_matrix = np.zeros((img_matrix.shape[0], img_matrix.shape[1]))

    for i in range(0, final_matrix.shape[0]):
        for j in range(0, final_matrix.shape[1]):

            # Taking the submatrix to apply the filter
            operation_matrix = new_matrix[i : i + filter.shape[0], j : j + filter.shape[1]]

            # Applying the operation
            product = operation_matrix * convolution_filter
            final_matrix[i][j] = np.sum(product)
            
    # Returning the final matrix
    if (float_result):
        return final_matrix.astype(np.float64)
    final_matrix = np.clip(final_matrix, 0, 255)
    return final_matrix.astype(np.uint8)

# Mean filter
@runs_rgb
def mean_filter(img_matrix: np.ndarray, dimension: int) -> np.ndarray:

    # Checking if the dimension is valid
    if (dimension % 2 == 0):
        print("A dimensão do filtro deve ser ímpar!")
        return img_matrix

    # Taking the number of elements
    n_elements = dimension * dimension

    # Creating the new matrix wit padding
    new_rows = (dimension - 1) // 2
    new_columns = (dimension - 1) // 2
    new_matrix = np.pad(img_matrix, ((new_rows, new_rows), (new_columns, new_columns)), mode = 'edge')

    # Applying the filter in the image
    final_matrix = np.zeros((img_matrix.shape[0], img_matrix.shape[1]))

    for i in range(0, final_matrix.shape[0]):
        for j in range(0, final_matrix.shape[1]):

            # Taking the submatrix to apply the filter
            operation_matrix = new_matrix[i : i + dimension, j : j + dimension]

            # Applying the operation
            elements_sum = np.sum(operation_matrix)
            mean_value = elements_sum // n_elements

            # Adding the value in the final matrix
            final_matrix[i][j] = mean_value

    # Returning the final matrix
    final_matrix = np.clip(final_matrix, 0, 255)
    return final_matrix.astype(np.uint8)

# Gaussian Smoothing
@runs_rgb
def gaussian_smoothing(img_matrix: np.ndarray, dimension: int, standard_deviation: float) -> np.ndarray:

    # Checking if the dimension is valid
    if (dimension % 2 == 0):
        print("A dimensão do filtro deve ser ímpar!")
        return img_matrix

    # Checking if the standard_deviation is valid
    if (standard_deviation <= 0):
        print("O valor do desvio padrão deve ser maior que 0!")
        return img_matrix

    # Constructing the kernel filter
    center = dimension // 2
    elements_sum = 0
    gauss_filter = np.zeros((dimension, dimension))
    for i in range(0, gauss_filter.shape[0]):
        for j in range(0, gauss_filter.shape[1]):
            x = i - center
            y = j - center

            # The resulting value is defined by the formula below
            gxy = (1 / (2 * np.pi * (standard_deviation ** 2))) * np.exp(-((x**2 + y**2) / (2 * (standard_deviation ** 2))))
            elements_sum += gxy

            # Adding the result in the filter matrix
            gauss_filter[i][j] = gxy

    # Normalizing the kernel
    gauss_filter = gauss_filter / elements_sum

    # Applying the filter
    final_matrix = gauss_filter

    # Returning the final matrix
    final_matrix = np.clip(final_matrix, 0, 255)
    return final_matrix.astype(np.uint8)

# Median filter
@runs_rgb
def median_filter(img_matrix: np.ndarray, dimension: int) -> np.ndarray:

    # Checking if the dimension is valid
    if (dimension % 2 == 0):
        print("O valor das dimensões da máscara deve ser ímpar!")
        return img_matrix

    # Taking the median position
    median_position = (dimension * dimension) // 2

    # Creating the new matrix wit padding
    new_rows = (dimension - 1) // 2
    new_columns = (dimension - 1) // 2
    new_matrix = np.pad(img_matrix, ((new_rows, new_rows), (new_columns, new_columns)), mode = 'edge')

    # Applying the kernel in the image
    final_matrix = np.zeros((img_matrix.shape[0], img_matrix.shape[1]))

    for i in range(0, final_matrix.shape[0]):
        for j in range(0, final_matrix.shape[1]):

            # Taking the submatrix to apply the filter
            operation_matrix = new_matrix[i : i + dimension, j : j + dimension]

            # Taking the median
            ordered_operation_matrix = operation_matrix.flatten()
            ordered_operation_matrix = np.sort(ordered_operation_matrix)
            median = ordered_operation_matrix[median_position]

            # Applying the operation
            final_matrix[i][j] = median

    # Returning the final matrix
    final_matrix = np.clip(final_matrix, 0, 255)
    return final_matrix.astype(np.uint8)

# Laplacian filter
@runs_rgb
def laplacian(img_matrix: np.ndarray, kernel: int, dimension_log: int, standard_deviation_log: float, log: bool = True) -> np.ndarray:

    # If LoG is true, we apply 
    if (log):
        img_matrix_input = gaussian_smoothing(img_matrix, dimension_log, standard_deviation_log)
    else:
        img_matrix_input = img_matrix

    img_matrix_input = img_matrix_input.astype(np.float64)

    # Choosing the kernel
    if (kernel == 1):
        kernel_apply = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    elif (kernel == 2):
        kernel_apply = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    elif (kernel == 3):
        kernel_apply = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        kernel_apply = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

    # Applying the filter
    final_matrix = convolution(img_matrix_input, kernel_apply, True)

    # Sharpening
    if (kernel == 1 or kernel == 2):
        # f(x, y) + c * d²f(x, y)
        final_matrix = img_matrix + final_matrix
    else:
        # f(x, y) - c * d²f(x, y)
        final_matrix = img_matrix - final_matrix

    # Normalizing
    min_value = np.min(final_matrix)
    if (min_value < 0):
        final_matrix = final_matrix + np.abs(min_value)
    max_value = np.max(final_matrix)
    if (max_value > 0):
        final_matrix = final_matrix / max_value

    final_matrix = final_matrix * 255

    # Returning the result
    return final_matrix.astype(np.uint8)

# High-boost
@runs_rgb
def high_boost(img_matrix: np.ndarray, dimension_gauss: int, k: float, standard_deviation_gauss: float) -> np.ndarray:

    # following the steps described in the book
    # 1. blur the image
    # Using mean filter
    blur_image = gaussian_smoothing(img_matrix, dimension_gauss, standard_deviation_gauss)

    # 2. subtracting the blurred image from the original
    # Converting the matrix
    img_matrix_converted = img_matrix.astype(np.float64)
    blur_image = blur_image.astype(np.float64)
    mask = img_matrix_converted - blur_image

    # Applying k to the mask
    mask = mask * k 

    # 3. Applying the mask to the image
    final_image = img_matrix_converted + mask

    # Adjusting the values ​​to be in the range [0, 255]
    final_image = np.clip(final_image, 0, 255)

    # Returning the result
    return final_image.astype(np.uint8)

# Sobel filtering
@runs_rgb
def sobel(img_matrix: np.ndarray, axis: str) -> np.ndarray:

    # Defining the sobel's kernels
    x_kernel = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])

    y_kernel = np.array([[1, 2, 1],
                         [0, 0, 0],
                         [-1, -2, -1]])


    if (axis == 'x'):

        # Applying the filter in the image
        x_filtered = convolution(img_matrix, x_kernel)

        # Normalizing the matrix
        x_filtered_normalized = x_filtered - np.min(x_filtered)
        x_filtered_normalized = (x_filtered_normalized / np.max(x_filtered_normalized)) * 255


    if (axis == 'y'):

        # Applying the filter in the image
        y_filtered = convolution(img_matrix, y_kernel)

        # Normalizing the matrix
        y_filtered_normalized = y_filtered - np.min(y_filtered)
        y_filtered_normalized = (y_filtered_normalized / np.max(y_filtered_normalized)) * 255

    # Defining the final matrix
    if (axis == 'x'):
        final_matrix = x_filtered_normalized
    elif (axis == 'y'):
        final_matrix = y_filtered_normalized

    # Returning the final matriz
    return final_matrix.astype(np.uint8)

# Magnitude gradient
@runs_rgb
def magnitude_gradient(img_matrix: np.ndarray):

    # Obtaining the x and y filtered image
    x_filtered = sobel(img_matrix, 'x').astype(np.float64)
    y_filtered = sobel(img_matrix, 'y').astype(np.float64)

    # Applying the soma described in book |G| = |gx| + |gy|
    sum_matrix = np.abs(x_filtered) + np.abs(y_filtered)

    # Applying thresholding
    sum_matrix = thresholding(sum_matrix, 128)

    # Returning the result
    return sum_matrix.astype(np.uint8)