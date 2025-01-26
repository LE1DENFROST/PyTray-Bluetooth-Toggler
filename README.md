# Bluetooth Toggle Tray Application

> A simple, elegant application to toggle Bluetooth on or off directly from your system tray. Built with Python and PyQt6, this project offers a lightweight and user-friendly solution to manage your Bluetooth connectivity with ease. 🚀

---

## 🛠 Features

- **System Tray Integration**: Control Bluetooth with a simple click.
- **Quick Toggle**: Double-click the tray icon to enable or disable Bluetooth instantly.
- **Custom Icons**: Visual feedback with on/off Bluetooth status icons.
- **Error Handling**: Built-in checks to handle potential script execution errors gracefully.
- **Batch Startup Script**: Ensures required dependencies are installed and launches the app effortlessly.

---

## 📂 Project Structure

```
project-root                          
├── start.bat            # Batch script to install dependencies and start the app
├── assets               # Resource folder
│   ├── img
│   │   ├── bluetooth_on.png
│   │   └── bluetooth_off.png
│   ├── ps1
│   │   └── bt.ps1       # PowerShell script to toggle Bluetooth state
│   │── app
│   │   └── app.py       # Main application script

```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.7+**
- **Pip** (Python package installer)
- **Windows OS** (Required for PowerShell script compatibility)

---

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/LE1DENFROST/bluetooth-toggle-app.git
   cd bluetooth-toggle-app
   ```

2. **Run the startup script**:

   Simply execute the `start.bat` file:

   ```
   start.bat
   ```

   This script will:
   - Check for Python and pip installation.
   - Install the required `PyQt6` library.
   - Launch the application.

---

## 💻 Usage

- **Tray Icon**:
  - Right-click the tray icon to access options like "Bluetooth Aç/Kapat" (Toggle Bluetooth) and "Çıkış" (Exit).
  - Double-click the tray icon to toggle Bluetooth.

- **PowerShell Script**: The `bt.ps1` script ensures that Bluetooth is toggled on/off programmatically using Windows APIs.

---

## ⚙️ Customization

### Changing Icons

To replace the default Bluetooth icons:
1. Navigate to `assets/img/`.
2. Replace `bluetooth_on.png` and `bluetooth_off.png` with your custom icons.

### Adjusting Scripts

- The PowerShell script `bt.ps1` can be modified to extend functionality, such as additional Bluetooth device management.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- [PyQt6 Documentation](https://riverbankcomputing.com/software/pyqt/intro) for their fantastic GUI library.
- Microsoft PowerShell for providing seamless Bluetooth control.

---

## 📝 Author

Developed by [LE1DENFROST](https://github.com/LE1DENFROST).

Feel free to reach out for feedback, suggestions, or contributions! 🌟
