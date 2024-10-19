[app]
title = MC_Map_Treversal
project_dir = ./
input_file = src/PySide_main.py
exec_directory = dist/
project_file =
icon = res/favicon.ico

[python]
python_path = python
packages = Nuitka
android_packages = buildozer==1.5.0,cython==0.29.33

[qt]
qml_files =
excluded_qml_plugins =
modules = Widgets,Gui,Core

[android]
wheel_pyside =
wheel_shiboken =
plugins =

[nuitka]
macos.permissions =
mode = onefile
extra_args = --quiet --noinclude-qt-translations

[buildozer]
mode = debug
recipe_dir =
jars_dir =
ndk_path =
sdk_path =
local_libs =
arch =
