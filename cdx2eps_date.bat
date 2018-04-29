@echo off

:start

cd C:\Users\Lois\Documents\Thesis\Tex\figs

set /p mydate="Convert files more recent than (DD/MM/YYYY): " || set mydate=%date%
echo.

REM set mydate=10/05/2017

set fpath=%cd%

echo Date is %mydate%
echo Path is %fpath%

forfiles /M "*.cdx" /d +%mydate% /c "cmd /q /c C:\Users\Lois\Documents\Thesis\cdx2eps.bat @fname @ext @path"

echo.
set choice=
set /p choice="Do you want to restart? Press 'y' and enter for yes: "
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='y' goto start

REM cmd /k