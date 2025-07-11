@echo off
echo Preparing Portable Environment...

:: Get the directory where this batch file is located
set "ROOT_DIR=%~dp0"

:: Define the full paths to the python executable and the script directory
set "PYTHON_EXE=%ROOT_DIR%python-3.10.11-embed-amd64\python.exe"
set "SOURCE_DIR=%ROOT_DIR%stable-diffusion-webui-depthmap-script-main"

::
:: THIS IS THE MOST IMPORTANT STEP
:: We must change to the source directory so Python can find the 'src' module.
:: The sys.path.insert(0, SCRIPT_DIR) in the python script does the rest.
::
cd /d "%SOURCE_DIR%"

echo Launching Portable Depth Map UI from %cd%
"%PYTHON_EXE%" gui.py %*

echo.
echo UI has been closed.
pause