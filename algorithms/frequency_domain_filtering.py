# Importing the necessary libraries
import numpy as np
from .aux_functions import next_power_of_two, runs_rgb

# Discrete Fourier Transform
@runs_rgb
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

# FFT Function
def fast_fourier_transform(img_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    # If matrix is 3D, then we calculate in each channel
    if (len(img_matrix.shape) == 3):

        real_channels = list()
        imaginary_channels = list()

        for i in range(0, 3):
            real, imag = fast_fourier_transform(img_matrix[:, :, i])
            real_channels.append(real)
            imaginary_channels.append(imag)
        return np.dstack(real_channels), np.dstack(imaginary_channels)

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

    # Applying numpy FFT2D 
    fft_result = np.fft.fft2(padded_image)

    # Talking the result matrices
    real_matrix = fft_result.real
    imaginary_matrix = fft_result.imag

    # Returning the results
    return real_matrix, imaginary_matrix

# Function to get the result image of fft
def get_result_image(real_matrix: np.ndarray, imaginary_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    # Reconstructing the complex_matrix
    complex_matrix = real_matrix + 1j * imaginary_matrix
    shifted_complex_matrix = np.fft.fftshift(complex_matrix)

    matrix_magnitude = np.abs(shifted_complex_matrix)
    final_matrix = np.log(1 + matrix_magnitude)

    # Normalizing the matrix
    min_value = np.min(final_matrix)
    max_value = np.max(final_matrix)

    if (max_value > min_value):
        final_matrix = (final_matrix - min_value) / (max_value - min_value) * 255.0 
    else:
        final_matrix = np.zeros_like(final_matrix)

    # Returning the final matrix
    return final_matrix.astype(np.uint8), shifted_complex_matrix

# Function to invert fourier transform
'''@runs_rgb
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
    return final_matrix.astype(np.uint8)'''