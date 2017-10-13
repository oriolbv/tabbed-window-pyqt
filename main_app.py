from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QMenu
from src.tabbed_window import TabbedWindow

if __name__ == '__main__':
    # Create application
    a = QApplication()

    # Create tabbed views
    red = QMainWindow()
    green = QMainWindow()
    blue = QMainWindow()

    # w = TabbedWindow()

    red.setStyleSheet("QMainWindow { background-color: red; }")
    blue.setStyleSheet("QMainWindow { background-color: blue; }")
    green.setStyleSheet("QMainWindow { background-color: green; }")


