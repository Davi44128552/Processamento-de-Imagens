# Importing the necessary libraries
import os
from qt_core import *

# Creating the class Pushbutton
class PyPushButton(QPushButton):
    def __init__(self, text = "", height = 40, minimuim_width = 50, text_padding = 55, text_color = "#c3ccdf", icon_path = "", icon_color = "#c3ccdf", button_color = "#44475a", button_hover = "#4f5368", button_pressed = "#282a36", is_active = False):
        super().__init__()

        # Setting the parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)
        self.minimum_width = minimuim_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.button_color = button_color
        self.button_hover = button_hover
        self.button_pressed = button_pressed
        self.is_active = is_active

        # Setting style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            button_hover = self.button_hover,
            button_color = self.button_color,
            button_pressed = self.button_pressed,
            is_active = self.is_active
        )

    # Function to change selected buttons
    def set_active(self, is_active_menu):
        self.set_style(
            text_padding = self.text_padding,
                text_color = self.text_color,
                button_hover = self.button_hover,
                button_color = self.button_color,
                button_pressed = self.button_pressed,
                is_active = is_active_menu
        )

    # Method to set style
    def set_style(self, text_padding = 55, text_color = "#c3ccdf", button_color = "#44475a", button_hover = "#4f5368", button_pressed = "#282a36", is_active = False):

        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {button_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}

        QPushButton:hover {{
            background-color: {button_hover}
        }}

        QPushButton:pressed {{
            background-color: {button_pressed}
        }} 
        """

        active_style = f"""

        QPushButton {{
            background-color: {button_hover};
            border-right: 5px solid #282a36;
        }}

        """

        if (not is_active):
            self.setStyleSheet(style)
        else: 
            self.setStyleSheet(style + active_style)

    # Method to paint the buttons
    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)

        # Creating a painter
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # Creating a container for the items
        container = QRect(0, 0, self.minimum_width, self.height())

        self.draw_icon(painter, self.icon_path, container, self.icon_color)

        # Ending the painter
        painter.end()

    # Drawning icon
    def draw_icon(self, painter, image, rect, color):

        # Format path
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Draw icon
        icon = QPixmap(icon_path)
        painter_button = QPainter(icon)
        painter_button.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter_button.fillRect(icon.rect(), color)
        painter_button.end()
        painter.drawPixmap(
            ((rect.width() - icon.width()) / 2),
            ((rect.height() - icon.height()) / 2),
            icon
        )


