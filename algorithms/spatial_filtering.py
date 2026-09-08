# Spatial filtering functions

# Importing the necessary libraries
import numpy as np

# Convolution
def convolution(img_matrix: np.ndarray, filter: np.ndarray) -> np.ndarray:

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
    final_matrix = np.clip(final_matrix, 0, 255)
    return final_matrix.astype(np.uint8)

# Mean filter
def mean_filter(img_matrix: np.ndarray, dimension: int):

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
def gaussian_smoothing(img_matrix: np.ndarray, dimension: int, standard_deviation: float):

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

            # Applying the operation
            filtered_values = operation_matrix * gauss_filter
            result = np.sum(filtered_values)
            final_matrix[i][j] = result

    # Returning the final matrix
    final_matrix = np.clip(final_matrix, 0, 255)
    return final_matrix.astype(np.uint8)
