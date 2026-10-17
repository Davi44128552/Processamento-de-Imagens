# Importing the necessary libraries
import numpy as np
from .aux_functions import next_power_of_two

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

# Functions for the fast Fourier transform
# Cooley-Tukey algorithm for 1D matrices
def cooley_tukey(matrix: np.ndarray) -> np.ndarray:

    # Array size
    array_size = matrix.shape[0]

    # Cooley-Tukey is a divide and conquer algorithm
    # Base case
    if (array_size <= 1):
        return matrix

    # Dividing the matrix into even and odd indices
    even_matrix = matrix[0::2]
    odd_matrix = matrix[1::2]

    # Applying the Cooley-Tukey test recursively to the new matrices
    even_output = cooley_tukey(even_matrix)
    odd_output = cooley_tukey(odd_matrix)

    # Conquer: Calculating the Twiddle factors
    # Defined by e^((-2jpik) / N)
    factor = np.exp(-2j * np.pi * np.arange(array_size // 2) / array_size)

    # Combining the results
    first_half = even_output + factor * odd_output
    second_half = even_output - factor * odd_output

    # Concatenating the results
    final_matrix = np.concatenate([first_half, second_half])

    # Returning the result
    return final_matrix

# FFT Function
def fast_fourier_transform(img_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    # Converting the matrix
    input_matrix = img_matrix.astype(np.float64)

    # Taking the image dimensions
    N = img_matrix.shape[0]
    M = img_matrix.shape[1]  

    # Defining the new dimensions
    new_N = next_power_of_two(N)
    new_M = next_power_of_two(M)

    # Creating the matrix
    padded_image = np.zeros((new_N, new_M)).astype(np.float64)
    padded_image[:N, :M] = input_matrix

    # Applying the cooley tukey in each row
    rows_fft = np.zeros((new_N, new_M), dtype = np.complex128)
    for i in range(0, new_N):
        rows_fft[i, :] = cooley_tukey(padded_image[i, :])

    # Applying the cooley tukey in each column
    columns_fft = np.zeros((new_N, new_M), dtype = np.complex128)
    for j in range(0, new_M):
        columns_fft[:, j] = cooley_tukey(rows_fft[:, j])

    # Results
    columns_fft_real = columns_fft.real
    columns_fft_imaginary = columns_fft.imag

    # Returning the results
    return columns_fft_real, columns_fft_imaginary

# Function to get the result image of fft
def get_result_image(real_matrix: np.ndarray, imaginary_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    # Reconstructing the complex_matrix
    complex_matrix = real_matrix + 1j * imaginary_matrix
    shifted_complex_matrix = np.fft.fftshift(complex_matrix)

    # Calculating the result

    shifted_real_matrix = shifted_complex_matrix.real
    shifted_imaginary_matrix = shifted_complex_matrix.imag

    matrix_magnitude = np.sqrt(shifted_real_matrix ** 2 + shifted_imaginary_matrix ** 2)
    final_matrix = np.log(1 + matrix_magnitude)

    # Normalizing the matrix
    final_matrix = (final_matrix - np.min(final_matrix)) / (np.max(final_matrix) - np.min(final_matrix))
    final_matrix = final_matrix * 255

    # Returning the final matrix
    return final_matrix.astype(np.uint8), shifted_complex_matrix

# Function to invert fourier transform
def inverse_fft(shifted_complex_matrix: np.ndarray) -> np.ndarray:

    # Undo the shift
    complex_matrix = np.fft.ifftshift(shifted_complex_matrix)

    # Taking initial values
    N = complex_matrix.shape[0]
    M = complex_matrix.shape[1]
    
    conjugate_input = complex_matrix.conj()

    # Applying the cooley_tukey algorithm
    rows_output = np.zeros((N, M), dtype = np.complex128)
    for i in range(0, N):
        rows_output[i, :] = cooley_tukey(conjugate_input[i, :])

    columns_output = np.zeros((N, M), dtype = np.complex128)
    for j in range(0, M):
        columns_output[:, j] = cooley_tukey(rows_output[:, j])

    # Calculating the final matrix
    final_matrix = columns_output.conj() / (N * M)
    final_matrix = final_matrix.real
    final_matrix = np.clip(final_matrix, 0, 255)

    # Returning the result matrix
    return final_matrix.astype(np.uint8)