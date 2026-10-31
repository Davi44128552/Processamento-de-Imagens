from qt_core import *

# Creating a class to draw the graph in the piecewise algorithm
class Canvas(QWidget):

    # Class variables
    margin = 20
    click_tolerance = 8

    # Constructor
    def __init__(self):

        super().__init__()
        self.points = [(0, 0), (255, 255)]
        self.selected = None
        dimension = 256 + 2 * self.margin
        self.setFixedSize(dimension, dimension)

    def widget(self, coordinate_rs):
        return QPoint(self.margin + int(coordinate_rs[0]), self.margin + 255 - int(coordinate_rs[1]))

    def curve(self, position):
        return (max(0, min(255, position.x() - self.margin)), max(0, min(255, 255 - (position.y() - self.margin))))

    def find_point(self, position):

        for k, (r, s) in enumerate(self.points):
            p = self.widget((r, s))
            if (abs(p.x() - position.x()) <= self.click_tolerance and abs(p.y() - position.y()) <= self.click_tolerance):
                return k
        return None

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 255))
        painter.setPen(QPen(QColor(200, 200, 200), 2))
        painter.drawRect(self.margin, self.margin, 255, 255)
        painter.drawLine(self.widget((0, 0)), self.widget((255, 255)))
        painter.setPen(QPen(QColor(30, 100, 220), 2))

        for k in range(0, len(self.points) - 1):
            painter.drawLine(self.widget(self.points[k]), self.widget(self.points[k + 1]))

        painter.setPen(QPen(QColor(0, 0, 0), 1))
        painter.setBrush(QColor(220, 50, 50))

        for coord in self.points:
            painter.drawEllipse(self.widget(coord), 5, 5)

        painter.end()

    def mousePressEvent(self, event):
        point = self.find_point(event.pos())

        if (event.button() == Qt.MouseButton.LeftButton):

            if (point is None):
                coords = self.curve(event.pos())

                for p in self.points:
                    if (p[0] == coords[0]):
                        return
                self.points.append(coords)
                self.points = sorted(self.points, key = lambda x: x[0])
                point = self.points.index(coords)

            self.selected = point

        elif (event.button() == Qt.MouseButton.RightButton):

            if ((point is not None) and (0 < point < (len(self.points) - 1))):
                self.points.pop(point)

        self.update()

    def mouseMoveEvent(self, event):

        if (self.selected is None):
            return

        point = self.selected
        coords = self.curve(event.pos())

        if (point == 0):
            coords = (0, coords[1])
        elif (point == (len(self.points) - 1)):
            coords = (255, coords[1])
        else:
            new_r_value = max(self.points[point - 1][0] + 1, min(self.points[point + 1][0] - 1, coords[0]))
            coords = (new_r_value, coords[1])

        self.points[point] = coords
        self.update()

    def mouseReleaseEvent(self, event):
        self.selected = None
    