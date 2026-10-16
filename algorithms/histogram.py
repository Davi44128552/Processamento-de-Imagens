# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import mplcursors
from .colors_algorithms import convert_rgb_to_hsi, convert_hsi_to_rgb

# Function to show the histogram
def calculate_histogram(img_matrix: np.ndarray, title: str = None, norm: bool = False, generate_graph: bool = False) -> list:

    img_size = 2 ** (img_matrix.itemsize * 8)

    # Creating the intensity frequency vector
    intensity_frequency = list()
    for i in range(0, img_size):
        intensity_frequency.append(0)
    # Converting the matrix into a vector
    img_matrix_1d = img_matrix.flatten()

    # iterating through the vector and adding the values ​​to the list
    for pixel in img_matrix_1d:
        intensity_frequency[pixel] += 1

    # Normalizing if true
    if (norm):
        for i in range(0, img_size):
            intensity_frequency[i] = intensity_frequency[i] / (img_matrix_1d.size)

    x_axis = range(0, 256)

    if (generate_graph):
        # Generating the graph if necessary
        fig_config, _ = plt.subplots(figsize = (10, 8))
        fig_config.canvas.manager.set_window_title(title)
        graph = plt.bar(x_axis, intensity_frequency, color="lightgray", width=1.0, edgecolor = "black")
        plt.title(title)
        plt.ylabel("Frequência")
        plt.xlabel("Intensidade do Pixel")
        plt.xlim([0, 255])

        # Configing the cursor to show the data
        cursor = mplcursors.cursor(graph, hover = False)

        @cursor.connect("add")
        def int_data(data):
            x_val = int(round(data.target[0]))
            y_val = data.target[1]
            data.annotation.set_text(f"Intensidade: {x_val} \nFrequência: {y_val}")

        plt.show(block = False)

    # Returning the result
    return intensity_frequency

# Histogram equalization function
def histogram_equalization(img_matrix: np.ndarray) -> np.ndarray:

    img_size = 2 ** (img_matrix.itemsize * 8)

    # Calculating the histogram
    img_histogram = calculate_histogram(img_matrix, norm = True, generate_graph = False)

    # applying the formula 3.3-4 from image processing book
    # We can use sum instead of integration
    sumk = 0
    cdf_list = list()
    for i in range(0, img_size):
        sumk += img_histogram[i]
        cdf_list.append(np.round((img_size - 1) * sumk))

    # Taking the result and applying in the matrix
    img_matrix_1d = img_matrix.flatten()
    for i in range(0, img_matrix_1d.size):
        img_matrix_1d[i] = cdf_list[img_matrix_1d[i]]

    # Converting the vector into a matrix
    final_matrix = img_matrix_1d.reshape(img_matrix.shape)

    # Returning the final result
    return final_matrix.astype(np.uint8)

# Histogram function to RGBI
def rgb_histogram(img_matrix: np.ndarray, title: str = None, norm: bool = False, generate_graph: bool = False) -> list:

    R = img_matrix[:, :, 0]
    G = img_matrix[:, :, 1]
    B = img_matrix[:, :, 2]
    _, _, I = convert_rgb_to_hsi(img_matrix)
    I = (255 * I).astype(np.uint8)

    R_result = calculate_histogram(R, title, norm, False)
    G_result = calculate_histogram(G, title, norm, False)
    B_result = calculate_histogram(B, title, norm, False)
    I_result = calculate_histogram(I, title, norm, False)

    # Creating the graph, if necessary
    if (generate_graph):
        fig, axs = plt.subplots(2, 2, figsize = (12, 8))
        x_axis = range(0, 256)
        fig.suptitle(title)

        # Red
        axs[0, 0].bar(x_axis, R_result, color = 'red', width = 1.0, edgecolor = "black")
        axs[0, 0].set_title('RED')
        axs[0, 0].set_xlim([0, 256])

        # Green
        axs[0, 1].bar(x_axis, G_result, color = 'green', width = 1.0, edgecolor = "black")
        axs[0, 1].set_title('GREEN')
        axs[0, 1].set_xlim([0, 256])

        # Blue
        axs[1, 0].bar(x_axis, B_result, color = 'blue', width = 1.0, edgecolor = "black")
        axs[1, 0].set_title('BLUE')
        axs[1, 0].set_xlim([0, 256])

        # Intensity
        axs[1, 1].bar(x_axis, I_result, color = 'gray', width = 1.0, edgecolor = "black")
        axs[1, 1].set_title('INTENSITY')
        axs[1, 1].set_xlim([0, 256])

        plt.tight_layout()
        plt.show(block = True)

    # Returning the results
    return R_result, G_result, B_result, I_result

# RGB Histogram equalization function
def rgb_histogram_equalization(img_matrix: np.ndarray) -> np.ndarray:

    # Converting RGB to HSI
    H, S, I = convert_rgb_to_hsi(img_matrix)

    # Converting I to uint8
    I_input = I * 255.0
    I_input = I_input.astype(np.uint8)

    # Applying histogram equalization
    I_output = histogram_equalization(I_input)

    # Converting I output to [0.0, 1.0] range
    I_output = I_output.astype(np.float64)
    I_output = I_output / 255.0

    # Converting HSI to RGB
    final_matrix = convert_hsi_to_rgb(H, S, I_output)

    # Returning the final matrix
    return final_matrix.astype(np.uint8)