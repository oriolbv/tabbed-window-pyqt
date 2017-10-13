from PyQt5.QtWidgets import QMainWindow
from .tab_view import TabView


class TabbedWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        # Create tab widget
        self.tabs = TabView()
        self.tabs.setDocumentMode(True)

        # Set up main window
        self.setCentralWidget(self.tabs)

    def current_view(self):
        pass

    def set_current_view(self, index):
        self.tabs.setCurrentIndex(index)

    def insert_view(self, pos, page, text):
        # Get tab's index at the given global position
        index = self.tabs.tabAt(self.tabs.mapFromGlobal(pos))

        # Insert new tab
        return self.tabs.insertTab(index, page, text)

    def add_view(self, view, title):
        return self.tabs.addTab(view, title)

    def remove_view(self, index):
        self.tabs.removeTab(index)
