# Importing modules
import sys
import os
import ctypes
from qt_core import *
from gui.windows.main_win.ui_main_window import *
from PIL.ImageQt import ImageQt

# Import the algorithms files
directory = os.path.dirname(os.path.abspath(__file__))
directory = os.path.abspath(os.path.join(directory, ".."))
sys.path.append(directory)
from algorithms.intensity_transformations import *
from algorithms.aux_functions import *
from algorithms.histogram import *
from algorithms.spatial_filtering import *
from algorithms.geometric_operations import *
from algorithms.frequency_domain_filtering import *
from algorithms.colors_algorithms import *
from gui.dialogs.dialog_convolution_matrix import ConvolutionMatrixDialog
from gui.dialogs.dialog_hsi_result import HSIDialog
from gui.dialogs.dialog_canvas import DialogCanvas

# Main window class
class MainWindow(QMainWindow):
    def __init__(self):

        # Creating the class and showing de window
        super().__init__()

        # Adding a title to the application
        self.setWindowTitle("CalopImage")

        # Taking the icon and setting in the application
        directory = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(directory, "images", "calopsita_appimage.png")
        
        # Creating the application icon
        self.setWindowIcon(QIcon(icon_path))

        # Setting the main window
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button action
        self.ui.toggle_button.clicked.connect(lambda: self.toggle_button(self.ui.left_menu))

        # Calling the function to apply the transformation
        self.ui.toggle2_button.clicked.connect(lambda: self.toggle_button(self.ui.transformation_menu))
        self.ui.button_thresholding.clicked.connect(self.open_thresholding)
        self.ui.button_negative.clicked.connect(self.open_negative)
        self.ui.button_brightness.clicked.connect(self.open_brightness)
        self.ui.button_logarithm_transformation.clicked.connect(self.open_logarithm)
        self.ui.button_power_law.clicked.connect(self.open_power_law)
        self.ui.button_piecewise_linear.clicked.connect(self.opne_piecewise_linear)
        self.ui.button_contrast_stretching.clicked.connect(self.open_contrast_stretching)
        self.ui.button_intensity_level_slicing.clicked.connect(self.open_intensity_level_slicing)
        self.ui.button_bit_plane_slicing.clicked.connect(self.open_bit_plane_slicing)
        self.ui.button_steganography_apply.clicked.connect(self.open_steganography_apply)
        self.ui.button_steganography_undo.clicked.connect(self.open_steganography_decode)
        self.ui.transformation_download_button.clicked.connect(self.save_image)
        self.ui.button_transformation_go_back.clicked.connect(self.go_back)
        self.ui.toggle_histogram_button.clicked.connect(lambda: self.toggle_button(self.ui.equalization_hist_menu))
        self.ui.histogram_download_button.clicked.connect(self.save_image)
        self.ui.button_histogram_go_back.clicked.connect(self.go_back)

        # Spatial filtering buttons
        self.ui.button_convolution.clicked.connect(self.open_convolution_apply)
        self.ui.button_mean.clicked.connect(self.open_mean_filter_apply)
        self.ui.button_gaussian.clicked.connect(self.open_gaussian_smoothing_filter_apply)
        self.ui.button_median.clicked.connect(self.open_median_filter_apply)
        self.ui.button_laplacian.clicked.connect(self.open_laplacian_filter_apply)
        self.ui.button_highboost.clicked.connect(self.open_highboost_filter_apply)
        self.ui.button_sobel.clicked.connect(self.open_sobel_apply)
        self.ui.button_magnitude_gradient.clicked.connect(self.open_magnitude_gradient_apply)
        self.ui.toggle_spatial_button.clicked.connect(lambda: self.toggle_button(self.ui.spatial_filtering_menu))
        self.ui.button_spatial_go_back.clicked.connect(self.go_back)
        self.ui.spatial_download_button.clicked.connect(self.save_image)

        # Geometric operations buttons
        self.ui.toggle_geometric_button.clicked.connect(lambda: self.toggle_button(self.ui.geometric_operations_menu))
        self.ui.scaling_button.clicked.connect(self.open_scaling_apply)
        self.ui.geometric_download_button.clicked.connect(self.save_image)
        self.ui.button_geometric_go_back.clicked.connect(self.go_back)

        self.ui.rotating_button.clicked.connect(self.open_rotating_apply)
        
        # Frequency domain buttons
        self.ui.toggle_frequency_button.clicked.connect(lambda: self.toggle_button(self.ui.frequency_algorithms_menu))
        self.ui.button_dft.clicked.connect(self.open_dft_apply)
        self.ui.button_fft_apply.clicked.connect(self.open_fft_apply)
        self.ui.button_inverse_fourier.clicked.connect(self.open_ifft_apply)
        self.ui.frequency_download_button.clicked.connect(self.save_image)
        self.ui.button_frequency_go_back.clicked.connect(self.go_back)

        # Colors algorithms buttons
        self.ui.toggle_color_button.clicked.connect(lambda: self.toggle_button(self.ui.colors_algorithms_menu))
        self.ui.button_get_hsi.clicked.connect(self.open_rgb_hsi)
        self.ui.button_get_rgb.clicked.connect(self.open_hsi_rgb)
        self.ui.button_grayscale_mean.clicked.connect(self.open_grayscale_mean_color_apply)
        self.ui.button_grayscale_weighted_mean.clicked.connect(self.open_grayscale_weighted_apply)
        self.ui.button_rgb_negative.clicked.connect(self.open_negative_rgb)
        self.ui.button_chroma_key.clicked.connect(self.open_chroma_key)
        self.ui.button_adjust_hsi.clicked.connect(self.open_adjust_hsi_channels_apply)
        self.ui.button_adjust_color_balance.clicked.connect(self.open_adjust_color_balance_apply)
        self.ui.button_sepia_filter.clicked.connect(self.open_adjust_sepia_apply)
        self.ui.button_colors_go_back.clicked.connect(self.go_back)
        self.ui.button_colors_download_button.clicked.connect(self.save_image)  

        # Showing the GUI
        self.show()

        # Adding the behavior to the button
        self.ui.toggle_button2.clicked.connect(self.open_image)
        self.ui.toggle_button3.clicked.connect(self.random_image_select)
        self.ui.config_button.clicked.connect(self.help)
        self.ui.select_part_window_ui.pushButton.clicked.connect(self.ui.select_part_window.accept)
        self.ui.sobel_apply_window_ui.pushButton.clicked.connect(self.ui.sobel_apply_window.accept)
        self.ui.scaling_apply_window_ui.pushButton.clicked.connect(self.ui.scaling_apply_window.accept)
        self.ui.get_rgb_window_ui.buttonBox.clicked.connect(self.ui.get_rgb_window.accept)
        # self.ui.histogram_window_ui.pushButton.clicked.connect(self.ui.histogram_window.accept)
        
        self.is_drawning_mask = False
        self.drawning = False
        self.last_point = QPoint()
        self.brush_color = QColor(0, 0, 0)
        self.brush_size = 7
        self.mask_image = None
        self.mirror_brush = False

        self.ui.fft_paint_window_ui.buttonGroup.buttonClicked.connect(self.update_size)
        self.ui.fft_paint_window_ui.buttonGroup_2.buttonClicked.connect(self.update_color)
        self.ui.fft_paint_window_ui.checkBox.stateChanged.connect(self.update_mirror)
        self.ui.ui_pages.label_2.mousePressEvent = self.label_mouse_press
        self.ui.ui_pages.label_2.mouseMoveEvent = self.label_mouse_move
        self.ui.ui_pages.label_2.mouseReleaseEvent = self.label_mouse_release

        self.button_list = [self.ui.button_thresholding, self.ui.button_negative, self.ui.button_brightness, self.ui.button_logarithm_transformation, self.ui.button_power_law,
                                       self.ui.button_contrast_stretching, self.ui.button_intensity_level_slicing, self.ui.button_bit_plane_slicing,
                                       self.ui.button_steganography_apply, self.ui.button_steganography_undo, self.ui.config_button, self.ui.toggle_button, self.ui.toggle_button2, 
                                       self.ui.toggle_button3, self.ui.button_convolution, self.ui.button_mean, self.ui.button_gaussian, 
                                       self.ui.button_median, self.ui.button_laplacian, self.ui.button_highboost, self.ui.button_piecewise_linear,
                                       self.ui.button_sobel, self.ui.button_magnitude_gradient, self.ui.toggle_spatial_button]

        self.waiting_for_rotation_click = False
        self.rotation_angle = 0
        self.alg_type = 'bilinear'

        # Some config buttons behavior
    def help(self):
        self.ui.toggle_button2.set_active(False)
        self.ui.toggle_button3.set_active(False)
        self.ui.config_button.set_active(True)

    def go_back(self):
        # Removing the transformations menu
        self.ui.main_layout.removeWidget(self.ui.transformation_menu)
        self.ui.transformation_menu.hide()

        # Removing the histogram menu
        self.ui.main_layout.removeWidget(self.ui.equalization_hist_menu)
        self.ui.equalization_hist_menu.hide()

        # Removing the spatial filtering menu
        self.ui.main_layout.removeWidget(self.ui.spatial_filtering_menu)
        self.ui.spatial_filtering_menu.hide()

        # Removing the geometric operations menu
        self.ui.main_layout.removeWidget(self.ui.geometric_operations_menu)
        self.ui.geometric_operations_menu.hide()

        # Removing the frequency domain menu
        self.ui.main_layout.removeWidget(self.ui.frequency_algorithms_menu)
        self.ui.frequency_algorithms_menu.hide()

        # Removing the colors algorithms menu
        self.ui.main_layout.removeWidget(self.ui.colors_algorithms_menu)
        self.ui.colors_algorithms_menu.hide()

        # Adding the left menu layout
        self.ui.main_layout.insertWidget(0, self.ui.left_menu)
        self.ui.left_menu.show()

        # Returning to main window
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page1)

    # Adding a action to toggle button
    def toggle_button(self, menu):

        # Configing
        menu_width = menu.width()
        width = 50
        if (menu_width == 50):
            width = 300

        self.animation = QPropertyAnimation(menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    # Adding the button function to open a image
    def open_image(self):

        self.is_drawning_mask = False
        self.active_button(self.ui.toggle_button2)

        # Opening file selector
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione a imagem", "", "Imagens (*.png *.jpg *.jpeg *.bmp)")
        if (file_path):

            # Reading the image
            load_image = QImage(file_path)
            load_image = QPixmap.fromImage(load_image)

            # Applying scale
            load_image = self.resize_image_display(load_image)

            # Changing the label and showing the image to the user
            self.ui.ui_pages.label_2.setPixmap(load_image)
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.page2)

            self.select_algorithms(file_path)

    # Adding the button function to take a random image
    def random_image_select(self):

        self.active_button(self.ui.toggle_button3)
                
        # Opening file selector
        directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(directory, "..", "test_images", "calopsita.jpg")
        image_path = os.path.normpath(image_path)
        if (image_path):

            # Reading the image
            random_image = QPixmap(image_path)
            random_image = self.resize_image_display(random_image)

            # Changing the label and showing the image to the user
            self.ui.ui_pages.label.setPixmap(random_image)
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.page3)

            self.select_algorithms(image_path)

            # Going to transformation function
    # Function to save the images
    def save_image(self):

        # Defining the path
        file_path,_ = QFileDialog.getSaveFileName(self, "Salve a imagem", "", "Imagens (*.png *.bmp *.jpg *.jpeg)")

        # Verifying path
        if (file_path):
            self.final_image.save(file_path)

    # Function to apply the intensity_transformations
    def transformation(self, img_path):

        # Adding the transformations menu
        self.ui.main_layout.removeWidget(self.ui.left_menu)
        self.ui.left_menu.hide()
        self.ui.main_layout.insertWidget(0, self.ui.transformation_menu)
        self.ui.transformation_menu.show()

        # Reading the image
        self.matrix = conversion_to_matrix(img_path)
        self.final_image = conversion_to_image(self.matrix)

    # Function to apply the histogram
    def apply_histogram(self, img_path):

        # Adding the histogram menu
        self.ui.main_layout.removeWidget(self.ui.left_menu)
        self.ui.left_menu.hide()
        self.ui.main_layout.insertWidget(0, self.ui.equalization_hist_menu)
        self.ui.equalization_hist_menu.show()
        self.matrix = conversion_to_matrix(img_path)

        # Executing histogram window
        if (self.ui.histogram_window.exec()):

            if (self.ui.histogram_window_ui.radioButton.isChecked()):
                self.matrix = conversion_to_matrix(img_path, "L")
                converted_matrix = histogram_equalization(self.matrix)
                QTimer.singleShot(2000, lambda: calculate_histogram(self.matrix, title = "Histograma antes da equalização", generate_graph = True))
                QTimer.singleShot(2000, lambda: calculate_histogram(converted_matrix, title = "Histograma depois da equalização", generate_graph = True))
            elif (self.ui.histogram_window_ui.radioButton_2.isChecked()):
                converted_matrix = rgb_histogram_equalization(self.matrix)
                QTimer.singleShot(2000, lambda: rgb_histogram(self.matrix, title = "Histograma de distribuição de cores", generate_graph = True))
                QTimer.singleShot(2000, lambda: rgb_histogram(converted_matrix, title = "Histograma de distribuição de cores depois da equalização", generate_graph = True))
        self.apply_transformation(converted_matrix)

    def apply_spatial_filtering(self, img_path):

        # Adding spatial filtering
        self.ui.main_layout.removeWidget(self.ui.left_menu)
        self.ui.left_menu.hide()
        self.ui.main_layout.insertWidget(0, self.ui.spatial_filtering_menu)
        self.ui.spatial_filtering_menu.show()

        # Reading the image
        self.matrix = conversion_to_matrix(img_path)
        self.final_image = conversion_to_image(self.matrix)

    def apply_geometric_operations(self, img_path):

        # Adding frequency domain
        self.ui.main_layout.removeWidget(self.ui.left_menu)
        self.ui.left_menu.hide()
        self.ui.main_layout.insertWidget(0, self.ui.geometric_operations_menu)
        self.ui.geometric_operations_menu.show()

        # Reading the image
        self.matrix = conversion_to_matrix(img_path)
        self.final_image = conversion_to_image(self.matrix)

    def apply_frequency_domain(self, img_path):

        # Adding frequency domain
        self.ui.main_layout.removeWidget(self.ui.left_menu)
        self.ui.left_menu.hide()
        self.ui.main_layout.insertWidget(0, self.ui.frequency_algorithms_menu)
        self.ui.frequency_algorithms_menu.show()

        # Reading the image
        self.matrix = conversion_to_matrix(img_path)
        self.final_image = conversion_to_image(self.matrix)

    def apply_colors_algorithms(self, img_path):

        # Adding colors
        self.ui.main_layout.removeWidget(self.ui.left_menu)
        self.ui.left_menu.hide()
        self.ui.main_layout.insertWidget(0, self.ui.colors_algorithms_menu)
        self.ui.colors_algorithms_menu.show()

        # Reading the image
        self.matrix = conversion_to_matrix(img_path)
        self.final_image = conversion_to_image(self.matrix)

    def active_button(self, selected_button):

        for button in self.button_list:
            if (button == selected_button):
                button.set_active(True)
            else:
                button.set_active(False)

    # Window to choose the algorithms type
    def select_algorithms(self, file_path):

        if (self.ui.select_part_window.exec()):

            # Checking which radiobutton was selected
            if (self.ui.select_part_window_ui.radioButton.isChecked()):

                # Going to intensity transformations "window"
                self.transformation(file_path)

            elif (self.ui.select_part_window_ui.radioButton_2.isChecked()):
                
                # Going to histogram function
                self.apply_histogram(file_path)

            elif (self.ui.select_part_window_ui.radioButton_3.isChecked()):

                # Going to spatial_filtering function
                self.apply_spatial_filtering(file_path)

            elif (self.ui.select_part_window_ui.radioButton_4.isChecked()):
                self.apply_geometric_operations(file_path)

            elif (self.ui.select_part_window_ui.radioButton_5.isChecked()):

                # Going to frequency domain function
                self.apply_frequency_domain(file_path)

            elif (self.ui.select_part_window_ui.radioButton_6.isChecked()):
                self.apply_colors_algorithms(file_path)

    # applying the transformations
    # thresholding
    def open_thresholding(self):

        self.active_button(self.ui.button_thresholding)

        # Executing the thresholding dialog
        if (self.ui.thresholding_window.exec()):

            # Taking the value
            T = self.ui.thresholding_window_ui.lineEdit.text()

            try:
                T = int(T)
                converted_matrix = thresholding(self.matrix, T)
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("O valor deve ser inteiro")
                return

    # Negative
    def open_negative(self):

        self.active_button(self.ui.button_negative)

        # Executing the negative dialog
        if (self.ui.negative_window.exec()):

            # Taking the value
            L = self.ui.negative_window_ui.lineEdit.text()
            
            try:
                L = float(L)
                converted_matrix = negative(self.matrix, L)
                self.apply_transformation(converted_matrix)
            except ValueError:
                if (L.strip() != ""):
                    print("O valor deve ser um número")
                    return
                converted_matrix = negative(self.matrix)
                self.apply_transformation(converted_matrix)

    # Brightness
    def open_brightness(self):

        self.active_button(self.ui.button_brightness)

        # Executing the brightness window
        if (self.ui.brightness_window.exec()):

            # Taking the value
            k = self.ui.brightness_window_ui.lineEdit.text()

            try:
                k = float(k)
                converted_matrix = brightness(self.matrix, k)
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("O valor deve ser um número!")
                return 

    # Logarithm
    def open_logarithm(self):

        self.active_button(self.ui.button_logarithm_transformation)

        # Executing the logarith dialog
        if (self.ui.logarithm_transformation_window.exec()):

            # Taking the value
            c = self.ui.logarithm_transformation_window_ui.lineEdit.text()

            try:
                c = float(c)
                converted_matrix = negative(self.matrix, c)
                self.apply_transformation(converted_matrix)
            except ValueError:
                if (c.strip() != ""):
                    print("O valor deve ser um número")
                    return
                converted_matrix = logarithm_transformation(self.matrix)
                self.apply_transformation(converted_matrix)

    # Power law
    def open_power_law(self):

        self.active_button(self.ui.button_power_law)

        # Executing the power law dialog
        if (self.ui.power_law_window.exec()):

            # Taking the value of gamma
            gamma = self.ui.power_law_window_ui.lineEdit.text()

            try:
                gamma = float(gamma)
                converted_matrix = power_law_transformation(self.matrix, gamma)
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("O valor deve ser float")
                return

    # Piecewise linear
    def opne_piecewise_linear(self):

        self.active_button(self.ui.button_piecewise_linear)

        # Open the dialog window
        dialog = DialogCanvas(self)
        if (dialog.exec()):
            try:
                # Executing the algorithm
                converted_matrix = piecewise_linear(self.matrix, dialog.get_points())
                self.apply_transformation(converted_matrix)

            except ValueError as e:
                QMessageBox.warning(self, "Erro", str(e))
                return

    # Contrast stretching
    def open_contrast_stretching(self):

        self.active_button(self.ui.button_contrast_stretching)

        # Executing the algorithm
        converted_matrix = contrast_stretching(self.matrix)
        self.apply_transformation(converted_matrix)

    # Intensity level slicing
    def open_intensity_level_slicing(self):

        self.active_button(self.ui.button_intensity_level_slicing)

        if (self.ui.intensity_level_slicing_window.exec()):

            min_value = self.ui.intensity_level_slicing_window_ui.lineEdit.text()
            max_value = self.ui.intensity_level_slicing_window_ui.lineEdit_3.text()
            algorithm = self.ui.intensity_level_slicing_window_ui.lineEdit_2.text().strip().lower()

            try:
                min_value = int(min_value)
                max_value = int(max_value)
                converted_matrix = intensity_level_slicing(self.matrix, min_value, max_value, algorithm)
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("Os valores mínimo e máximo devem ser inteiros!")
                return

    # Bit plane slicing
    def open_bit_plane_slicing(self):

        self.active_button(self.ui.button_bit_plane_slicing)

        # Excecuting the bit plane window
        if (self.ui.bit_plane_slicing_window.exec()):

            bit_reference = self.ui.bit_plane_slicing_window_ui.lineEdit.text()

            try:
                bit_reference = int(bit_reference)
                converted_matrix = bit_plane_slicing(self.matrix, bit_reference)
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("O valor deve ser inteiro")
                return

    # Steganography
    def open_steganography_apply(self):

        self.active_button(self.ui.button_steganography_apply)

        # Executing the steganography window
        if (self.ui.steganopgraphy_apply_window.exec()):
            message = self.ui.steganopgraphy_apply_window_ui.lineEdit.text()
            converted_matrix = steganography_apply(self.matrix, message)
            self.apply_transformation(converted_matrix)

    def open_steganography_decode(self):

        self.active_button(self.ui.button_steganography_undo)

        # Executing the steganography window
        message = steganography_decoder(self.matrix)
        self.ui.steganography_decode_window_ui.retranslateUi(self.ui.steganography_decode_window, message)
        self.ui.steganography_decode_window.exec()

    def apply_transformation(self, converted_matrix: np.ndarray = None):
        self.final_image = conversion_to_image(converted_matrix)
        self.final_image = ImageQt(self.final_image)
        self.final_image = QPixmap.fromImage(self.final_image)
        self.final_image_show = self.resize_image_display(self.final_image)
        self.ui.ui_pages.label_2.setPixmap(self.final_image_show)

    # Spatial filtering algorithms
    # Convolution
    def open_convolution_apply(self):

        self.active_button(self.ui.button_convolution)

        # Executing the convolution window
        if (self.ui.convolution_apply_window.exec()):

            # Taking the value
            T = self.ui.convolution_apply_window_ui.lineEdit.text()

            try:
                T = int(T)
                matrix_dialog = ConvolutionMatrixDialog(T, self)

                if matrix_dialog.exec():
                    kernel = matrix_dialog.get_matrix()
                    converted_matrix = convolution(self.matrix, kernel, norm=True)
                    print("Pronto!")
                    self.apply_transformation(converted_matrix)

            except ValueError:
                print("Erro de valor!")
            
    # Mean filter
    def open_mean_filter_apply(self):

        self.active_button(self.ui.button_mean)

        # Executing the mean window
        if (self.ui.mean_filter_apply_window.exec()):

            # Taking the value
            T = self.ui.mean_filter_apply_window_ui.lineEdit.text()

            try:
                T = int(T)
                converted_matrix = mean_filter(self.matrix, T)
                print("Pronto!")
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("O valor deve ser inteiro")
                return

    # Gaussian smoothing filter
    def open_gaussian_smoothing_filter_apply(self):
        
        self.active_button(self.ui.button_gaussian)

        if (self.ui.gaussian_smoothing_apply_window.exec()):

            # Taking the values
            kernel_size = self.ui.gaussian_smoothing_apply_window_ui.lineEdit.text()
            standard_deviation = self.ui.gaussian_smoothing_apply_window_ui.lineEdit_2.text()

            try:
                kernel_size = int(kernel_size)
                standard_deviation = float(standard_deviation)
                converted_matrix = gaussian_smoothing(self.matrix, kernel_size, standard_deviation)
                print("Pronto!")
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("Os valores devem ser inteiro e decimal, respectivamente")
                return 

    # Median Filter
    def open_median_filter_apply(self):

        self.active_button(self.ui.button_median)

        # Executing the median window
        if (self.ui.median_filter_apply_window.exec()):

            # Taking the value
            T = self.ui.median_filter_apply_window_ui.lineEdit.text()

            try:
                T = int(T)
                converted_matrix = median_filter(self.matrix, T)
                print("Pronto!")
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("O valor deve ser inteiro")
                return

    # Laplacian filter
    def open_laplacian_filter_apply(self):

        self.active_button(self.ui.button_laplacian)

        # Executing laplacian window
        if (self.ui.laplacian_filter_apply_window.exec()):

            # Taking the radio value
            if (self.ui.laplacian_filter_apply_window_ui.radioButton.isChecked()):
                kernel = 1
            elif (self.ui.laplacian_filter_apply_window_ui.radioButton_2.isChecked()):
                kernel = 2
            elif (self.ui.laplacian_filter_apply_window_ui.radioButton_3.isChecked()):
                kernel = 3
            elif (self.ui.laplacian_filter_apply_window_ui.radioButton_4.isChecked()):
                kernel = 4

            if (self.ui.laplacian_filter_apply_window_ui.radioButton_5.isChecked()):
                log = True
            elif (self.ui.laplacian_filter_apply_window_ui.radioButton_6.isChecked()):
                log = False

            dimension_log = self.ui.laplacian_filter_apply_window_ui.lineEdit.text()
            standard_deviation_log = self.ui.laplacian_filter_apply_window_ui.lineEdit_2.text()

            if (log):
                try:
                    dimension_log = int(dimension_log)
                    standard_deviation_log = float(standard_deviation_log)
                except ValueError:
                    print("Os valores devem ser números!")
            else:
                dimension_log = 0
                standard_deviation_log = 0


            converted_matrix = laplacian(self.matrix, kernel, dimension_log, standard_deviation_log, log)
            print("Pronto!")
            self.apply_transformation(converted_matrix)

    # High boost filter
    def open_highboost_filter_apply(self):

        self.active_button(self.ui.button_highboost)

        # Executing highboost window
        if (self.ui.high_boost_filter_apply_window.exec()):

            # Taking the values
            gauss_dimension_filter = self.ui.high_boost_filter_apply_window_ui.lineEdit.text()
            gauss_standard_deviation = self.ui.high_boost_filter_apply_window_ui.lineEdit_2.text()
            k = self.ui.high_boost_filter_apply_window_ui.lineEdit_3.text()

            try:
                gauss_dimension_filter = int(gauss_dimension_filter)
                gauss_standard_deviation = float(gauss_standard_deviation)
                k = float(k)
                converted_matrix = high_boost(self.matrix, gauss_dimension_filter, gauss_standard_deviation, k)
                print("Pronto!")
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("Os valores devem ser inteiro, float e float, respectivamente")
                return

    # Sobel
    def open_sobel_apply(self):

        self.active_button(self.ui.button_sobel)

        # Executing sobel window
        if (self.ui.sobel_apply_window.exec()):

            # Taking the raio value
            if (self.ui.sobel_apply_window_ui.radioButton.isChecked()):
                converted_matrix = sobel(self.matrix, 'x')
            elif (self.ui.sobel_apply_window_ui.radioButton_2.isChecked()):
                converted_matrix = sobel(self.matrix, 'y')

            # Applying the algorith result
            print("Pronto!")
            self.apply_transformation(converted_matrix)


    # Magnitude gradient
    def open_magnitude_gradient_apply(self):

        self.active_button(self.ui.button_magnitude_gradient)

        # Applying the algorithm
        converted_matrix = magnitude_gradient(self.matrix)
        print("Pronto!")
        self.apply_transformation(converted_matrix)

    # Geometric operations
    def open_scaling_apply(self):

        self.active_button(self.ui.scaling_button)

        # Executing scaling window
        if (self.ui.scaling_apply_window.exec()):

            # Selecting the alg type
            if (self.ui.scaling_apply_window_ui.radioButton.isChecked()):
                self.alg_type = 'nearest'
            elif (self.ui.scaling_apply_window_ui.radioButton_2.isChecked()):
                self.alg_type = 'bilinear'

            try:
                # Taking the values
                sx = float(self.ui.scaling_apply_window_ui.lineEdit.text())
                sy = float(self.ui.scaling_apply_window_ui.lineEdit_2.text())
                converted_matrix = scaling(self.matrix, sx, sy, self.alg_type)
                print("Pronto!")
                self.apply_transformation(converted_matrix)

            except ValueError as e:
                print("Os valores de sx e sy devem ser floats!")

    # Rotating
    def open_rotating_apply(self):

        self.active_button(self.ui.rotating_button)

        # Executing rotating window
        if (self.ui.rotating_apply_window.exec()):

            T = self.ui.rotating_apply_window_ui.lineEdit.text()

            try:
                self.rotation_angle = int(T)

                if (self.ui.rotating_apply_window_ui.radioButton.isChecked()):
                    self.alg_type = 'nearest'
                elif (self.ui.rotating_apply_window_ui.radioButton_2.isChecked()):
                    self.alg_type = 'bilinear'

                self.waiting_for_rotation_click = True
                self.ui.ui_pages.label_2.setCursor(Qt.CursorShape.CrossCursor)
            except ValueError:
                print("O angulo deve ser um numero!")

    # Frequency domain filters
    # DFT
    def open_dft_apply(self):

        self.active_button(self.ui.button_dft)
        self.original_matrix_shape = self.matrix.shape

        real_matrix, imaginary_matrix = discrete_fourier_transform(self.matrix)
        converted_matrix, shifted_complex_matrix = get_result_image(real_matrix, imaginary_matrix)
        self.shifted_complex_matrix = shifted_complex_matrix
       
        self.is_drawning_mask = True
        original_height, original_width = shifted_complex_matrix.shape[:2]
        self.mask_image = QImage(original_width, original_height, QImage.Format.Format_Grayscale8)
        self.mask_image.fill(QColor(255, 255, 255))

        self.ui.fft_paint_window.show()
        
        self.apply_transformation(converted_matrix)

    # Apply fft
    def open_fft_apply(self):

        self.active_button(self.ui.button_fft_apply)
        self.original_matrix_shape = self.matrix.shape

        # Obtaining the result matrices
        real_matrix, imaginary_matrix = fast_fourier_transform(self.matrix)

        # Applying the result
        converted_matrix, shifted_complex_matrix = get_result_image(real_matrix, imaginary_matrix)
        self.shifted_complex_matrix = shifted_complex_matrix

        self.is_drawning_mask = True
        original_height, original_width = shifted_complex_matrix.shape[:2]
        self.mask_image = QImage(original_width, original_height, QImage.Format.Format_Grayscale8)
        self.mask_image.fill(QColor(255, 255, 255))

        self.ui.fft_paint_window.show()
        
        print("Pronto!")
        self.apply_transformation(converted_matrix)

    # Inverse fourier
    def open_ifft_apply(self):

        # First checks to go on with the code
        condition1 = not hasattr(self, 'shifted_complex_matrix')
        condition2 = not hasattr(self, 'mask_image')

        if (condition1 or condition2 or self.mask_image is None):
            print("Não há nenhuma matriz fft para aplicar a inversa!")
            return

        self.ui.fft_paint_window.hide()
        self.active_button(None)

        # Extracting pixels from modified matrix
        width = self.mask_image.width()
        height = self.mask_image.height()
        pointer = self.mask_image.bits()
        mask_matrix = np.frombuffer(pointer, dtype = np.uint8).reshape((height, width))

        # Normalizing
        mask_matrix = mask_matrix / 255.0

        # Adjusting masj dimensions
        if (len(self.shifted_complex_matrix.shape) == 3):

            mask_matrix_expanded = np.expand_dims(mask_matrix, axis = 2)
            filtered_matrix = self.shifted_complex_matrix * mask_matrix_expanded

        else:
            filtered_matrix = self.shifted_complex_matrix * mask_matrix

        converted_matrix = inverse_fft(filtered_matrix)
        print("Pronto!")

        # Removing padding
        N = self.original_matrix_shape[0]
        M = self.original_matrix_shape[1]

        if (len(self.original_matrix_shape) == 3):
            converted_matrix = converted_matrix[:N, :M, :]
        else:
            converted_matrix = converted_matrix[:N, :M]

        self.is_drawning_mask = False
        self.apply_transformation(converted_matrix)

    # Colors algorithms
    def open_rgb_hsi(self):

        self.active_button(self.ui.button_get_hsi)

        self.H, self.S, self.I = convert_rgb_to_hsi(self.matrix)

        images_data = [
            (self.H, "Canal H (Matiz)"),
            (self.S, "Canal S (Saturação)"),
            (self.I, "Cancal I (Intensidade)")
        ]

        results_dialog = HSIDialog(images_data, self)
        results_dialog.exec()
        self.ui.get_hsi_window.exec()

    def open_hsi_rgb(self):

        self.active_button(self.ui.button_get_rgb)

        # Executing the window
        if (self.ui.get_rgb_window.exec()):

            if (self.ui.get_rgb_window_ui.radioButton.isChecked()):

                if (self.ui.get_rgb_window_2.exec()):

                    shift_h = self.ui.get_rgb_window_2_ui.lineEdit.text()
                    shift_s = self.ui.get_rgb_window_2_ui.lineEdit_2.text()
                    shift_i = self.ui.get_rgb_window_2_ui.lineEdit_3.text()
                
            elif (self.ui.get_rgb_window_ui.radioButton_2.isChecked()):
                shift_h = 0.0
                shift_s = 1.0
                shift_i = 1.0

            try:
                shift_h = float(shift_h)
                shift_s = float(shift_s)
                shift_i = float(shift_i)

                self.H, self.S, self.I = adjust_hsi_channels_2(self.H, self.S, self.I, shift_h, shift_s, shift_i)
                converted_matrix = convert_hsi_to_rgb(self.H, self.S, self.I)
                print("Pronto!")
                self.apply_transformation(converted_matrix)

            except ValueError:
                print("Os valores devem ser decimais!")

    # Grayscale Mean filter
    def open_grayscale_mean_color_apply(self):

        self.active_button(self.ui.button_grayscale_mean)

        # Applying the function
        converted_matrix = gray_scale_mean(self.matrix)
        print("Pronto!")
        self.apply_transformation(converted_matrix)

    # Grayscale weighted mean filter
    def open_grayscale_weighted_apply(self):

        self.active_button(self.ui.button_grayscale_weighted_mean)

        # Open the window
        if (self.ui.grayscale_weighted_mean_apply_window.exec()):

            # Taking the values
            wred = self.ui.grayscale_weighted_mean_apply_window_ui.lineEdit.text()
            wgreen = self.ui.grayscale_weighted_mean_apply_window_ui.lineEdit_2.text()
            wblue = self.ui.grayscale_weighted_mean_apply_window_ui.lineEdit_3.text()

            if (wred.strip() == ""):
                wred = 0.299
            if (wgreen.strip() == ""):
                wgreen = 0.587
            if (wblue.strip() == ""):
                wblue = 0.114

            # Applying the function
            try:
                wred = float(wred)
                wgreen = float(wgreen)
                wblue = float(wblue)
                converted_matrix = gray_scale_weigthted_arithmetic_mean(self.matrix, wred, wgreen, wblue)
                print("Pronto!")
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("Os valores devem ser numeros!")

    # Negative
    def open_negative_rgb(self):

        self.active_button(self.ui.button_rgb_negative)

        # Executing the negative dialog
        if (self.ui.negative_color_window.exec()):

            # Taking the value
            L = self.ui.negative_color_window_ui.lineEdit.text()
            
            try:
                L = float(L)
                converted_matrix = rgb_negative(self.matrix, L)
                self.apply_transformation(converted_matrix)
            except ValueError:
                if (L.strip() != ""):
                    print("O valor deve ser um número")
                    return
                converted_matrix = rgb_negative(self.matrix)
                self.apply_transformation(converted_matrix)

    # Chroma key
    def open_chroma_key(self):

        self.active_button(self.ui.button_chroma_key)

        # Executing chromakey window
        if (self.ui.chroma_key_window.exec()):

            r = self.ui.chroma_key_window_ui.lineEdit.text()
            g = self.ui.chroma_key_window_ui.lineEdit_2.text()
            b = self.ui.chroma_key_window_ui.lineEdit_3.text()
            tol = self.ui.chroma_key_window_ui.lineEdit_4.text()

            try:
                r = int(r)
                g = int(g)
                b = int(b)
                tol = float(tol)

                back_image_path, _ = QFileDialog.getOpenFileName(self, "Selecione a imagem de fundo", "", "Imagens (*.png *.jpg *.jpeg *.bmp)")    

                if (back_image_path):
                    back_image = conversion_to_matrix(back_image_path)
                    converted_matrix = chroma_key(self.matrix, back_image, color_vector = [r, g, b], tol = tol)
                    print("Pronto!")
                    self.apply_transformation(converted_matrix)         

            except ValueError:
                print("Os valores devem ser int, int, int e float, respectivamente!")

    # Adjust HSI
    def open_adjust_hsi_channels_apply(self):

        self.active_button(self.ui.button_adjust_hsi)

        # Executing color adjust window
        if (self.ui.adjust_hsi_channels_window.exec()):

            # Taking the values
            shift_h = self.ui.adjust_hsi_channels_window_ui.lineEdit.text()
            shift_s = self.ui.adjust_hsi_channels_window_ui.lineEdit_2.text()
            shift_i = self.ui.adjust_hsi_channels_window_ui.lineEdit_3.text()

            if (shift_h.strip() == ""):
                shift_h = 0.0
            if (shift_s.strip() == ""):
                shift_s = 1.0
            if (shift_i.strip() == ""):
                shift_i = 1.0

            try:
                shift_h = float(shift_h)
                shift_s = float(shift_s)
                shift_i = float(shift_i)

                converted_matrix = adjust_hsi_channels(self.matrix, shift_h, shift_s, shift_i)
                print("Pronto!")
                self.apply_transformation(converted_matrix)

            except ValueError:
                print("Os valores devem ser números!")

    def open_adjust_sepia_apply(self):

        self.active_button(self.ui.button_sepia_filter)

        # Applying sepia filter
        converted_matrix = sepia_rgb(self.matrix)
        print("Pronto!")
        self.apply_transformation(converted_matrix)

    # Adjust color balance
    def open_adjust_color_balance_apply(self):

        self.active_button(self.ui.button_adjust_color_balance)

        # Executing color adjust window
        if (self.ui.adjust_color_balance_window.exec()):

            # Taking the values
            shift_cr = self.ui.adjust_color_balance_window_ui.lineEdit.text()
            shift_mg = self.ui.adjust_color_balance_window_ui.lineEdit_2.text()
            shift_yb = self.ui.adjust_color_balance_window_ui.lineEdit_3.text()

            if (shift_cr.strip() == ""):
                shift_cr = 0.0
            if (shift_mg.strip() == ""):
                shift_mg = 0.0
            if (shift_yb.strip() == ""):
                shift_yb = 0.0

            try:
                shift_cr = float(shift_cr)
                shift_mg = float(shift_mg)
                shift_yb = float(shift_yb)

                converted_matrix = adjust_color_balance(self.matrix, shift_cr, shift_mg, shift_yb)
                print("Pronto!")
                self.apply_transformation(converted_matrix)

            except ValueError:
                print("Os valores devem ser números!")

    def get_image_coords(self, event):

        if (event.button() == Qt.MouseButton.LeftButton):

            label = self.ui.ui_pages.label_2
            pixmap = label.pixmap()

            if (pixmap is None or not hasattr(self, 'matrix')):
                return

            original_height, original_width = self.matrix.shape[:2]

            disp_width = pixmap.width()
            disp_height = pixmap.height()

            offset_x = (label.width() - disp_width) // 2
            offset_y = (label.height() - disp_height) // 2

            click_x = event.pos().x() - offset_x
            click_y = event.pos().y() - offset_y

            if (0 <= click_x < disp_width and 0 <= click_y < disp_height):
                original_x = int(click_x * (original_width / disp_width))
                original_y = int(click_y * (original_height / disp_height))
                pixel_value = self.matrix[original_y, original_x]

                if self.waiting_for_rotation_click:
                    converted_matrix = rotation(self.matrix, self.rotation_angle, original_x, original_y, self.alg_type)
                    self.apply_transformation(converted_matrix)
                    self.waiting_for_rotation_click = False
                    self.ui.ui_pages.label_2.unsetCursor()

    # Function to resize the image according to display  
    def resize_image_display(self, pixmap: QPixmap) -> QPixmap:

        if (pixmap.width() > 700 or pixmap.height() > 700):
            return pixmap.scaled(700, 700, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        return pixmap

    def label_mouse_press(self, event):
        if (self.waiting_for_rotation_click):
            self.get_image_coords(event)
            return

        if (self.is_drawning_mask and event.button() == Qt.MouseButton.LeftButton):
            self.drawning = True
            self.last_point = event.pos()

    def label_mouse_move(self, event):
        if (self.is_drawning_mask and self.drawning):
            point = event.pos()
            self.draw_on_image(self.last_point, point)
            self.last_point = point

    def label_mouse_release(self, event):
        if (self.is_drawning_mask and event.button() == Qt.MouseButton.LeftButton):
            self.drawning = False

    def draw_on_image(self, p1, p2):

        label = self.ui.ui_pages.label_2
        pixmap = label.pixmap()
        if (pixmap is None):
            return

        disp_width = pixmap.width()
        disp_height = pixmap.height()
        offset_x = (label.width() - disp_width) // 2
        offset_y = (label.height() - disp_height) // 2

        pix_p1 = QPoint(p1.x() - offset_x, p1.y() - offset_y)
        pix_p2 = QPoint(p2.x() - offset_x, p2.y() - offset_y)
        
        painter = QPainter(pixmap)
        pen = QPen(self.brush_color, self.brush_size, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawLine(pix_p1, pix_p2)

        if (self.mirror_brush):
            mirror_pixel1 = QPoint(disp_width - pix_p1.x(), disp_height - pix_p1.y())
            mirror_pixel2 = QPoint(disp_width - pix_p2.x(), disp_height - pix_p2.y())
            painter.drawLine(mirror_pixel1, mirror_pixel2)

        painter.end()
        label.setPixmap(pixmap)

        # Drawning matrix mask

        original_width = self.mask_image.width()
        original_height = self.mask_image.height()

        def map_point(p_pix):
            cx = max(0, min(p_pix.x() - offset_x, disp_width - 1))
            cy = max(0, min(p_pix.y() - offset_y, disp_height - 1))
            ox = int(cx * (original_width / disp_width))
            oy = int(cy * (original_height / disp_height))
            return QPoint(ox, oy)

        op1 = map_point(pix_p1)
        op2 = map_point(pix_p2)

        scale_x = original_width / disp_width
        original_brush_size = int(self.brush_size * scale_x)

        painter_mask = QPainter(self.mask_image)
        pen_mask = QPen(self.brush_color, original_brush_size, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)
        painter_mask.setPen(pen_mask)
        painter_mask.drawLine(op1, op2)

        if (self.mirror_brush):
            mirror_op1 = map_point(mirror_pixel1)
            mirror_op2 = map_point(mirror_pixel2)
            painter_mask.drawLine(mirror_op1, mirror_op2)

        painter_mask.end()

    def update_size(self, button):

        radioButtonSelected = button.text()
        if (radioButtonSelected == 'Fino'):
            self.brush_size = 4
        elif (radioButtonSelected == 'Médio'):
            self.brush_size = 7
        elif (radioButtonSelected == 'Grosso'):
            self.brush_size = 20

    def update_color(self, button):

        radioButtonSelected = button.text()
        if (radioButtonSelected == 'Preto'):
            self.brush_color = QColor(0, 0, 0)
        elif (radioButtonSelected == 'Cinza'):
            self.brush_color = QColor(128, 128, 128)
        elif (radioButtonSelected == 'Branco'):
            self.brush_color = QColor(255, 255, 255)

    def update_mirror(self, state):
        self.mirror_brush = (state != 0)


# main
def main():
    myappid = 'davi.calopimage.app.1' 
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except Exception as e:
        print(f"{e}")

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()