# Importing the necessary modules
import numpy as np

# Scaling function
def scaling(img_matrix: np.ndarray, sx: float, sy: float, alg_type: str) -> np.ndarray:

    # Taking the original matrix info
    original_matrix_height = img_matrix.shape[0]
    original_matrix_width = img_matrix.shape[1]

    # Creating the result matrix
    n_rows_matrix = int(np.round(img_matrix.shape[0] * sy))
    n_columns_matrix = int(np.round(img_matrix.shape[1] * sx))
    result_matrix = np.zeros((n_rows_matrix, n_columns_matrix))

    # Scaling the matrix
    for r in range(0, n_rows_matrix):
        for c in range(0, n_columns_matrix):

            # Applying the mapping formula
            
            x = c / sx
            y = r / sy

            if (alg_type == 'nearest'):

                # 1st method

                # Rounding the result values
                x = int(np.round(x))
                y = int(np.round(y))

                # Applying to the image
                x = max(0, min(x, img_matrix.shape[1] - 1))
                y = max(0, min(y, img_matrix.shape[0] - 1))
                result_matrix[r][c] = img_matrix[y][x]

            elif (alg_type == 'bilinear'):

                # 2nd method

                # Taking the neighboors coordinates
                xul = max(0, min(int(x), original_matrix_width - 1))
                yul = max(0, min(int(y), original_matrix_height - 1))
                xbr = min(int(x) + 1, original_matrix_width - 1)
                ybr = min(int(y) + 1, original_matrix_height - 1)

                # Getting the pixel neighborhood
                q11 = img_matrix[yul][xul]
                q12 = img_matrix[ybr][xul]
                q21 = img_matrix[yul][xbr]
                q22 = img_matrix[ybr][xbr]

                # Applying interpolation along the axes
                dx = x - int(x) 
                dy = y - int(y)

                    # X
                r1 = (1 - dx) * q11 + dx * q21
                r2 = (1 - dx) * q12 + dx * q22

                    # Y
                pixel_result_value = (1 - dy) * r1 + dy * r2
                result_matrix[r][c] = pixel_result_value

    # Returning the final matrix
    return result_matrix.astype(np.uint8)