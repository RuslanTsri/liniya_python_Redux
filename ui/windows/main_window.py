import time
import threading
from utils.logger import logger
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow

from config import IS_FULL_SCREEN, IS_FAKE_CHANGE_DETECTORS, UNSELECTED_BUTTON_STYLE_UI, SELECTED_BUTTON_STYLE_UI
from hardware.detectors import detector
from ui.main_ui import Ui_MainWindow as MainUI
from core.settings import config
from ui.windows.alert_window import AlertWindow

class MainWindow(QMainWindow):
    # ТЕПЕР ЛОГІКА ПЕРЕДАЄТЬСЯ У ВІКНО ПРИ ЗАПУСКУ
    def __init__(self, winding_process, parent=None):
        super().__init__(parent)
        self.winding_process = winding_process  # Зберігаємо мізки

        self.alert_window = None
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.show()
        if IS_FULL_SCREEN:
            self.showFullScreen()

        if not IS_FAKE_CHANGE_DETECTORS:
            self.ui.left_detector_button.setHidden(True)
            self.ui.right_detector_button.setHidden(True)

        self.pressed_change_value_button = None
        self.value_to_change = None
        self.update_ui_timer = QTimer()
        self.update_ui_timer.timeout.connect(self._update_ui)
        self.update_ui_timer.start(500)

        threading.Thread(target=self.winding_process.park_carriege, daemon=True).start()

        self._setup_callbacks()
        self._setup_default_label_value()

    def button_10_clicked(self):
        self._unselect_value_buttons()
        self.ui.button_10.setStyleSheet(SELECTED_BUTTON_STYLE_UI)
        self.value_to_change = 10

    def button_1_clicked(self):
        self._unselect_value_buttons()
        self.ui.button_1.setStyleSheet(SELECTED_BUTTON_STYLE_UI)
        self.value_to_change = 1

    def button_01_clicked(self):
        self._unselect_value_buttons()
        self.ui.button_01.setStyleSheet(SELECTED_BUTTON_STYLE_UI)
        self.value_to_change = 0.1

    def button_001_clicked(self):
        self._unselect_value_buttons()
        self.ui.button_001.setStyleSheet(SELECTED_BUTTON_STYLE_UI)
        self.value_to_change = 0.01

    def len_button_clicked(self):
        self._unselect_value_type_buttons()
        self.ui.len_button.setStyleSheet(SELECTED_BUTTON_STYLE_UI)
        self.pressed_change_value_button = 'len'

    def diameter_button_clicked(self):
        self._unselect_value_type_buttons()
        self.ui.diametr_button.setStyleSheet(SELECTED_BUTTON_STYLE_UI)
        self.pressed_change_value_button = 'diameter'

    def width_button_clicked(self):
        self._unselect_value_type_buttons()
        self.ui.width_button.setStyleSheet(SELECTED_BUTTON_STYLE_UI)
        self.pressed_change_value_button = 'width'

    def user_speed_s2_button_clicked(self):
        self._unselect_value_type_buttons()
        self.ui.user_speed_s2_button.setStyleSheet(SELECTED_BUTTON_STYLE_UI)
        self.pressed_change_value_button = 'user_speed_s2'

    def parking_margin_button_clicked(self):
        self._unselect_value_type_buttons()
        self.ui.parking_margin_button.setStyleSheet(SELECTED_BUTTON_STYLE_UI)
        self.pressed_change_value_button = 'parking_margin'

    def add_value(self):
        if not self.value_to_change:
            self.show_alert()
            return
        self.modify_value(self.value_to_change)

    def minus_value(self):
        if not self.value_to_change:
            self.show_alert()
            return
        self.modify_value(-self.value_to_change)

    def modify_value(self, delta):
        if self.pressed_change_value_button == 'len':
            self.add_meters(delta)
        elif self.pressed_change_value_button == 'diameter':
            self.add_diameter(delta)
        elif self.pressed_change_value_button == 'width':
            self.add_width(delta)
        elif self.pressed_change_value_button == 'user_speed_s2':
            self.add_user_speed_s2(delta)
        elif self.pressed_change_value_button == 'parking_margin':
            self.add_parking_margin(delta)
        else:
            self.show_alert()

    def show_alert(self):
        self.alert_window = AlertWindow('Оберіть параметр', 'Помилка', parent=self,
                                        is_ok_button_hide=False, is_cancel_button_hide=True)
        self.alert_window.exec()

    def add_meters(self, meters):
        config.filament_meters += meters
        if config.filament_meters < 0: config.filament_meters = 0
        self.ui.len_button.setText(f'{round(config.filament_meters, 2)}')

    def add_parking_margin(self, width):
        config.parking_margin += width
        self.ui.parking_margin_button.setText(f'{round(config.parking_margin, 2)}')

    def add_diameter(self, diameter):
        config.filament_thickness += diameter
        if config.filament_thickness < 0.01: config.filament_thickness = 0.01
        self.ui.diametr_button.setText(f'{round(config.filament_thickness, 3)}')
        self.winding_process.set_filament_thickness(config.filament_thickness)

    def add_width(self, width):
        config.spool_width += width
        if config.spool_width < 1: config.spool_width = 1
        self.ui.width_button.setText(f'{round(config.spool_width, 2)}')
        self.winding_process.set_spool_width(config.spool_width)

    def add_user_speed_s2(self, s):
        config.user_spool_rpm += s
        if config.user_spool_rpm < 0: config.user_spool_rpm = 0
        self.ui.user_speed_s2_button.setText(f'{int(config.user_spool_rpm)}')
        self.winding_process.set_spool_rpm(config.user_spool_rpm)

    def _update_ui(self):
        try:
            self.ui.plastic_len_finished_label.setText(f'{self.winding_process.get_meters()} M')
        except:
            pass

    def _unselect_value_buttons(self):
        self.ui.button_10.setStyleSheet(UNSELECTED_BUTTON_STYLE_UI)
        self.ui.button_1.setStyleSheet(UNSELECTED_BUTTON_STYLE_UI)
        self.ui.button_01.setStyleSheet(UNSELECTED_BUTTON_STYLE_UI)
        self.ui.button_001.setStyleSheet(UNSELECTED_BUTTON_STYLE_UI)

    def _unselect_value_type_buttons(self):
        self.ui.len_button.setStyleSheet(UNSELECTED_BUTTON_STYLE_UI)
        self.ui.diametr_button.setStyleSheet(UNSELECTED_BUTTON_STYLE_UI)
        self.ui.width_button.setStyleSheet(UNSELECTED_BUTTON_STYLE_UI)
        self.ui.user_speed_s2_button.setStyleSheet(UNSELECTED_BUTTON_STYLE_UI)
        self.ui.parking_margin_button.setStyleSheet(UNSELECTED_BUTTON_STYLE_UI)

    def _setup_callbacks(self):
        self.ui.park_button.clicked.connect(
            lambda: threading.Thread(target=self.winding_process.park_carriege, daemon=True).start())
        self.ui.add_button.clicked.connect(self.add_value)
        self.ui.minus_button.clicked.connect(self.minus_value)
        self.ui.len_button.clicked.connect(self.len_button_clicked)
        self.ui.diametr_button.clicked.connect(self.diameter_button_clicked)
        self.ui.user_speed_s2_button.clicked.connect(self.user_speed_s2_button_clicked)
        self.ui.width_button.clicked.connect(self.width_button_clicked)
        self.ui.parking_margin_button.clicked.connect(self.parking_margin_button_clicked)
        self.ui.button_10.clicked.connect(self.button_10_clicked)
        self.ui.button_1.clicked.connect(self.button_1_clicked)
        self.ui.button_01.clicked.connect(self.button_01_clicked)
        self.ui.button_001.clicked.connect(self.button_001_clicked)
        self.ui.start_button.clicked.connect(self.winding_process.start_filament_winding)
        self.ui.stop_button.clicked.connect(self.winding_process.stop_filament_winding)

    def _setup_default_label_value(self):
        self.ui.len_button.setText(f'{config.filament_meters}')
        self.ui.diametr_button.setText(f'{config.filament_thickness}')
        self.ui.width_button.setText(f'{config.spool_width}')
        self.ui.user_speed_s2_button.setText(f'{config.user_spool_rpm}')
        self.ui.parking_margin_button.setText(f'{config.parking_margin}')