# projectMLinCV
Project "Machine learning in computer vision"

# Demo projects

## YOLOv5 with TensorFlow Lite in C++
https://github.com/iwatake2222/play_with_tflite/tree/master/pj_tflite_det_yolov5


Tested on Windows 10, in PyCharm

# projectMLinCV
using yolov5

Test image inference and video inference

## Prerequisites

 - Needs Python to run, tested with Python 3.9
 - Needs pip to run pip install commands, to check if you have pip run `py -m pip --version`
 - If you installed Python from source, with an installer from python.org, or via Homebrew you should already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip separately, see [installing pip/setuptools/wheel with Linux Package Managers](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/)
 - Needs poetry installed in order to manage environments, on Windows installation is: `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -` or other versions of this command for your operating system.  
 - You can check if you have poetry installed: `poetry --version`

## Installation

To install the project, follow these steps:

1. Navigate to your folder and create poetry virtual environment `poetry env use python 3.9` or other Python version you have, to check your version run `python --version`
2. Make sure you have poetry-core installed: `pip install poetry-core`
3. To install the project directly from repository use `pip install git+https://github.com/mariarzv/projectMLinCV.git@assignment1`  or if that doesn't work you can clone or download the repository and install the package directly from dist folder:

1. Install the required dependencies by running `pip install -r requirements.txt` in the terminal.
2. Run `cd dist` and `pip install projectmlincv-0.1.0-py3-none-any.whl` to install the project using the wheel file. If project is already installed with the same version as the provided wheel you can use --force-reinstall to force an installation of the wheel.

## Running

To run the project, navigate to demo.py directory and run `python demo.py`. This will grab an image and save the inference result in the images folder.





