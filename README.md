# CG Project Instructions

This document is used to show how to run the source code.

first version: surrounding environment is only the coordinate system

The following technics are included in this project:
1. Texture
   1. skybox
2. Light
3. Multiple ModelViews Handling
4. Animation
5. Keyboard control

## Requirments
Python needs to be installed. The latest version is recommended. The version I tested on my machine is `Python 3.9.7`. More information on how to install Python can be found here (https://www.python.org/)  
The following packages are also needed:
1. PyOpenGL
2. pygame
3. Pillow
4. numpy

`pip` is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes. The following command can be used to check if pip is already available in your machine.
```
python3 -m pip --version
```
If you installed Python from source, with an installer from python.org, or via Homebrew you should already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip separately, see [Installing pip/setuptools/wheel with Linux Package Managers](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/).

After making sure `pip` is available, following can install the packages:
```
pip install PyOpenGL
pip install pygame
pip install Pillow
pip install numpy
```

## How to run the code
Go to the directory of the main file: `skeleton.py`  
Run the following command:
```
python3 skeleton.py
```