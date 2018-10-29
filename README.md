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

here you go again... script is ready to be run.

### Linux Debian Stable

with Debian 9.5 Stretch python



