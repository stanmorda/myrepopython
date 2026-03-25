import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, QTime, Qt, QPoint
from PyQt6.QtGui import QPainter, QColor, QPolygon

class AnalogClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Стрелочные часы")
        self.resize(300, 300)
        
        # Таймер для перерисовки каждую секунду
        timer = QTimer(self)
        timer.timeout.connect(self.update) # update() вызывает paintEvent
        timer.start(1000)

    def paintEvent(self, event):
        # Координаты стрелок (полигоны)
        hour_hand = QPolygon([QPoint(7, 8), QPoint(-7, 8), QPoint(0, -40)])
        minute_hand = QPolygon([QPoint(7, 8), QPoint(-7, 8), QPoint(0, -70)])
        second_hand = QPolygon([QPoint(1, 8), QPoint(-1, 8), QPoint(0, -90)])

        hour_color = QColor(127, 0, 127)
        minute_color = QColor(0, 127, 127, 191)
        second_color = QColor(255, 0, 0)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Переносим центр координат в середину окна
        painter.translate(self.width() // 2, self.height() // 2)
        
        # Масштабируем, чтобы часы вписывались в размер окна
        side = min(self.width(), self.height())
        painter.scale(side / 200.0, side / 200.0)

        time = QTime.currentTime()

        # Рисуем часовую стрелку
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(hour_color)
        painter.save()
        painter.rotate(30.0 * (time.hour() + time.minute() / 60.0))
        painter.drawConvexPolygon(hour_hand)
        painter.restore()

        # Рисуем минутную стрелку
        painter.setBrush(minute_color)
        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(minute_hand)
        painter.restore()

        # Рисуем секундную стрелку
        painter.setBrush(second_color)
        painter.save()
        painter.rotate(6.0 * time.second())
        painter.drawConvexPolygon(second_hand)
        painter.restore()

        # Рисуем деления циферблата
        painter.setPen(hour_color)
        for i in range(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = AnalogClock()
    clock.show()
    sys.exit(app.exec())
