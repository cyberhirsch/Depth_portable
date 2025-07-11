@echo off
echo ==========================================================
echo  Setting up the Portable Depth Map Environment
echo ==========================================================
echo.

echo [+] Enabling pip in portable Python...
powershell -Command "((Get-Content -Path '.\python-3.10.11-embed-amd64\python310._pth' -Raw) -replace '#import site', 'import site') | Set-Content -Path '.\python-3.10.11-embed-amd64\python310._pth'"
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
.\python-3.10.11-embed-amd64\python.exe get-pip.py
del get-pip.py
echo.

echo [+] Installing all required libraries...
.\python-3.10.11-embed-amd64\python.exe -m pip install -r .\stable-diffusion-webui-depthmap-script-main\requirements.txt
echo.

echo ==========================================================
echo  Setup complete! You can now run 'Run_Depth_Portable.bat'.
echo ==========================================================
pause