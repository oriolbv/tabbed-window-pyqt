from PyQt5.QtWidgets import QMainWindow, QAction, QWidget
from src.tabbed_window import TabbedWindow


class TabbedWindows(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.__tabbed_windows = []

        # Create tabbed views
        red = QMainWindow()
        green = QMainWindow()
        blue = QMainWindow()

        w = TabbedWindow(self)
        w.is_main_window = True

        red.setStyleSheet("QMainWindow { background-color: red; }")
        blue.setStyleSheet("QMainWindow { background-color: blue; }")
        green.setStyleSheet("QMainWindow { background-color: green; }")

        w.add_view(red, "Red View")
        w.add_view(blue, "Blue View")
        w.add_view(green, "Green View")

        # Added test toolbar
        tb = red.addToolBar("toolbar")
        tb.addAction("RED")

        # Add test menubar
        ma = QAction("Test", green)
        m = green.menuBar().addMenu("File")
        m.addAction(ma)

        self.add_tabbed_window(w)

        # Set size and show
        w.resize(400, 400)
        w.show()

    def add_tabbed_window(self, tabbed_window):
        self.__tabbed_windows.append(tabbed_window)

    def move_to_window(self, wnd, pos, ghost, _view, _tab_bar):
        # Remove view from this window
        view = _view
        index = ghost.index()
        text = _tab_bar.tabText(index)
        page = view.widget(index)

        view.removeTab(index)

        # Insert tab into the new window at the given cursor's position
        index = wnd.insert_view(pos, page, text)

        # Set it as the current tab and move focus to the new window
        wnd.set_current_view(index)
        wnd.raise_()


    def create_new_window(self, ghost, _view):
        # Create the new window with the same size and centered under the cursor
        wnd = TabbedWindow(self)
        wnd.is_main_window = False
        wnd.setGeometry(ghost.geometry())

        # Move widget to the new window
        view = _view
        index = ghost.index()
        tab = view.widget(index)
        text = view.tabText(index)

        view.removeTab(index)
        wnd.add_view(tab, text)

        self.__tabbed_windows.append(wnd)

        # Show the new window
        wnd.show()
