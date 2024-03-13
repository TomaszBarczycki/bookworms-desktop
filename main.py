import sys
from PySide6.QtWidgets import QApplication, QWidget
from startpage_ui import Ui_Form

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form() 
    ui.setupUi(window) 
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()