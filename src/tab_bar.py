from PyQt5.QtWidgets import QTabBar, QApplication
from PyQt5.QtCore import Qt
from .ghost_window import GhostWindow



class TabBar(QTabBar):
    def __init__(self, parent):
        super(TabBar, self).__init__(parent)
        self.m_ghost = None

    def mouseMoveEvent(self, QMouseEvent):
        if self.m_ghost:
            self.m_ghost.move_with_offset(QMouseEvent.globalPos())

    def mousePressEvent(self, QMouseEvent):
        # If left button is pressed start tab move event
        print(QMouseEvent.button())
        print(QMouseEvent.pos())
        print(QMouseEvent.button() == Qt.LeftButton)
        print(self.tabAt(QMouseEvent.pos()) > -1)

        # if QMouseEvent.button() == Qt.LeftButton & self.tabAt(QMouseEvent.pos()) > -1:
        self.m_ghost = GhostWindow(self, QMouseEvent.pos())
        self.m_ghost.show()

        # Call superclass
        QTabBar.mousePressEvent(self, QMouseEvent)

    def mouseReleaseEvent(self, QMouseEvent):
        # Call superclass if a button different than the left one was released and return
        if QMouseEvent.button() != Qt.LeftButton:
            QTabBar.mouseReleaseEvent(self, QMouseEvent)
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
                    self.parent().parent().parent().create_new_window(self.m_ghost, self.parent())
            else:
                # Move the dragged tab into the window under the cursor
                wnd = w.window()
                wnd.closeEvent(self)

                if wnd:
                    self.parent().parent().parent().move_to_window(wnd, QMouseEvent.globalPos(), self.m_ghost, self.parent(), self)



        # Close ghost
        self.m_ghost.close()

    def tab_removed(self, index):
        if self.count() == 0:
            self.window().close()

