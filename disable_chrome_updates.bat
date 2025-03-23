@echo off
echo Полное удаление Google Update и отключение обновлений Chrome...

:: Остановка и удаление служб Google Update
sc stop gupdate >nul 2>&1
sc delete gupdate >nul 2>&1
sc stop gupdatem >nul 2>&1
sc delete gupdatem >nul 2>&1

:: Удаление папки Google Update
if exist "%ProgramFiles(x86)%\Google\Update" (
    echo Удаление папки Google Update...
    rmdir /s /q "%ProgramFiles(x86)%\Google\Update"
)

if exist "%ProgramFiles%\Google\Update" (
    echo Удаление папки Google Update...
    rmdir /s /q "%ProgramFiles%\Google\Update"
)

:: Удаление задач из планировщика задач
schtasks /Delete /TN "\GoogleUpdate\GoogleUpdateTaskMachineCore" /F >nul 2>&1
schtasks /Delete /TN "\GoogleUpdate\GoogleUpdateTaskMachineUA" /F >nul 2>&1

echo Google Update полностью удален. Обновления Chrome отключены.
pause