from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPalette, QBrush
from PyQt5.QtCore import Qt


class GhostWindow(QWidget):
    def __init__(self, parent, pos):
        super(GhostWindow, self).__init__(parent)
        self.__parent = parent
        wnd = self.__parent.window()
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(wnd.grab()))

        self.setPalette(palette)
        self.setGeometry(wnd.geometry())
        self.setWindowOpacity(0.5)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.__m_offset = self.__parent.mapToGlobal(pos) - wnd.pos()
        self.__m_index = self.__parent.tabAt(pos)
        self.__m_origin_pos = self.__parent.mapToGlobal(pos)

    def move_with_offset(self, pos):
        self.move(pos - self.__m_offset)

    def drag_started(self, pos):
        return (pos - self.__m_origin_pos).manhattanLength() >= QApplication.startDragDistance()

    def offset(self):
        return self.__m_offset

    def index(self):
        return self.__m_index

