from PySide6.QtWidgets import QMainWindow, QDialog

from config import IS_FULL_SCREEN
from ui.alert_ui import Ui_Dialog as AlertUI


class AlertWindow(QDialog):
    def __init__(self, message: str, title: str, parent=None,
                 is_ok_button_hide=True, is_cancel_button_hide=True,
                 ok_button_function=lambda: None, cancel_button_function=lambda: None):
        super().__init__(parent)
        if IS_FULL_SCREEN:
            self.showFullScreen()

        self.ui = AlertUI()
        self.ui.setupUi(self)
        self.ui.info_label.setText(message)
        self.setWindowTitle(title)
        self.ok_button_function = ok_button_function
        self.cancel_button_function = cancel_button_function
        self.ui.close_button.setHidden(is_ok_button_hide)
        self.ui.cancelButton.setHidden(is_cancel_button_hide)
        self.ui.close_button.clicked.connect(self.ok_button_action)
        self.ui.cancelButton.clicked.connect(self.cancel_button_action)

    def ok_button_action(self, _=None):
        self.ok_button_function()
        self.close()

    def cancel_button_action(self, _=None):
        self.cancel_button_function()
        self.close()
