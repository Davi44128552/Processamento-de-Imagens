# Importing the necessary libraries
import numpy as np
from .aux_functions import next_power_of_two, runs_rgb

# Discrete Fourier Transform
def discrete_fourier_transform(img_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    # Checking the dimensions of the image
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

    # Creating the rows matrix
    n = np.arange(N)
    k = n.reshape((N, 1))
    weight_rows = np.exp((-2j * np.pi * k * n) / N)

    # Creating the columns matrix
    n = np.arange(M)
    k = n.reshape((M, 1))
    weight_columns = np.exp((-2j * np.pi * n * k) / M)

    # Calculating discrete fourier transform using the formula
    result_matrices = weight_rows @ input_matrix @ weight_columns

    # Taking the result matrices
    real_matrix = result_matrices.real
    imaginary_matrix = result_matrices.imag

    # Returning the final matrices
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

    if (len(complex_matrix.shape) == 3):
        shifted_complex_matrix = np.fft.fftshift(complex_matrix, axes = (0, 1))
    else:
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

# Cooley-Tukey algorithm for 1D matrices
def cooley_tukey(matrix: np.ndarray) -> np.ndarray:

    # Array size
    array_size = matrix.shape[-1]

    # Cooley-Tukey is a divide and conquer algorithm
    # Base case
    if (array_size <= 1):
        return matrix

    # Dividing the matrix into even and odd indices
    even_matrix = matrix[..., 0::2]
    odd_matrix = matrix[..., 1::2]

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
    final_matrix = np.concatenate([first_half, second_half], axis = -1)

    # Returning the result
    return final_matrix

# Function to invert fourier transform
@runs_rgb
def inverse_fft(shifted_complex_matrix: np.ndarray) -> np.ndarray:

    # Undo the shift
    complex_matrix = np.fft.ifftshift(shifted_complex_matrix)

    # Taking initial values
    N = complex_matrix.shape[0]
    M = complex_matrix.shape[1]
    
    conjugate_input = complex_matrix.conj()

    # Applying the cooley_tukey algorithm
    rows_output = cooley_tukey(conjugate_input)
    columns_output = cooley_tukey(rows_output.T)
    columns_output =columns_output.T

    # Calculating the final matrix
    final_matrix = columns_output.conj() / (N * M)
    final_matrix = final_matrix.real
    final_matrix = np.clip(final_matrix, 0, 255)

    # Returning the result matrix
    return final_matrix.astype(np.uint8)