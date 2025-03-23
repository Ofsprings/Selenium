@echo off
echo Установка Selenium и необходимых библиотек для Windows...

:: Проверка, установлен ли Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python не найден. Пожалуйста, установите Python вручную с https://www.python.org/downloads/
    pause
    exit /b 1
) else (
    echo Python уже установлен.
)

:: Проверка, установлен ли pip
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip не найден. Устанавливаем...
    python -m ensurepip --upgrade
) else (
    echo pip уже установлен.
)

:: Установка Selenium и других библиотек
echo Устанавливаем Selenium, requests и pytest...
python -m pip install selenium requests pytest

:: Установка ChromeDriver (если нужно)
echo Устанавливаем ChromeDriver...
where chromedriver >nul 2>&1
if %errorlevel% neq 0 (
    echo ChromeDriver не найден. Устанавливаем...
    :: Получаем версию Chrome
    for /f "tokens=*" %%a in ('reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version 2^>nul') do (
        for /f "tokens=3" %%b in ("%%a") do (
            set CHROME_VERSION=%%b
        )
    )
    if "%CHROME_VERSION%"=="" (
        echo Не удалось определить версию Chrome. Убедитесь, что Chrome установлен.
        pause
        exit /b 1
    )
    echo Версия Chrome: %CHROME_VERSION%

    :: Получаем версию ChromeDriver
    for /f "tokens=*" %%a in ('curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_%CHROME_VERSION%') do (
        set CHROMEDRIVER_VERSION=%%a
    )
    echo Версия ChromeDriver: %CHROMEDRIVER_VERSION%

    :: Скачиваем и распаковываем ChromeDriver
    curl -o chromedriver_win32.zip https://chromedriver.storage.googleapis.com/%CHROMEDRIVER_VERSION%/chromedriver_win32.zip
    tar -xf chromedriver_win32.zip
    move chromedriver.exe "C:\Windows\System32"
    del chromedriver_win32.zip
) else (
    echo ChromeDriver уже установлен.
)

echo Установка завершена!
pause