import sys
import subprocess
from PyQt6 import QtWidgets, QtGui

bty = "off"
icon_on_path = r'assets\img\bluetooth_on.png'
icon_off_path = r'assets\img\bluetooth_off.png'

def run_bt_script(state):
    try:
        script_path = r'assets\ps1\bt.ps1'
        subprocess.run([
            "powershell", "-ExecutionPolicy", "Bypass", "-File", script_path, "-BluetoothStatus", state
        ], check=True)
    except Exception as e:
        print(f"Hata: {e}")

def toggle_bluetooth():
    global bty
    if bty == "on":
        run_bt_script("Off")
        bty = "off"
        tray_icon.setIcon(QtGui.QIcon(icon_off_path))
    else:
        run_bt_script("On")
        bty = "on"
        tray_icon.setIcon(QtGui.QIcon(icon_on_path))
    update_menu()

def quit_app():
    QtWidgets.QApplication.quit()

def update_menu():
    if bty == "on":
        bluetooth_action.setChecked(True)
    else:
        bluetooth_action.setChecked(False)

app = QtWidgets.QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
tray_icon = QtWidgets.QSystemTrayIcon()
tray_icon.setIcon(QtGui.QIcon(icon_off_path))
tray_icon.setVisible(True)
menu = QtWidgets.QMenu()

bluetooth_action = QtGui.QAction("Bluetooth Aç/Kapat")
bluetooth_action.setCheckable(True)
bluetooth_action.triggered.connect(toggle_bluetooth)
menu.addAction(bluetooth_action)
quit_action = QtGui.QAction("Çıkış")
quit_action.triggered.connect(quit_app)
menu.addAction(quit_action)
tray_icon.setContextMenu(menu)

def on_double_click(reason):
    if reason == QtWidgets.QSystemTrayIcon.ActivationReason.DoubleClick:
        toggle_bluetooth()

tray_icon.activated.connect(on_double_click)

if __name__ == "__main__":
    sys.exit(app.exec())
