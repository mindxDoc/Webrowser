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
        user_input = self.searchBar.text()
        url = QtCore.QUrl.fromUserInput(user_input)
        url.setScheme("https")
        print(url)
        # Use regular expression to check if the URL is a valid domain address
        import re
        pattern = r"^(?:http|ftp)s?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}$"
        if re.match(pattern, url.toString()):
            self.webEngineView.setUrl(url)
        else:
            url = "www.google.com/search?q=" + user_input
            self.webEngineView.setUrl(QtCore.QUrl.fromUserInput(url))
    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Back, checked=True)
    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Reload, checked=True)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Browser()
    window.show()
    app.exec()