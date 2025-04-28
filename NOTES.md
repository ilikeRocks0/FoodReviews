# Notes
personal notes when working on this project


### enviroment 
created venv with
python -m venv .venv



open venv
.\.venv\Scripts\activate

to turn off
deactivate


### downloading pip 2.0.0
Interesting things I learned
python 11 was downloaded from microsoft store so I dont have access to the file location
python 11 location
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\python3.11.exe
python 3.8.3 location (what I was using previously)
C:\Users\mager\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts

pip 2.0.0 only works with versions python 3.9 >

doing the following uses the python 3.11 version (i didnt know you can specify the version cool!)
py -3.11

-m is a parameter that makes it run a module that avoids unneccesary scripts
yea I still dont know

I created the python enviroment with py -3.11 -m venv my_new_env
specifying -3.11, so python version 3.11 will make the python environment with version 3.11

### making it easy to redownload dependencies on other computers
Dependecy downloads
pip freeze gets all dependencies
so use pipreqs
pipreqs ./src
looks like pipreqs had issues scanning the zip and env files so I moved files to src


Now to install correct requirements
pip install -r /path/to/requirements.txt


