# AESRLib - The blend of AES-**R** #
##### v2.0-beta [beta-release] #####
PyPi package for variable key based triple layer capsule encryption with power of AES, base64 and user-defined **randomizer (R)** functions.

**Index**

  - [AESRLib - The blend of AES-**R**](https://pypi.org/project/AESRLib/)
  - [1.0 Changelog](#10-changelog)
  - [2.0 Usage](#20-usage)
    - [2.1 Installation](#21-installation)
    - [2.2 Using it](#22-using-it)
      - [2.2.1 With IDE/IDLE ](#221-with-ideidle)
      - [2.2.2 With CMD/PS/Terminal ](#222-with-cmdpsterminal)
  - [3.0 Future Proposals](#30-future-proposals)
  - [4.0 LICENSE](#40-license)

## **1.0 Changelog** ##
> What's new in **v1.0b1** (v1.0-beta) than **v1.0b0** (v1.0-beta2)

* Additions: Version compatibility, password validations and retries, error handling, minor casting and snake case fixes.
* Removals: nTry method for multiple attempts check.

## **2.0 Usage** ##
To install and use it follow below steps as per convenience.

### 2.1 **Installation** ###
To download it, either fork this github repo or simply use Pypi via pip in a python3 supported environment. If you don't have python in your system, download from python official site (https://www.python.org/downloads)
```
pip install AESRLib
```

### 2.2 **Using it** ###
#### 2.2.1 With IDE/IDLE ####
First, import the module using:
```
from AESRLib import AESRandomizer as alib
```
And you are ready to go! The interactive function to trigger AESR for ready-to-use purpose is:
```
alib.initializer(filename)
```
filename - Its the input filename given with extension for processing like 'test.txt'
Providing the abstract function for instant use makes the user's task too easy and readily accessible
Ensure that the script using AESR is run in the **same root folder** as the file.

#### 2.2.2 With CMD/PS/Terminal ####
A ready to use way for running it without any hassle, just follow the steps (after installation of AESRLib as referred above):
1. Download/Copy the main.py file in a folder locally (main.py file is available in https://github.com/me-yutakun/AESRLib)
2. Go to that folder and open cmd/powershell/terminal
3. Place the file you want to encrypt/decrypt in same folder
4. Type ``` python main.py``` in cmd/powershell/terminal then press enter

**Recommended**: If screen is exiting too fast after showing error or you are not able to see the result properly use this way to run it.

## **3.0 Future Proposals** ##
1. Includes enhancement for randomization function
2. Bug fixes

## **4.0 LICENSE** ##
MIT License Copyright (c) 2018

###### **Updated**: 21.5.22 6.00.00 PM (IST)