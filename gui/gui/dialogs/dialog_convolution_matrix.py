from qt_core import *
import numpy as np

class ConvolutionMatrixDialog(QDialog):
    def __init__(self, n, parent = None):
        QDialog.__init__(self, parent)
        self.setWindowTitle(f"Matriz de Convolução {n}x{n}")
        self.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.n = n
        self.line_edits = []

        layout = QVBoxLayout(self)
        grid_layout = QGridLayout()

        for i in range(0, n):
            rows = []
            for j in range(0, n):
                le = QLineEdit("")
                le.setFixedSize(40, 40)
                le.setAlignment(Qt.AlignmentFlag.AlignCenter)
                le.setStyleSheet("background-color: #282a36; border: 1px solid #6272a4;")

                grid_layout.addWidget(le, i, j)
                rows.append(le)
            self.line_edits.append(rows)

        layout.addLayout(grid_layout)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        layout.addWidget(self.buttonBox)

    def get_matrix(self):
        kernel = np.zeros((self.n, self.n))
        for i in range(0, self.n):
            for j in range(0, self.n):
                value = self.line_edits[i][j].text()
                try:
                    kernel[i, j] = float(value)
                except ValueError:
                    print("Valor invalido")
        return kernel