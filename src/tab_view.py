from PyQt5.QtWidgets import QTabWidget
from .tab_bar import TabBar


class TabView(QTabWidget):
    def __init__(self, parent):
        super(TabView, self).__init__(parent)
        # Set custom tabbar
        self.setTabBar(TabBar())

    def tab_at(self, pos):
        return self.tabBar().tabAt(pos)
