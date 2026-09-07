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