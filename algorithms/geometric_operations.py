# Importing the necessary modules
import numpy as np
from .aux_functions import runs_rgb

# Scaling function
@runs_rgb
def scaling(img_matrix: np.ndarray, sx: float, sy: float, alg_type: str) -> np.ndarray:

    # Taking the original matrix info
    original_matrix_height = img_matrix.shape[0]
    original_matrix_width = img_matrix.shape[1]

    # Creating the result matrix
    n_rows_matrix = int(np.round(img_matrix.shape[0] * sy))
    n_columns_matrix = int(np.round(img_matrix.shape[1] * sx))
    result_matrix = np.zeros((n_rows_matrix, n_columns_matrix))

    c, r = np.meshgrid(np.arange(n_columns_matrix), np.arange(n_rows_matrix))
    
    # Scaling the matrix

    # Applying the mapping formula
    
    x = c / sx
    y = r / sy

    if (alg_type == 'nearest'):

        # 1st method

        # Rounding the result values
        x = np.round(x).astype(int)
        y = np.round(y).astype(int)

        # Applying to the image
        x = np.clip(x, 0, original_matrix_width - 1)
        y = np.clip(y, 0, original_matrix_height - 1)
        result_matrix = img_matrix[y, x]

    elif (alg_type == 'bilinear'):

        # 2nd method
        x_int = np.floor(x).astype(int)
        y_int = np.floor(y).astype(int)

        # Taking the neighboors coordinates
        xul = np.clip(x_int, 0, original_matrix_width - 1)
        yul = np.clip(y_int, 0, original_matrix_height - 1)
        xbr = np.clip(x_int + 1, 0, original_matrix_width - 1)
        ybr = np.clip(y_int + 1, 0, original_matrix_height - 1)

        # Getting the pixel neighborhood
        q11 = img_matrix[yul, xul]
        q12 = img_matrix[ybr, xul]
        q21 = img_matrix[yul, xbr]
        q22 = img_matrix[ybr, xbr]

        # Applying interpolation along the axes
        dx = x - x_int
        dy = y - y_int

            # X
        r1 = (1 - dx) * q11 + dx * q21
        r2 = (1 - dx) * q12 + dx * q22

            # Y
        pixel_result_value = (1 - dy) * r1 + dy * r2
        result_matrix = pixel_result_value

    # Returning the final matrix
    return result_matrix.astype(np.uint8)

# Rotation function
@runs_rgb
def rotation(img_matrix: np.ndarray, angle: float, pivot_x: int, pivot_y: int, alg_type: str) -> np.ndarray:

    # Taking the image dimensions
    original_image_height = img_matrix.shape[0]
    original_image_width = img_matrix.shape[1]
    
    # Converting the angle to radius
    rad = angle * (np.pi / 180)

    result_matrix = np.zeros((original_image_height, original_image_width))

    c, r = np.meshgrid(np.arange(original_image_width), np.arange(original_image_height))

    # Taking the pixels values
    x_pixel = c
    y_pixel = r

    # Calculating the distance between the pixel and the pivot
    dx = x_pixel - pivot_x
    dy = y_pixel - pivot_y

    # Rotating the pixel
    x_exact = dx * np.cos(-rad) - dy * np.sin(-rad) + pivot_x
    y_exact = dx * np.sin(-rad) + dy * np.cos(-rad) + pivot_y

    # Calculating the values acccording to the algorithm type
    if (alg_type == 'nearest'):

        x = np.round(x_exact).astype(int)
        y = np.round(y_exact).astype(int)

        # Adding the result to the result matrix
        # Checking if the pixel position is within the limit
        condition1 = (x >= 0) & (x < original_image_width) 
        condition2 = (y >= 0) & (y < original_image_height)

        result_matrix[(condition1 & condition2)] = img_matrix[y[(condition1 & condition2)], x[(condition1 & condition2)]]

    elif (alg_type == 'bilinear'):

        x = np.floor(x_exact).astype(int)
        y = np.floor(y_exact).astype(int)
        x2 = x + 1
        y2 = y + 1
        x3 = np.round(x_exact).astype(int)
        y3 = np.round(y_exact).astype(int)

        condition1 = (x >= 0) & (x2 < original_image_width)
        condition2 = (y >= 0) & (y2 < original_image_height)

        weigth_x = x_exact[(condition1 & condition2)] - x[(condition1 & condition2)]
        weigth_y = y_exact[(condition1 & condition2)] - y[(condition1 & condition2)]

        # Calculating the pixels
        pixel11 = img_matrix[y[(condition1 & condition2)], x[(condition1 & condition2)]]
        pixel12 = img_matrix[y[(condition1 & condition2)], x2[(condition1 & condition2)]]
        pixel21 = img_matrix[y2[(condition1 & condition2)], x[(condition1 & condition2)]]
        pixel22 = img_matrix[y2[(condition1 & condition2)], x2[(condition1 & condition2)]]

        # Calculating the pixel value
        pixel = pixel11 * (1 - weigth_x) * (1 - weigth_y) + pixel12 * weigth_x * (1 - weigth_y) + pixel21 * (1 - weigth_x) * weigth_y + pixel22 * weigth_x * weigth_y
        result_matrix[(condition1 & condition2)] = pixel

        # Applying nearest in the edges
        condition3 = (x3 >= 0) & (x3 < original_image_width)
        condition4 = (y3 >= 0) & (y3 < original_image_height)
        condition5 = ~(condition1 & condition2)

        result_matrix[(condition5 & condition4 & condition3)] = img_matrix[y3[(condition5 & condition4 & condition3)], x3[(condition5 & condition4 & condition3)]]

    # Returning the result
    return result_matrix.astype(np.uint8)

