from PyQt6 import QtWidgets as qtw, QtCore
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6 import uic
import sys

class Browser(qtw.QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()
        uic.loadUi("main.ui", self)

        # setup web engine and add view into content widget (have layout name is verticalLayout_3)
        self.webEngineView = QWebEngineView()
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_3.addWidget(self.webEngineView)

        #action enter to search, back and reload
        self.searchBar.returnPressed.connect(self.load)
        self.back.clicked.connect(self.backward)
        self.reloading.clicked.connect(self.reload)

    # loading url
    def load(self):
        url = self.searchBar.text()
        if not url.startswith("http"):
            url = "https://" + url
            self.webEngineView.load(QtCore.QUrl(url))
    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Back, checked=True)
    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Reload, checked=True)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Browser()
    window.show()
    app.exec()