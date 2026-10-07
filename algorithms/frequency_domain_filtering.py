# Importing the necessary libraries
import numpy as np

# Discrete Fourier Transform
def discrete_fourier_transform(img_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    # Converting the matrix
    input_matrix = img_matrix.astype(np.float64)

    # Taking the image dimensions
    N = img_matrix.shape[0]
    M = img_matrix.shape[1]

    # Creating the matrices
    real_matrix = np.zeros((N, M)).astype(np.float64)
    imaginary_matrix = np.zeros((N, M)).astype(np.float64)

    for i in range(0, N):
        for j in range(0, M):
            sum_r = 0
            sum_i = 0

            for r in range(0, N):
                for c in range(0, M):
                    sum_r += input_matrix[r][c] * np.cos(2 * np.pi * (((i * r) / N) + ((j * c) / M)))
                    sum_i -= input_matrix[r][c] * np.sin(2 * np.pi * (((i * r) / N) + ((j * c) / M)))

            # Saving the result in (i,j)
            real_matrix[i][j] = sum_r
            imaginary_matrix[i][j] = sum_i

    # Returning the matrices
    return real_matrix, imaginary_matrix

    