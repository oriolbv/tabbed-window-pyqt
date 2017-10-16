import sys
from PyQt5.QtWidgets import QApplication
from src.tabbed_windows import TabbedWindows

if __name__ == '__main__':
    # Create application
    a = QApplication(sys.argv)

    tabbed_windows = TabbedWindows()

    a.exec()
