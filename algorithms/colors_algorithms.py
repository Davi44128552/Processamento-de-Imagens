# Importing the necessary libraries
import numpy as np
from .aux_functions import resize_image

# Function to convert RGB -> HSI
def convert_rgb_to_hsi(img_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

    # Initial parameters
    input_matrix = img_matrix.astype(np.float64) / 255.0
    R = input_matrix[:, :, 0]
    G = input_matrix[:, :, 1]
    B = input_matrix[:, :, 2]

    # H = HUE / S = SATURATION / I = INTENSITY

    # Calculating Intensity
    # Defined by formula (R + G + B) / 3
    I = (R + G + B) / 3

    # Calculating Saturation
    # Defined by formula 1 - ((3 / (R + G + B)) * min(R, G, B))
    S = 1 - (((3) / (R + G + B + 1e-8)) * np.min(input_matrix, axis = 2))

    # Calculating Hue
    x1 = 0.5 * ((R - G) + (R - B))
    x2 = np.sqrt(np.power((R - G), 2) + 
    (R - B) * (G - B))
    theta = np.clip(x1 / (x2 + 1e-8), -1.0, 1.0)
    theta = np.arccos(theta)
    theta = np.degrees(theta)

    # Defining hue values
    condition = B <= G
    H = np.where(condition, theta, 360.0 - theta)
    return H, S, I

# Function to convert HSI -> RGB
def convert_hsi_to_rgb(H: np.ndarray, S: np.ndarray, I: np.ndarray) -> np.ndarray:

    # Creating the R, G and B matrices
    R = np.zeros((H.shape[0], H.shape[1]))
    R = R.astype(np.float64)

    G = np.zeros((H.shape[0], H.shape[1]))
    G = G.astype(np.float64)

    B = np.zeros((H.shape[0], H.shape[1]))
    B = B.astype(np.float64)
    
    # When converting from HSI to RGB, we must divide the calculation into 3 sectors, based on the value of the H angle.

    # 1: RG (0 <= H < 120)
    # R = I * [1 + (S*cos(H) / (cos(60 - H)))]
    # G = 3I - (R + B)
    # B = I(1 - S)

    condition1 = (H >= 0) & (H < 120)
    B[condition1] = I[condition1] * (1 - S[condition1])
    R[condition1] = I[condition1] * (1 + ((S[condition1] * np.cos(np.radians(H[condition1]))) / (np.cos(np.radians(60 - H[condition1])))))
    G[condition1] = 3 * I[condition1] - (R[condition1] + B[condition1])

    # 2: GB (120 <= H < 240)
    # G = I * [1 + (S*cos(H) / (cos(60 - H)))]
    # B = 3I - (R + G)
    # R = I(1 - S)

    condition2 = (H >= 120) & (H < 240)
    R[condition2] = I[condition2] * (1 - S[condition2])
    G[condition2] = I[condition2] * (1 + ((S[condition2] * np.cos(np.radians(H[condition2] - 120))) / (np.cos(np.radians(180 - H[condition2])))))
    B[condition2] = 3 * I[condition2] - (R[condition2] + G[condition2])

    # 3: RB (240 <= H <= 360)
    # B = I * [1 + (S*cos(H) / (cos(60 - H)))]
    # R = 3I - (G + B)
    # G = I(1 - S)

    condition3 = (H >= 240) & (H <= 360)
    G[condition3] = I[condition3] * (1 - S[condition3])
    B[condition3] = I[condition3] * (1 + ((S[condition3] * np.cos(np.radians(H[condition3] - 240))) / (np.cos(np.radians(300 - H[condition3])))))
    R[condition3] = 3 * I[condition3] - (G[condition3] + B[condition3])

    # Merging the matrices
    rgb_matrix = np.dstack((R, G, B))
    final_matrix = np.clip(rgb_matrix, 0.0, 1.0)
    final_matrix = final_matrix * 255

    # Returning the result
    return final_matrix.astype(np.uint8)

# Grayscale algorithms
    # Simple arithmetic mean
def gray_scale_mean(img_matrix: np.ndarray) -> np.ndarray:

    # Initial parameters
    input_matrix = img_matrix.astype(np.float64)
    R = input_matrix[:, :, 0]
    G = input_matrix[:, :, 1]
    B = input_matrix[:, :, 2]

    # The mean is defined by (R + G + B) / 3
    mean_matrix = (R + G + B) / 3.0

    # Merging the matrices
    final_matrix = np.dstack((mean_matrix, mean_matrix, mean_matrix))

    # Returning the result
    return final_matrix.astype(np.uint8)

    # Weighted arithmetic mean
def gray_scale_weigthted_arithmetic_mean(img_matrix: np.ndarray, wred: float = 0.299, wgreen: float = 0.587, wblue: float = 0.114) -> np.ndarray:
    # The standardized coefficients of the NTSC / ITU-R BT.601 system are:
    # R = 0.299
    # G = 0.587
    # B = 0.114

    # Initial parameters
    input_matrix = img_matrix.astype(np.float64)
    R = input_matrix[:, :, 0]
    G = input_matrix[:, :, 1]
    B = input_matrix[:, :, 2]

    # The formula is a simple weighted arithmetic mean
    mean_matrix = ((R * wred) + (G * wgreen) + (B * wblue)) / (wred + wgreen + wblue)

    # Merging the matrices
    final_matrix = np.dstack((mean_matrix, mean_matrix, mean_matrix))

    # Returning the result
    return final_matrix.astype(np.uint8)

# Chroma-Key function
def chroma_key(img_matrix: np.ndarray, background_img_matrix: np.ndarray, color_vector: list, tol: float) -> np.ndarray:
    
    # Resizing background matrix
    resized_background_img = resize_image(img_matrix, background_img_matrix)
    
    # Converting some input values to float
    img_matrix_float = img_matrix.astype(np.float64)
    color_vector_float = np.array(color_vector, dtype = np.float64)

    # Defining R, G, B in the image
    R = img_matrix_float[:, :, 0]
    G = img_matrix_float[:, :, 1]
    B = img_matrix_float[:, :, 2]

    # Calculating the Euclidean distance
    R_euc = (R - color_vector_float[0]) ** 2
    G_euc = (G - color_vector_float[1]) ** 2
    B_euc = (B - color_vector_float[2]) ** 2
    D = np.sqrt(R_euc + G_euc + B_euc)

    # Creating a matrix to check which values in tol is greater than D[x, y]
    Bool_matrix = D < tol

    # Applying the mask in the input image
    final_matrix = img_matrix.copy()
    final_matrix[Bool_matrix] = resized_background_img[Bool_matrix]

    # Returning the result image
    return final_matrix.astype(np.uint8)

# Function to adjust HSI channels
def adjust_hsi_channels(img_matrix: np.ndarray, shift_h: float = 0.0, scale_s: float = 1.0, scale_i: float = 1.0) -> np.ndarray:

    # Taking HSI values
    H, S, I = convert_rgb_to_hsi(img_matrix)

    # Defining the new values
    H_output = (H + shift_h) % 360.0

    S_output = S * scale_s
    S_output = np.clip(S_output, 0.0, 1.0)

    I_output = I * scale_i
    I_output = np.clip(I_output, 0.0, 1.0)

    # Converting the output values into rgb
    final_matrix = convert_hsi_to_rgb(H_output, S_output, I_output)

    # Returning the final matrix
    return final_matrix.astype(np.uint8)

# Function to adjust HSI channels
def adjust_hsi_channels_2(H: np.ndarray, S: np.ndarray, I: np.ndarray, shift_h: float = 0.0, scale_s: float = 1.0, scale_i: float = 1.0) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

    # Defining the new values
    H_output = (H + shift_h) % 360.0

    S_output = S * scale_s
    S_output = np.clip(S_output, 0.0, 1.0)

    I_output = I * scale_i
    I_output = np.clip(I_output, 0.0, 1.0)

    # Returning the final matrix
    return H_output, S_output, I_output

# Function to adjust color balance
def adjust_color_balance(img_matrix: np.ndarray, shift_cr: float = 0.0, shift_mg: float = 0.0, shift_yb: float = 0.0) -> np.ndarray:

    # Initial parameters
    input_matrix = img_matrix.astype(np.float64)
    R = input_matrix[:, :, 0]
    G = input_matrix[:, :, 1]
    B = input_matrix[:, :, 2]

    # Applying the shifts
    R_output = R + shift_cr
    G_output = G + shift_mg
    B_output = B + shift_yb

    # Merging the channels
    final_matrix = np.dstack((R_output, G_output, B_output))
    final_matrix = np.clip(final_matrix, 0, 255)

    # Returning the final matrix
    return final_matrix.astype(np.uint8)

# Functions to use sepia filter
# There are three methods we can apply sepia

# RGB transformation (Industry standard)
def sepia_rgb(img_matrix: np.ndarray, filter_matrix: np.ndarray = None) -> np.ndarray:

    # Initial parameters
    input_matrix = img_matrix.astype(np.float64)
    R = input_matrix[:, :, 0]
    G = input_matrix[:, :, 1]
    B = input_matrix[:, :, 2]

    # if the user has not specified a filtering matrix, we will use the industry standard
    if (filter_matrix is None):
        filter_matrix = np.array([[0.393, 0.769, 0.189],
                                    [0.349, 0.686, 0.168],
                                    [0.272, 0.534, 0.131]])

    # Checking if the input matrix is 3x3
    elif (filter_matrix.shape[0] != 3 or filter_matrix.shape[1] != 3):
        print("A matriz de entrada deve ser 3x3!")
        return

    # Applying the matrix into the image channels
    R_output = filter_matrix[0, 0] * R + filter_matrix[0, 1] * G + filter_matrix[0, 2] * B
    G_output = filter_matrix[1, 0] * R + filter_matrix[1, 1] * G + filter_matrix[1, 2] * B
    B_output = filter_matrix[2, 0] * R + filter_matrix[2, 1] * G + filter_matrix[2, 2] * B

    # Merging the matrices
    final_matrix = np.dstack((R_output, G_output, B_output))
    final_matrix = np.clip(final_matrix, 0, 255)

    # Returning the final matrix
    return final_matrix.astype(np.uint8)
