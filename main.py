from PySide6.QtWidgets import QApplication, QLabel

import sys

app = QApplication(sys.argv)

label = QLabel('Welcome to Bookworms!')

label.show()

app.exec()
