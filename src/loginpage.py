from PySide6.QtWidgets import QWidget, QMessageBox
import requests
from views.loginpage_ui import Ui_Form as LoginPageUi
from views.registrationpage_ui import Ui_Form as RegistrationPageUi

class LoginPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = LoginPageUi()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.label_5.mousePressEvent = self.open_registration_window

    def open_registration_window(self, event):
        self.registration_window = RegistrationPage(self.stacked_widget)
        self.stacked_widget.addWidget(self.registration_window)
        self.stacked_widget.setCurrentWidget(self.registration_window)
        
    def login(self):
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if not (email and password):
            QMessageBox.warning(self, "Error", "All fields are required!")
            return

        data = {
            "email": email,
            "password": password
        }

        response = requests.post("https://bookworms.fly.dev/api/login", json=data)

        if response.status_code == 200:
            QMessageBox.information(self, "Success", "Logged in successfully!")
        else:
            QMessageBox.warning(self, "Error", "Invalid email or password")

class RegistrationPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = RegistrationPageUi()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.pushButton.clicked.connect(self.register)
        self.ui.label_5.mousePressEvent = self.open_login_window
    
    def open_login_window(self, event):
        self.login_window = LoginPage(self.stacked_widget)
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.setCurrentWidget(self.login_window)

    def register(self):
        username = self.ui.lineEdit.text()
        email = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit_3.text()
        confirm_password = self.ui.lineEdit_4.text()
   
        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match!")
            return
        
        if not (username and email and password and confirm_password):
            QMessageBox.warning(self, "Error", "All fields are required!")
            return

        data = {
            "name": username,
            "email": email,
            "password": password,
            "password_confirmation": confirm_password
        }

        response = requests.post("https://bookworms.fly.dev/api/register", json=data)

        if response.status_code == 200:
            QMessageBox.information(self, "Success", "Registered successfully!")
        else:
            error_message = response.json().get('message', 'Something went wrong')
            QMessageBox.warning(self, "Error", error_message)
