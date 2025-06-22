@echo off
echo === BAT FILE IS RUNNING ===
echo Current directory is: %CD%
echo Looking for folder: "dp0MindMapAI"

if exist "MindMapAI" (
    echo ✅ Found MindMapAI
) else (
    echo ❌ MindMapAI folder not found in %CD%
    echo Please move this file to the same directory that contains MindMapAI
    goto end
)

echo Checking Python installation...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python not found or not added to PATH
    goto end
)

echo All checks passed.
pause

:end
echo Press any key to exit...
pause >nul
