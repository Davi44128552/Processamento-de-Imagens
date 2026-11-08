# Importing os
import os

# Importing modules
from qt_core import *

# Importing pages
from gui.pages.ui_pages import Ui_StackedWidget

# Importing widgets
from gui.widgets.py_push_button import PyPushButton

# Importing dialogs
import gui.dialogs.dialog_one_input as one_input
import gui.dialogs.message_dialog as response
import gui.dialogs.dialog_three_input as three_input
import gui.dialogs.message_dialog as message_dialog
import gui.dialogs.dialog_method_select as dialog_method_select
import gui.dialogs.dialog_two_input as two_input
import gui.dialogs.radio_select_two_options as two_radio
import gui.dialogs.scaling_dialog as scaling_dialog
import gui.dialogs.dialog_laplacian as dialog_laplacian
import gui.dialogs.dialog_chroma_key as dialog_chroma
import gui.dialogs.histogram_dialog as histogram_dialog
import gui.dialogs.dialog_hsi_to_rgb as dialog_rgb
import gui.dialogs.paint_dialog as paint
import gui.dialogs.rotating_dialog as rotating_dialog

# Path to select images
app_path = os.path.abspath(os.getcwd())
folder = "gui/images/"
path = os.path.join(app_path, folder)

# Main window
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # Setting the initial parameters
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # Creating central widget
        self.central_frame = QFrame()

        # Creating and cofiguring the main layout
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Creating and cofiguring the extra frames
        # Left menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # Left menu layout
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Top Frame menu
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(40)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")

        # Top frame layout
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # Top bottoms
        self.toggle_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.toggle_button2 = PyPushButton(text = "Abrir Imagem", icon_path = "folder.svg")
        self.toggle_button3 = PyPushButton(text = "Pegar Imagem Aleatória", icon_path = "random.svg")

        # Add buttons
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.toggle_button2)
        self.left_menu_top_layout.addWidget(self.toggle_button3)

        # Menu spacer
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Bottom frame menu
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")

        # Bottom frame layout
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # bottom button
        self.config_button = PyPushButton(text = "Ajuda", icon_path = "qmark.svg")

        # Add buttons
        self.left_menu_bottom_layout.addWidget(self.config_button)

        # Label version
        self.left_menu_version = QLabel("v1.2.0")
        self.left_menu_version.setAlignment(Qt.AlignCenter)
        self.left_menu_version.setMaximumHeight(30)
        self.left_menu_version.setMinimumHeight(30)
        self.left_menu_version.setStyleSheet("color: #c3ccdf")

        # Add to layout
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_version)

        # Adding the histogram equalization frame
        self.equalization_hist_menu = QFrame()
        self.equalization_hist_menu.setStyleSheet("background-color: #44475a")
        self.equalization_hist_menu.setMaximumWidth(50)
        self.equalization_hist_menu.setMinimumWidth(50)

        # Left menu layout
        self.equalization_hist_menu_layout = QVBoxLayout(self.equalization_hist_menu)
        self.equalization_hist_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.equalization_hist_menu_layout.setSpacing(0)

        # Adding the transformations frame
        self.transformation_menu = QFrame()
        self.transformation_menu.setStyleSheet("background-color: #44475a")
        self.transformation_menu.setMaximumWidth(50)
        self.transformation_menu.setMinimumWidth(50)

        # Left menu layout
        self.transformation_menu_layout = QVBoxLayout(self.transformation_menu)
        self.transformation_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.transformation_menu_layout.setSpacing(0)

        # Adding the spatial filtering frame
        self.spatial_filtering_menu = QFrame()
        self.spatial_filtering_menu.setStyleSheet("background-color: #44475a")
        self.spatial_filtering_menu.setMaximumWidth(50)
        self.spatial_filtering_menu.setMinimumWidth(50)

        # Spatial filtering left menu layout
        self.spatial_filtering_menu_layout = QVBoxLayout(self.spatial_filtering_menu)
        self.spatial_filtering_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.spatial_filtering_menu_layout.setSpacing(0)

        # Adding geometric operations frame
        self.geometric_operations_menu = QFrame()
        self.geometric_operations_menu.setStyleSheet("background-color: #44475a")
        self.geometric_operations_menu.setMaximumWidth(50)
        self.geometric_operations_menu.setMinimumWidth(50)

        # Geometric operations left menu layout
        self.geometric_operations_menu_layout = QVBoxLayout(self.geometric_operations_menu)
        self.geometric_operations_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.geometric_operations_menu_layout.setContentsMargins(0, 0, 0, 0)

        # Adding the frequency domain algorithms
        self.frequency_algorithms_menu = QFrame()
        self.frequency_algorithms_menu.setStyleSheet("background-color: #44475a")
        self.frequency_algorithms_menu.setMaximumWidth(50)
        self.frequency_algorithms_menu.setMinimumWidth(50)

        self.frequency_algorithms_menu_layout = QVBoxLayout(self.frequency_algorithms_menu)
        self.frequency_algorithms_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.frequency_algorithms_menu_layout.setSpacing(0)

        # Adding the colors algorithms frame
        self.colors_algorithms_menu = QFrame()
        self.colors_algorithms_menu.setStyleSheet("background-color: #44475a")
        self.colors_algorithms_menu.setMaximumWidth(50)
        self.colors_algorithms_menu.setMinimumWidth(50)

        # Colors algorithms left menu layout
        self.colors_algorithms_menu_layout = QVBoxLayout(self.colors_algorithms_menu)
        self.colors_algorithms_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.colors_algorithms_menu_layout.setSpacing(0)

        # Configuring the buttons
        self.toggle2_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.toggle_histogram_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.toggle_spatial_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.button_thresholding = PyPushButton(text = "Limiarização", icon_path = "icon1.svg")
        self.button_negative = PyPushButton(text = "Negativa", icon_path = "icon2.svg")
        self.button_brightness = PyPushButton(text = "Brilho", icon_path = "icon10.svg")
        self.button_logarithm_transformation = PyPushButton(text = "Transformação Logarítmica", icon_path = "icon3.svg")
        self.button_power_law = PyPushButton(text = "Transformação gamma", icon_path = "icon4.svg")
        self.button_piecewise_linear = PyPushButton(text = "Transformação Linear definida por Partes", icon_path = "piecewise.svg")
        self.button_contrast_stretching = PyPushButton(text = "Alongamento de contraste", icon_path = "icon5.svg")
        self.button_intensity_level_slicing = PyPushButton(text = "Fatiamento por intensidade", icon_path = "icon7.svg")
        self.button_bit_plane_slicing = PyPushButton(text = "Fatiamento por planos de bits", icon_path = "icon6.svg")
        self.button_steganography_apply = PyPushButton(text = "Aplicar Esteganografia", icon_path = "icon8.svg")
        self.button_steganography_undo = PyPushButton(text = "Decodificar Esteganografia", icon_path = "icon9.svg")
        self.transformation_download_button = PyPushButton(text = "Baixar Imagem", icon_path = "download.svg")        
        self.histogram_download_button = PyPushButton(text = "Baixar Imagem", icon_path = "download.svg")        
        self.button_transformation_go_back = PyPushButton(text = "Voltar", icon_path = "arrow.svg")
        self.button_histogram_go_back = PyPushButton(text = "Voltar", icon_path = "arrow.svg")

        # Spatial filtering buttons
        self.toggle_spatial_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.button_convolution = PyPushButton(text = "Convolução", icon_path = "convolution.svg")
        self.button_mean = PyPushButton(text = "Suavização da Média", icon_path = "mean.svg")
        self.button_gaussian = PyPushButton(text = "Gaussiano", icon_path = "gaussian_smoothing.svg")
        self.button_median = PyPushButton(text = "Suavização da Mediana", icon_path = "median_filter.svg")
        self.button_laplacian = PyPushButton(text = "Filtro laplaciano", icon_path = "laplacian.svg")
        self.button_highboost = PyPushButton(text = "Filtro por High-boost", icon_path = "highboost.svg")
        self.button_sobel = PyPushButton(text = "Sobel", icon_path = "sobel.svg")
        self.button_magnitude_gradient = PyPushButton(text = "Detecção pelo Gradiente", icon_path = "magnitude_gradient.svg")
        self.button_spatial_go_back = PyPushButton(text = "Voltar", icon_path = "arrow.svg")
        self.spatial_download_button = PyPushButton(text = "Baixar Imagem", icon_path = "download.svg")

        # Geometric operations buttons
        self.toggle_geometric_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.scaling_button = PyPushButton(text = "Aplicar Escala", icon_path = "scale.svg")
        self.rotating_without_pivot_button = PyPushButton(text = "Aplicar Rotação Simples", icon_path = "rotate.svg")
        self.rotating_button = PyPushButton(text = "Aplicar Rotação com Pivô", icon_path = "rotate.svg")
        self.button_geometric_go_back = PyPushButton(text = "Voltar", icon_path = "arrow.svg")
        self.geometric_download_button = PyPushButton(text = "Baixar Imagem", icon_path = "download.svg")

        # Frequency domain filtering buttons
        self.toggle_frequency_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.button_dft = PyPushButton(text = "Transformada Discreta de Fourier", icon_path = "dft.svg")
        self.button_fft_apply = PyPushButton(text = "Aplicar Transformada Rápida de Fourier", icon_path = "fft.svg")
        self.button_inverse_fourier = PyPushButton(text = "Transformada Inversa", icon_path = "inverse_fft.svg")
        self.button_frequency_go_back = PyPushButton(text = "Voltar", icon_path = "arrow.svg")
        self.frequency_download_button = PyPushButton(text = "Baixar Imagem", icon_path = "download.svg")

        # Colors algorithms
        self.toggle_color_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.button_get_hsi = PyPushButton(text = "Converter RGB para HSI", icon_path = "convert.svg")
        self.button_get_rgb = PyPushButton(text = "Converter HSI para RGB", icon_path = "convert.svg")
        self.button_grayscale_mean = PyPushButton(text = "Escala de cinza pela média", icon_path = "grayscale_mean.svg")
        self.button_grayscale_weighted_mean = PyPushButton(text = "Escala de cinza por média ponderada", icon_path = "grayscale_weighted_mean.svg")
        self.button_chroma_key = PyPushButton(text = "Chroma Key", icon_path = "chroma_key.svg")
        self.button_adjust_hsi = PyPushButton(text = "Ajustar canais HSI", icon_path = "grayscale_weighted_mean.svg")
        self.button_adjust_color_balance = PyPushButton(text = "Ajustar balancemanto de cores", icon_path = "grayscale_weighted_mean.svg")
        self.button_sepia_filter = PyPushButton(text = "Filtro sépia", icon_path = "sepia.svg")
        self.button_colors_go_back = PyPushButton(text = "Voltar", icon_path = "arrow.svg")
        self.button_colors_download_button = PyPushButton(text = "Baixar Imagem", icon_path = "download.svg")
        
        # Adding the buttons to layout
        self.equalization_hist_menu_layout.addWidget(self.toggle_histogram_button)
        self.hist_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.equalization_hist_menu_layout.addItem(self.hist_spacer)
        self.equalization_hist_menu_layout.addWidget(self.histogram_download_button)
        self.equalization_hist_menu_layout.addWidget(self.button_histogram_go_back)
        self.equalization_hist_menu.hide()

        self.transformation_menu_layout.addWidget(self.toggle2_button)
        self.transformation_menu_layout.addWidget(self.button_thresholding)
        self.transformation_menu_layout.addWidget(self.button_negative)
        self.transformation_menu_layout.addWidget(self.button_brightness)
        self.transformation_menu_layout.addWidget(self.button_logarithm_transformation)
        self.transformation_menu_layout.addWidget(self.button_power_law)
        self.transformation_menu_layout.addWidget(self.button_piecewise_linear)
        self.transformation_menu_layout.addWidget(self.button_contrast_stretching)
        self.transformation_menu_layout.addWidget(self.button_intensity_level_slicing)
        self.transformation_menu_layout.addWidget(self.button_bit_plane_slicing)
        self.transformation_menu_layout.addWidget(self.button_steganography_apply)
        self.transformation_menu_layout.addWidget(self.button_steganography_undo)
        self.transformation_menu_layout.addWidget(self.transformation_download_button)
        self.transformation_menu_layout.addWidget(self.button_transformation_go_back)
        self.transformation_menu.hide()

        self.spatial_filtering_menu_layout.addWidget(self.toggle_spatial_button)
        self.spatial_filtering_menu_layout.addWidget(self.button_convolution)
        self.spatial_filtering_menu_layout.addWidget(self.button_mean)
        self.spatial_filtering_menu_layout.addWidget(self.button_gaussian)
        self.spatial_filtering_menu_layout.addWidget(self.button_median)
        self.spatial_filtering_menu_layout.addWidget(self.button_laplacian)
        self.spatial_filtering_menu_layout.addWidget(self.button_highboost)
        self.spatial_filtering_menu_layout.addWidget(self.button_sobel)
        self.spatial_filtering_menu_layout.addWidget(self.button_magnitude_gradient)
        self.spatial_filtering_menu_layout.addWidget(self.spatial_download_button)
        self.spatial_filtering_menu_layout.addWidget(self.button_spatial_go_back)
        self.spatial_filtering_menu.hide()

        self.geometric_operations_menu_layout.addWidget(self.toggle_geometric_button)
        self.geometric_operations_menu_layout.addWidget(self.scaling_button)
        self.geometric_operations_menu_layout.addWidget(self.rotating_without_pivot_button)
        self.geometric_operations_menu_layout.addWidget(self.rotating_button)
        self.geometric_operations_menu_layout.addWidget(self.geometric_download_button)
        self.geometric_operations_menu_layout.addWidget(self.button_geometric_go_back)
        self.geometric_operations_menu.hide()

        self.frequency_algorithms_menu_layout.addWidget(self.toggle_frequency_button)
        self.frequency_algorithms_menu_layout.addWidget(self.button_dft)
        self.frequency_algorithms_menu_layout.addWidget(self.button_fft_apply)
        self.frequency_algorithms_menu_layout.addWidget(self.button_inverse_fourier)
        self.frequency_algorithms_menu_layout.addWidget(self.frequency_download_button)
        self.frequency_algorithms_menu_layout.addWidget(self.button_frequency_go_back)
        self.frequency_algorithms_menu.hide()

        self.colors_algorithms_menu_layout.addWidget(self.toggle_color_button)
        self.colors_algorithms_menu_layout.addWidget(self.button_get_hsi)
        self.colors_algorithms_menu_layout.addWidget(self.button_get_rgb)
        self.colors_algorithms_menu_layout.addWidget(self.button_grayscale_mean)
        self.colors_algorithms_menu_layout.addWidget(self.button_grayscale_weighted_mean)
        self.colors_algorithms_menu_layout.addWidget(self.button_chroma_key)
        self.colors_algorithms_menu_layout.addWidget(self.button_adjust_hsi)
        self.colors_algorithms_menu_layout.addWidget(self.button_adjust_color_balance)
        self.colors_algorithms_menu_layout.addWidget(self.button_sepia_filter)
        self.colors_algorithms_menu_layout.addWidget(self.button_colors_download_button)
        self.colors_algorithms_menu_layout.addWidget(self.button_colors_go_back)
        self.colors_algorithms_menu.hide()

        # Content
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Top bar
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        # Left label to top bar
        self.top_label_left = QLabel("Aplicação para processamento de imagens")

        # Top spacer
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Right label to top bar
        self.top_label_right = QLabel("CALOPIMAGE")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # Add to layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # Bottom bar
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        # Left label to bottom bar
        self.bottom_label_left = QLabel("Criado por: Davi I. L. Souza")

        # bottom spacer
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Right label to bottom bar
        self.bottom_label_right = QLabel("© 2026")

        # Add to layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # Application pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page1)

        # Adding content to the page
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # Add widgets to app
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # Configuring the chapter dialog box
        self.select_part_window = QDialog()
        self.select_part_window_ui = dialog_method_select.Ui_Dialog()
        self.select_part_window_ui.setupUi(self.select_part_window)
        self.select_part_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.select_part_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "calopsita_appimage.png"))))
        self.select_part_window.setWindowTitle("Seleção de algoritmos")

        # Configuring the dialog box
        self.thresholding_window = QDialog()
        self.thresholding_window_ui = one_input.Ui_Dialog()
        self.thresholding_window_ui.setupUi(self.thresholding_window)
        self.thresholding_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.thresholding_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon1.svg"))))
        self.thresholding_window.setWindowTitle("Limiarização")

        self.brightness_window = QDialog()
        self.brightness_window_ui = one_input.Ui_Dialog()
        self.brightness_window_ui.setupUi(self.brightness_window)
        self.brightness_window_ui.retranslateUi(self.brightness_window, "Escreva um valor para ajustar o brilho", "1")
        self.brightness_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.brightness_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon10.svg"))))
        self.brightness_window.setWindowTitle("Brilho")

        self.negative_window = QDialog()
        self.negative_window_ui = one_input.Ui_Dialog()
        self.negative_window_ui.setupUi(self.negative_window)
        self.negative_window_ui.retranslateUi(self.negative_window, "Escreva um valor para L", "")
        self.negative_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.negative_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon2.svg"))))
        self.negative_window.setWindowTitle("Negativa")

        self.logarithm_transformation_window = QDialog()
        self.logarithm_transformation_window_ui = one_input.Ui_Dialog()
        self.logarithm_transformation_window_ui.setupUi(self.logarithm_transformation_window)
        self.logarithm_transformation_window_ui.retranslateUi(self.logarithm_transformation_window, "Escreva um valor para c", "")
        self.logarithm_transformation_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.logarithm_transformation_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon3.svg"))))
        self.logarithm_transformation_window.setWindowTitle("Transformação logarítmica")

        self.power_law_window = QDialog()
        self.power_law_window_ui = one_input.Ui_Dialog()
        self.power_law_window_ui.setupUi(self.power_law_window)
        self.power_law_window_ui.retranslateUi(self.power_law_window, "Escreva um valor para gamma", "1")
        self.power_law_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.power_law_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon4.svg"))))
        self.power_law_window.setWindowTitle("Transformação Gamma")

        self.intensity_level_slicing_window = QDialog()
        self.intensity_level_slicing_window_ui = scaling_dialog.Ui_Dialog()
        self.intensity_level_slicing_window_ui.setupUi(self.intensity_level_slicing_window)
        self.intensity_level_slicing_window_ui.retranslateUi(self.intensity_level_slicing_window, label1 = u"Valor mínimo", label2 = u"Valor máximo", alg1 = u"Binary", alg2 = u"Preserve")
        self.intensity_level_slicing_window.setStyleSheet("background-color: #44475a; font: 700 10pt 'Segoe UI'; color: white")
        self.intensity_level_slicing_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon7.svg"))))
        self.intensity_level_slicing_window.setWindowTitle("Transformação por nível de intensidade")

        self.bit_plane_slicing_window = QDialog()
        self.bit_plane_slicing_window_ui = one_input.Ui_Dialog()
        self.bit_plane_slicing_window_ui.setupUi(self.bit_plane_slicing_window)
        self.bit_plane_slicing_window_ui.retranslateUi(self.bit_plane_slicing_window, "Escreva um plano de bit de referência (entre 0 e 7)", "")
        self.bit_plane_slicing_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.bit_plane_slicing_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon6.svg"))))
        self.bit_plane_slicing_window.setWindowTitle("Transformação por planos de bits")

        self.steganopgraphy_apply_window = QDialog()
        self.steganopgraphy_apply_window_ui = one_input.Ui_Dialog()
        self.steganopgraphy_apply_window_ui.setupUi(self.steganopgraphy_apply_window)
        self.steganopgraphy_apply_window_ui.retranslateUi(self.steganopgraphy_apply_window, "Escreva uma mensagem qualquer", "")
        self.steganopgraphy_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.steganopgraphy_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon8.svg"))))
        self.steganopgraphy_apply_window.setWindowTitle("Aplicar Esteganografia")

        self.steganography_decode_window = QDialog()
        self.steganography_decode_window_ui = response.Ui_Dialog()
        self.steganography_decode_window_ui.setupUi(self.steganography_decode_window)
        self.steganography_decode_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.steganography_decode_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon9.svg"))))
        self.steganography_decode_window.setWindowTitle("Esteganografia decodificada")

        # Histogram windows
        self.histogram_window = QDialog()
        self.histogram_window_ui = histogram_dialog.Ui_Dialog()
        self.histogram_window_ui.setupUi(self.histogram_window)
        self.histogram_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.histogram_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, ""))))
        self.histogram_window.setWindowTitle("Histograma")

        # Spatial algorithms windows
        # Convolution
        self.convolution_apply_window = QDialog()
        self.convolution_apply_window_ui = one_input.Ui_Dialog()
        self.convolution_apply_window_ui.setupUi(self.convolution_apply_window)
        self.convolution_apply_window_ui.retranslateUi(self.convolution_apply_window, "Escreva o tamanho do kernel", "")
        self.convolution_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.convolution_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "convolution.svg"))))
        self.convolution_apply_window.setWindowTitle("Convolução")

        # Mean filter
        self.mean_filter_apply_window = QDialog()
        self.mean_filter_apply_window_ui = one_input.Ui_Dialog()
        self.mean_filter_apply_window_ui.setupUi(self.mean_filter_apply_window)
        self.mean_filter_apply_window_ui.retranslateUi(self.mean_filter_apply_window, "Escreva o tamanho do kernel", "")
        self.mean_filter_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.mean_filter_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "mean.svg"))))
        self.mean_filter_apply_window.setWindowTitle("Filtro de Média")

        # Gaussian smoothing
        self.gaussian_smoothing_apply_window = QDialog()
        self.gaussian_smoothing_apply_window_ui = two_input.Ui_Dialog()
        self.gaussian_smoothing_apply_window_ui.setupUi(self.gaussian_smoothing_apply_window)
        self.gaussian_smoothing_apply_window_ui.retranslateUi(self.gaussian_smoothing_apply_window, "Escreva o tamanho do kernel", "Escreva o valor do desvio padrão")
        self.gaussian_smoothing_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.gaussian_smoothing_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "gaussian_smoothing.svg"))))
        self.gaussian_smoothing_apply_window.setWindowTitle("Filtro Gaussiano")

        # Median filter
        self.median_filter_apply_window = QDialog()
        self.median_filter_apply_window_ui = one_input.Ui_Dialog()
        self.median_filter_apply_window_ui.setupUi(self.median_filter_apply_window)
        self.median_filter_apply_window_ui.retranslateUi(self.median_filter_apply_window, "Escreva o tamanho do kernel", "")
        self.median_filter_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.median_filter_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "median_filter.svg"))))
        self.median_filter_apply_window.setWindowTitle("Filtro de Mediana")

        # Laplacian filter
        self.laplacian_filter_apply_window = QDialog()
        self.laplacian_filter_apply_window_ui = dialog_laplacian.Ui_Dialog()
        self.laplacian_filter_apply_window_ui.setupUi(self.laplacian_filter_apply_window)
        self.laplacian_filter_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.laplacian_filter_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "laplacian.svg"))))
        self.laplacian_filter_apply_window.setWindowTitle("Filtro Laplaciano")

        # High boost
        self.high_boost_filter_apply_window = QDialog()
        self.high_boost_filter_apply_window_ui = three_input.Ui_Dialog()
        self.high_boost_filter_apply_window_ui.setupUi(self.high_boost_filter_apply_window)
        self.high_boost_filter_apply_window_ui.retranslateUi(self.high_boost_filter_apply_window, "Dimensão do filtro gaussiano", "Desvio padrão do filtro de gauss", "Fator de amplificação")
        self.high_boost_filter_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.high_boost_filter_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "highboost.svg"))))
        self.high_boost_filter_apply_window.setWindowTitle("Filtro High-boost")

        # Sobel
        self.sobel_apply_window = QDialog()
        self.sobel_apply_window_ui = two_radio.Ui_Dialog()
        self.sobel_apply_window_ui.setupUi(self.sobel_apply_window)
        self.sobel_apply_window_ui.retranslateUi(self.sobel_apply_window, "Sx", "Sy")
        self.sobel_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.sobel_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "sobel.svg"))))
        self.sobel_apply_window.setWindowTitle("Sobel")

        # Geometric operations windows
        # Scaling
        self.scaling_apply_window = QDialog()
        self.scaling_apply_window_ui = scaling_dialog.Ui_Dialog()
        self.scaling_apply_window_ui.setupUi(self.scaling_apply_window)
        self.scaling_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.scaling_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "scale.svg"))))
        self.scaling_apply_window.setWindowTitle("Escala")

        # Simple rotating
        self.rotating_without_pivot_window = QDialog()
        self.rotating_without_pivot_window_ui = rotating_dialog.Ui_Dialog()
        self.rotating_without_pivot_window_ui.setupUi(self.rotating_without_pivot_window)
        self.rotating_without_pivot_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.rotating_without_pivot_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "rotate.svg"))))
        self.rotating_without_pivot_window.setWindowTitle("Rotação Simples")

        # Rotating
        self.rotating_apply_window = QDialog()
        self.rotating_apply_window_ui = rotating_dialog.Ui_Dialog()
        self.rotating_apply_window_ui.setupUi(self.rotating_apply_window)
        self.rotating_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.rotating_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "rotate.svg"))))
        self.rotating_apply_window.setWindowTitle("Rotação com pivô")

        # Frequency domain windows
        # DFT
        self.dft_apply_window = QDialog()
        self.dft_apply_window_ui = message_dialog.Ui_Dialog()
        self.dft_apply_window_ui.setupUi(self.dft_apply_window)
        self.dft_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.dft_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "dft.svg"))))
        self.dft_apply_window.setWindowTitle("Transformada Discreta de Fourier")

        # FFT Paint
        self.fft_paint_window = QDialog()
        self.fft_paint_window_ui = paint.Ui_Dialog()
        self.fft_paint_window_ui.setupUi(self.fft_paint_window)
        self.fft_paint_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.fft_paint_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "fft.svg"))))
        self.fft_paint_window.setWindowTitle("Transformada Rápida de Fourier")

        # Colors algorithms windows
        self.get_hsi_window = QDialog()
        self.get_hsi_window_ui = message_dialog.Ui_Dialog()
        self.get_hsi_window_ui.setupUi(self.get_hsi_window)
        self.get_hsi_window_ui.retranslateUi(self.get_hsi_window, "As matrizes H, S e I foram salvas na memória da aplicação!")
        self.get_hsi_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.get_hsi_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "convert.svg"))))
        self.get_hsi_window.setWindowTitle("Converter RGB - HSI")

        # HSI -> RGB
        self.get_rgb_window = QDialog()
        self.get_rgb_window_ui = dialog_rgb.Ui_Dialog()
        self.get_rgb_window_ui.setupUi(self.get_rgb_window)
        self.get_rgb_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.get_rgb_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "convert.svg"))))
        self.get_rgb_window.setWindowTitle("Converter HSI - RGB")

        self.get_rgb_window_2 = QDialog()
        self.get_rgb_window_2_ui = three_input.Ui_Dialog()
        self.get_rgb_window_2_ui.setupUi(self.get_rgb_window_2)
        self.get_rgb_window_2_ui.retranslateUi(self.get_rgb_window_2, "Deslocamento Hue", "Deslocamento Saturation", "Deslocamento Intensity")
        self.get_rgb_window_2.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.get_rgb_window_2.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "convert.svg"))))
        self.get_rgb_window_2.setWindowTitle("Converter HSI - RGB")

        # Weighted mean
        self.grayscale_weighted_mean_apply_window = QDialog()
        self.grayscale_weighted_mean_apply_window_ui = three_input.Ui_Dialog()
        self.grayscale_weighted_mean_apply_window_ui.setupUi(self.grayscale_weighted_mean_apply_window)
        self.grayscale_weighted_mean_apply_window_ui.retranslateUi(self.grayscale_weighted_mean_apply_window, "Peso do canal R", "Peso do canal G", "Peso do canal B")
        self.grayscale_weighted_mean_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.grayscale_weighted_mean_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "grayscale_weighted_mean.svg"))))
        self.grayscale_weighted_mean_apply_window.setWindowTitle("Escala de Cinza pela média ponderada")

        # Chroma key
        self.chroma_key_window = QDialog()
        self.chroma_key_window_ui = dialog_chroma.Ui_Dialog()
        self.chroma_key_window_ui.setupUi(self.chroma_key_window)
        self.chroma_key_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.chroma_key_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "chroma_key.svg"))))
        self.chroma_key_window.setWindowTitle("Chroma Key")

        # Adjust HSI
        self.adjust_hsi_channels_window = QDialog()
        self.adjust_hsi_channels_window_ui = three_input.Ui_Dialog()
        self.adjust_hsi_channels_window_ui.setupUi(self.adjust_hsi_channels_window)
        self.adjust_hsi_channels_window_ui.retranslateUi(self.adjust_hsi_channels_window, "Deslocamento Hue", "Deslocamento Saturation", "Deslocamento Intensity")
        self.adjust_hsi_channels_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.adjust_hsi_channels_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "grayscale_weighted_mean.svg"))))
        self.adjust_hsi_channels_window.setWindowTitle("Ajustar HSI")

        # Adjust_color_balance
        self.adjust_color_balance_window = QDialog()
        self.adjust_color_balance_window_ui = three_input.Ui_Dialog()
        self.adjust_color_balance_window_ui.setupUi(self.adjust_color_balance_window)
        self.adjust_color_balance_window_ui.retranslateUi(self.adjust_color_balance_window, "Deslocamento CR", "Deslocamento MG", "Deslocamento YB")
        self.adjust_color_balance_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.adjust_color_balance_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "grayscale_weighted_mean.svg"))))
        self.adjust_color_balance_window.setWindowTitle("Aplicar ajuste de cores")

        parent.setCentralWidget(self.central_frame)