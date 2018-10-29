# T4C script 
## (a.k.a: There's no tripe for cats)

- ###### The script is currently supporting only conversion from CSV to JSON format:   
    - source CSV file must be placed inside "./data" folder
    - the output is also saved in "./data" and contains max 2 files (one with export, the other with errors)
    - this
- ###### The script accepts multiple arguments but none of them is mandatory:
    - **--source-file** : obviously the CSV file used as input
        - Default: ./data/hotels.csv
    - **--destination-file** : the file name or full path of the file where to store the output: 
        - Default: ./data/hotels.json
    - **--overwrite-destination-file** : flags that control the overwriting of the JSON file
        - Default: True
    - **--sort-by-field** : the name of the Field that can be used to sort the output file. If the name provided is not in the list of valid fields, "name" is used as fallback
        - Default: by default there's no sorting
    - **--complex-url-validation** : URL in the file are syntactically validate by default but there's an additional check that can be activated calling this parameter. If set to "True" the script will attempt to resolve the Top Level Domain. If no IP (4&6) is returned the validation fails and the item is not added to the destination file.
        - Default: False
        - **NOTE**: enabling this feature drastically reduces the performances of the script due to network traffic, dependency on DNS response time and sometimes throttling Don't enable if you don't have connectivity.
            - script is currently not checking for connectivity

##### Example:
 ````
 > python t4c.py  # (all default will be used)
 or
 > python t4c.py --overwrite-destination-file=False --sort-by-field=stars --complex-url-validation=True
 ````
 ----
 
# Let´s make it work:
This script depends only on few not standard libraries

###### validators - https://github.com/kvesteri/validators

###### tldextract - https://github.com/john-kurkowski/tldextract

and it has been developed with **python 2.7**

In order to run it please make sure that all dependencies are installed.

**Note**: in a vanilla MacBook I slightly struggled because not even *pip* was installed and some SSL TLS 1.0 error were thrown.
Depending on the OS you´re running, make sure that at least is installed:
#### MacOS Sierra (10.12.6)
````
$> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$> sudo python get-pip.py
 ### make sure Pip is installed now
$> pip -V
    > pip 18.1 from {your library folder}
````
###### Time now to install dependencies for t4c:
 
````
 ## inside the main t4c folder
$> sudo pip install -r requirements.txt
````
When the script finish to install the required modules, you are ready to successfully run the script!

### Linux Debian Stable

with Debian 9.5 Stretch **Python 2.7.13 (default, Nov 24 2017, 17:33:09)** is already installed however **pip** is missed.
Let's install it

````
admin@myhost:~/t4c-master$ sudo easy_install pip

[...]
Installing pip script to /usr/local/bin
Installing pip2.7 script to /usr/local/bin
Installing pip2 script to /usr/local/bin

Installed /usr/local/lib/python2.7/dist-packages/pip-18.1-py2.7.egg
Processing dependencies for pip
Finished processing dependencies for pip

$> pip -V
pip 18.1 from /usr/local/lib/python2.7/dist-packages/pip-18.1-py2.7.egg/pip (python 2.7)
````
Time now to install the required modules (assuiming you have already *t4c* folder in place and you are in
````
admin@myhost:~/t4c-master$ sudo pip install -r requirements.txt

Collecting validators (from -r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/45/7b/5b7b74208a3e0744d1a0efbfb1935fa46fa4cfe58d3d63f17c49c58c429c/validators-0.12.2.tar.gz
Collecting tldextract (from -r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/0e/0c/1b7332684dfc2e6311d59cd00859a5318a7e0ba50334ad217ceb9555e213/tldextract-2.2.0-py2.py3-none-any.whl (52kB)
    100% |████████████████████████████████| 61kB 4.0MB/s 
    
 [....]
````

Ready to run the script now!!

````
admin@myhost:~/t4c-master$python t4c.py

#############################################
2018-10-29 17:35:37,685 - INFO - I saved and validated 3999 hotels in 0.871470928192 seconds
2018-10-29 17:35:37,685 - INFO - Unfortunately 1 hotels did not pass the validation
2018-10-29 17:35:37,685 - INFO - You can find all the generated data inside /home/admin/t4c-master/data
2018-10-29 17:35:37,686 - INFO - Overall script took: 0.874050855637 seconds

````

#### Windows 10

First of all install Python 2.7 downloading the package from
https://www.python.org/downloads/release/python-2715/ (currently latest version)

Download the right version from you architecture (eg: **Windows x86-64 MSI installer**) 
Just follow the wizard and make sure that it automatically adds the python folder in PATH variable (it can be done manually...but why tto go for this hassle?)

At this point python is installed and also PIP is part of the release.
You can now open the command line (better as Administrator) and install the dependencies as we did for Mac

````
## inside the main t4c folder
$> pip install -r requirements.txt
````

here you go again... script is ready to be run as in the Mac and Debian instructions

