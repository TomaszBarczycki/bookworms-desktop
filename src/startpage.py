from PySide6.QtWidgets import QWidget
from views.startpage_ui import Ui_Form as StartPageUi

class StartPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = StartPageUi()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.pushButton.clicked.connect(self.showLoginPage)
        self.ui.pushButton_2.clicked.connect(self.showRegistrationPage)

    def showLoginPage(self):
        self.stacked_widget.setCurrentIndex(1)

    def showRegistrationPage(self):
        self.stacked_widget.setCurrentIndex(2)
