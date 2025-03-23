@echo off
echo Отключение обновлений Google Chrome...

:: Отключение автоматических обновлений через реестр
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Update" /v UpdateDefault /t REG_DWORD /d 0 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Update" /v AutoUpdateCheckPeriodMinutes /t REG_DWORD /d 0 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Update" /v DisableAutoUpdateChecksCheckboxValue /t REG_DWORD /d 1 /f

:: Отключение службы Google Update (gupdate), если она существует
sc query gupdate >nul 2>&1
if %errorlevel% equ 0 (
    sc stop gupdate >nul 2>&1
    sc config gupdate start= disabled >nul 2>&1
    echo Служба Google Update отключена.
) else (
    echo Служба Google Update не найдена.
)

:: Отключение задач планировщика, если они существуют
schtasks /Query /TN "GoogleUpdateTaskMachineCore" >nul 2>&1
if %errorlevel% equ 0 (
    schtasks /Change /TN "GoogleUpdateTaskMachineCore" /DISABLE >nul 2>&1
    echo Задача GoogleUpdateTaskMachineCore отключена.
) else (
    echo Задача GoogleUpdateTaskMachineCore не найдена.
)

schtasks /Query /TN "GoogleUpdateTaskMachineUA" >nul 2>&1
if %errorlevel% equ 0 (
    schtasks /Change /TN "GoogleUpdateTaskMachineUA" /DISABLE >nul 2>&1
    echo Задача GoogleUpdateTaskMachineUA отключена.
) else (
    echo Задача GoogleUpdateTaskMachineUA не найдена.
)

echo Обновления Google Chrome отключены.
pause