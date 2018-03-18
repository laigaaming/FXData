@echo off
cls

SETLOCAL ENABLEDELAYEDEXPANSION
SET FXData_PRJ_PATH=E:\Python\PycharmProjects\FXData

for /f "usebackq delims==" %%i in (`cscript %FXData_PRJ_PATH%\datetime_function.vbs`) do set dt=%%i
echo "====================== Process Starts @ %dt%======================"

SET LOG_PATH=FXData_PRJ_PATH\log
SET LOG_FILE=%LOG_PATH%\FX_DATA_Import_%dt%.log

python %FXData_PRJ_PATH%\src\main\fx\fxdataimport.py >> %LOG_FILE%

for /f "usebackq delims==" %%i in (`cscript %FXData_PRJ_PATH%\datetime_function.vbs`) do set dt=%%i
echo "====================== Process Ends @ %dt%======================"
PAUSE

exit 0
