# Importing the necessary modules
import numpy as np

# Scaling function
def scaling(img_matrix: np.ndarray, sx: float, sy: float, alg_type: str) -> np.ndarray:

    # Creating the result matrix
    n_rows_matrix = int(np.round(img_matrix.shape[0] * sy))
    n_columns_matrix = int(np.round(img_matrix.shape[1] * sx))
    result_matrix = np.zeros((n_rows_matrix, n_columns_matrix))

    # Scaling the matrix
    for r in range(0, n_rows_matrix):
        for c in range(0, n_columns_matrix):

            # Applying the mapping formula

            if (alg_type == 'nearest'):
                x = c / sx
                y = r / sy

                # 1st method
                # Rounding the result values
                x = int(np.round(x))
                y = int(np.round(y))

                # Applying to the image
                x = max(0, min(x, img_matrix.shape[1] - 1))
                y = max(0, min(y, img_matrix.shape[0] - 1))
                result_matrix[r][c] = img_matrix[y][x]

    # Returning the final matrix
    return result_matrix.astype(np.uint8)