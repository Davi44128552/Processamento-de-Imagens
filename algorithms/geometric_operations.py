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

# Rotation function
@runs_rgb
def rotation(img_matrix: np.ndarray, angle: float, pivot_x: int, pivot_y: int) -> np.ndarray:

    # Taking the image dimensions
    original_image_height = img_matrix.shape[0]
    original_image_width = img_matrix.shape[1]
    
    # Converting the angle to radius
    rad = angle * (np.pi / 180)

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

    for r in range(0, dimension[0]):
        for c in range(0, dimension[1]):

            # Taking the pixels values
            x_pixel = c + X_min
            y_pixel = r + Y_min

            # Calculating the distance between the pixel and the pivot
            dx = x_pixel - pivot_x
            dy = y_pixel - pivot_y

            # Rotating the pixel
            x = dx * np.cos(-rad) - dy * np.sin(-rad)
            y = dx * np.sin(-rad) + dy * np.cos(-rad)

            # Adding the pivot to the result
            x = int(round(x + pivot_x))
            y = int(round(y + pivot_y))

            # Adding the result to the result matrix
            # Checking if the pixel position is within the limit
            condition1 = 0 <= x < original_image_width
            condition2 = 0 <= y < original_image_height

            if (condition1 and condition2):
                result_matrix[r][c] = img_matrix[y][x]

    # Returning the result
    return result_matrix.astype(np.uint8)
