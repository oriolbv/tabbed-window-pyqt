from PyQt5.QtWidgets import QTabBar, QApplication
from PyQt5.QtCore import Qt
from .ghost_window import GhostWindow
from tabbed_window import TabbedWindow


class TabBar(QTabBar):
    def __init__(self, parent):
        super(TabBar, self).__init__(parent)
        self.m_ghost = None

    def mouseMoveEvent(self, QMouseEvent):
        if self.m_ghost:
            self.m_ghost.move_with_offset(QMouseEvent.globalPos())

    def mousePressEvent(self, QMouseEvent):
        # If left button is pressed start tab move event
        if QMouseEvent.button() == Qt.LeftButton & self.tabAt(QMouseEvent.pos()) > -1:
            self.m_ghost = GhostWindow(self, QMouseEvent.pos())
            self.m_ghost.show()

        # Call superclass
        QTabBar.mousePressEvent(QMouseEvent)

    def mouseReleaseEvent(self, QMouseEvent):
        # Call superclass if a button different than the left one was released and return
        if QMouseEvent.button() != Qt.LeftButton:
            QTabBar.mouseReleaseEvent(QMouseEvent)
            return

        # Execute drag code only if far enough
        if self.m_ghost.drag_started(QMouseEvent.globalPos()):
            w = QApplication.widgetAt(QMouseEvent.globalPos())

            # Choose action by the widget under the mouse's coordinates
            if not w:
                if self.count() == 1:
                    # Move the current window into the new position
                    self.window().move(self.m_ghost.pos())
                else:
                    # Creates a new window with the dragged tab
                    self.create_new_window(self.m_ghost)
            else:
                # Move the dragged tab into the window under the cursor
                wnd = w.window()

                if wnd:
                    self.move_to_window(wnd, QMouseEvent.globalPos(), self.m_ghost)

        # Close ghost
        self.m_ghost.close()

    def move_to_window(self, wnd, pos, ghost):
        # Remove view from this window
        view = self.parent()
        index = ghost.index()
        text = self.tabText(index)
        page = view.widget(index)

        view.removeTab(index)

        # Insert tab into the new window at the given cursor's position
        index = wnd.insert_view(pos, page, text)

        # Set it as the current tab and move focus to the new window
        wnd.set_current_view(index)
        # wnd.raise()

    def tab_removed(self, index):
        if self.count() == 0:
            self.window().close()

    def create_new_window(self, ghost):
        # Create the new window with the same size and centered under the cursor
        wnd = TabbedWindow()
        wnd.setGeometry(ghost.geometry())

        # Move widget to the new window
        view = self.parent()
        index = ghost.index()
        tab = view.widget(index)
        text = view.tabText(index)

        view.removeTab(index)
        wnd.add_view(tab, text)

        # Show the new window
        wnd.show()
