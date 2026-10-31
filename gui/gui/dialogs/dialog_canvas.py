from qt_core import *
from .dialog_piecewise_draw import Canvas

class DialogCanvas(QDialog):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Transformação Linear definida por Partes")
        self.canvas = Canvas()

        axis_label = QLabel("Horizontal: intensidade de entrada (r) | Vertical: intensidade de saída (s)")
        hint = QLabel("Botão esquerdo do mouse: adiciona ponto | Botão direito do mouse: remove ponto")

        # Buttons
        reset_button = QPushButton("Resetar")
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

        # Buttons' actions
        reset_button.clicked.connect(self.reset)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        # Dialog layout
        dialog_layout = QVBoxLayout (self)
        dialog_layout.addWidget(self.canvas)
        dialog_layout.addWidget(axis_label)
        dialog_layout.addWidget(hint)
        dialog_layout.addWidget(reset_button)
        dialog_layout.addWidget(buttons)

    def reset(self):
        self.canvas.points = [(0, 0), (255, 255)]
        self.canvas.update()

    def get_points(self):

        points_list = list(self.canvas.points)
        return points_list
