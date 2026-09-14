# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

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