for uiname in res/*.ui
do
 pyside6-uic "res/$uiname.ui" -o "src/Ui_$uiname.py"
done