# Rotation without pivot function
@runs_rgb
def rotation_without_pivot(img_matrix: np.ndarray, angle: float, alg_type: str) -> np.ndarray:

    # Taking the image dimensions
    original_image_height = img_matrix.shape[0]
    original_image_width = img_matrix.shape[1]
    
    # Converting the angle to radius
    rad = angle * (np.pi / 180)

    # Defining the pivots in the center of the image
    pivot_x = original_image_width / 2
    pivot_y = original_image_height / 2

    # Defining the result image dimension
    q1 = [0, 0]
    q2 = [original_image_width - 1, 0]
    q3 = [0, original_image_height - 1]
    q4 = [original_image_width - 1, original_image_height - 1]
    q_list = [q1, q2, q3, q4]

        # Calculating the distance between the qs and pivots
    for q in q_list:
        dx = q[0] - pivot_x
        dy = q[1] - pivot_y
        x_temp = dx * np.cos(rad) - dy * np.sin(rad)
        y_temp = dx * np.sin(rad) + dy * np.cos(rad)
        q[0] = x_temp + pivot_x
        q[1] = y_temp + pivot_y

    # Determining the Xmin and Xmax
    X_min = min([q1[0], q2[0], q3[0], q4[0]])
    X_max = max([q1[0], q2[0], q3[0], q4[0]])

    # Determining the Ymin and Ymax
    Y_min = min([q1[1], q2[1], q3[1], q4[1]])
    Y_max = max([q1[1], q2[1], q3[1], q4[1]])

    # Creating the new matrix
    dimension = [int(round(Y_max - Y_min)), int(round(X_max - X_min))]
    result_matrix = np.zeros((dimension[0], dimension[1]))

    c, r = np.meshgrid(np.arange(dimension[1]), np.arange(dimension[0]))

    # Taking the pixels values
    x_pixel = c + X_min
    y_pixel = r + Y_min

    # Calculating the distance between the pixel and the pivot
    dx = x_pixel - pivot_x
    dy = y_pixel - pivot_y

    # Rotating the pixel
    x_exact = dx * np.cos(-rad) - dy * np.sin(-rad) + pivot_x
    y_exact = dx * np.sin(-rad) + dy * np.cos(-rad) + pivot_y

    # Calculating the values acccording to the algorithm type
    if (alg_type == 'nearest'):

        x = np.round(x_exact).astype(int)
        y = np.round(y_exact).astype(int)

        # Adding the result to the result matrix
        # Checking if the pixel position is within the limit
        condition1 = (x >= 0) & (x < original_image_width) 
        condition2 = (y >= 0) & (y < original_image_height)

        result_matrix[(condition1 & condition2)] = img_matrix[y[(condition1 & condition2)], x[(condition1 & condition2)]]

    elif (alg_type == 'bilinear'):

        x = np.floor(x_exact).astype(int)
        y = np.floor(y_exact).astype(int)
        x2 = x + 1
        y2 = y + 1
        x3 = np.round(x_exact).astype(int)
        y3 = np.round(y_exact).astype(int)

        condition1 = (x >= 0) & (x2 < original_image_width)
        condition2 = (y >= 0) & (y2 < original_image_height)

        weigth_x = x_exact[(condition1 & condition2)] - x[(condition1 & condition2)]
        weigth_y = y_exact[(condition1 & condition2)] - y[(condition1 & condition2)]

        # Calculating the pixels
        pixel11 = img_matrix[y[(condition1 & condition2)], x[(condition1 & condition2)]]
        pixel12 = img_matrix[y[(condition1 & condition2)], x2[(condition1 & condition2)]]
        pixel21 = img_matrix[y2[(condition1 & condition2)], x[(condition1 & condition2)]]
        pixel22 = img_matrix[y2[(condition1 & condition2)], x2[(condition1 & condition2)]]

        # Calculating the pixel value
        pixel = pixel11 * (1 - weigth_x) * (1 - weigth_y) + pixel12 * weigth_x * (1 - weigth_y) + pixel21 * (1 - weigth_x) * weigth_y + pixel22 * weigth_x * weigth_y
        result_matrix[(condition1 & condition2)] = pixel

        # Applying nearest in the edges
        condition3 = (x3 >= 0) & (x3 < original_image_width)
        condition4 = (y3 >= 0) & (y3 < original_image_height)
        condition5 = ~(condition1 & condition2)

        result_matrix[(condition5 & condition4 & condition3)] = img_matrix[y3[(condition5 & condition4 & condition3)], x3[(condition5 & condition4 & condition3)]]

    # Returning the result
    return result_matrix.astype(np.uint8)