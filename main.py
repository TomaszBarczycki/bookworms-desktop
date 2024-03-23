import sys
from PySide6.QtWidgets import QApplication, QStackedWidget
from src.loginpage import LoginPage
from src.startpage import StartPage

if __name__ == '__main__':
    app = QApplication(sys.argv)

    stackedWidget = QStackedWidget()
    stackedWidget.setStyleSheet("background-color: #fcf7ec;")

    startPage = StartPage(stackedWidget)
    loginPage = LoginPage(stackedWidget)

    stackedWidget.addWidget(startPage)
    stackedWidget.addWidget(loginPage)
    stackedWidget.setWindowTitle("Bookworms")

    stackedWidget.show()

    sys.exit(app.exec())
