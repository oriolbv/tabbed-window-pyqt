from PyQt5.QtWidgets import QMainWindow
from .tab_view import TabView


class TabbedWindow(QMainWindow):
    def __init__(self, parent):
        super(QMainWindow, self).__init__(parent)
        self.__parent = parent
        self.__is_main_window = False

        # Create tab widget
        self.tabs = TabView(self)
        self.tabs.setDocumentMode(True)

        # Set up main window
        self.setCentralWidget(self.tabs)

    def current_view(self):
        pass

    def set_current_view(self, index):
        self.tabs.setCurrentIndex(index)

    def insert_view(self, pos, page, text):
        # Get tab's index at the given global position
        index = self.tabs.tab_at(self.tabs.mapFromGlobal(pos))

        # Insert new tab
        return self.tabs.insertTab(index, page, text)

    def add_view(self, view, title):
        return self.tabs.addTab(view, title)

    def remove_view(self, index):
        self.tabs.removeTab(index)

    def parent(self):
        return self.__parent

    def closeEvent(self, event):
        if not self.__is_main_window:
            self.closeEvent(event)
        else:
            print("not close")

    # Properties

    @property
    def is_main_window(self):
        return self.__is_main_window

    @is_main_window.setter
    def is_main_window(self, new_value):
        self.__is_main_window = new_value
