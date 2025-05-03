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

### test data
looks like its having trouble reading "I Hate this place"
thinks its positive
the test data works well tho

tried balancing out the data 30 bad 30 good
no seeable changes

trying with bigger data set
there is 6990280 reviews in yelp academic data set
i made 1-3 stars bad and 4,5 good


### timing data
I limited the amount of data from 6880280 to 25000
code basically checks if we read in 25000 and stops reading it in
6880280 takes a lot of days

7:38.14 mins to train the 25000
looks like it just set all data points to 0


# Timing functions
for 25000 data points
Reading Execution time: 0.026098 seconds
Jsoning Execution time: 0.092817 seconds
Filtering Execution time: 0.006079 seconds
Cleaning Execution time: 224.400014 seconds


# making mistakes in git
use git commit --amend to add staged changes to last commit
if you forgot to add files or need to update name

use "git restore --staged <file>..." to unstage
to unstage files

use "git restore <file>..." to discard changes in working directory
to undo modified changes


# pushing things to github

adding a new alias
git remote add origin (url to online repo)

pushing changes to remote
git push -u origin master