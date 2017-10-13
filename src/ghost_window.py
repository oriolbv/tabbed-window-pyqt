from PyQt5.QtWidgets import QWidget


class GhostWindow(QWidget):
    def __init__(self, parent):
        super(GhostWindow, self).__init__(parent)
        self.__m_offset = None
        self.__m_index = None
        self.__m_origin_pos = None