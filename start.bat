@echo off
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python yüklü değil. Lütfen Python'u https://www.python.org/ adresinden indirin ve kurun.
    pause
    exit /b 1
)
pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Pip yüklü değil. Python'u yeniden kurarken "Add Python to PATH" ve "pip" seçeneklerini etkinleştirdiğinizden emin olun.
    pause
    exit /b 1
)
echo Gerekli kütüphaneler kontrol ediliyor...
python -c "import PyQt6" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo PyQt6 bulunamadı. Yükleniyor...
    pip install PyQt6
    IF %ERRORLEVEL% NEQ 0 (
        echo PyQt6 yüklenirken bir hata oluştu.
        pause
        exit /b 1
    )
)
echo Tüm gerekli kütüphaneleri yüklediniz.
echo Uygulama başlatılıyor...
echo Set WshShell = CreateObject("WScript.Shell") > temp.vbs
echo WshShell.Run "cmd /c python ""assets\app\app.py""", 0, False >> temp.vbs
cscript temp.vbs
del temp.vbs
exit
