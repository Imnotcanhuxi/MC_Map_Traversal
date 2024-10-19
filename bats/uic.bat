for  %%I in (res\*.ui) do pyside6-uic "res/%%~nI.ui" -o "src/Ui_%%~nI.py"
