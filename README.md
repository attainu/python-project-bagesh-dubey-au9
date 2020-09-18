# Junk file organizer

Basically, as a lazy programmer my desktop is full of files (Junk Files). Due to the large number of files, it is a daunting task to sit and organize each file.
This program will help you to organize your files of a particular directory by any of the following options - extension/ size/ used.

## Getting Started

These instructions will describe step by step process to run the program in your local machine.

### Prerequisites

What things you need to install --

```
Python 3.x
```

### Module Used

import os
import argparse
import shutil
import datetime
from stat import ST_SIZE, ST_ATIME 


### Running the script

1. Clone the repository [link](https://github.com/attainu/python-project-bagesh-dubey-au9/tree/dev).
2. Open cmd/powershell for windows ***"file.py"*** file directory.
    * For windows use **shift + right click** and an option(**Open cmd window here**) will appear in the menu.
    
3. Type the following command: **python file.py --path <directory> --by <option>**
```
python file.py --path C:\Users\bages\Desktop --by extension
```
** By default, the directory will be the ***current directory path*** and option will be ***extension***.

4. To check the available options type the following command: **python file.py --h**
5. Press **enter** to run the script.

## Built With

* [Python](https://www.python.org/) - Language used for the program.

## Version

* Current version - 0.1

## Author

* BAGESH KUMAR DUBEY