# AESRLib - The blend of AES-**R** #
##### v1.0-beta [beta-release] #####
PyPi package for variable key based triple layer capsule encryption with power of AES, base64 and user-defined **randomizer (R)** functions.

**Index**

  - [AESRLib - The blend of AES-**R**](https://pypi.org/project/AESRLib/)
        - [v1.0-beta [beta-release]](#v10-beta-beta-release)
  - [Usage](#usage)
    - [1.1.1 Installation](#111-installation)
      - [1.2 Using it](#12-using-it)
    - [1.1.2 Alternative](#112-alternative)
  - [Future Proposals](#future-proposals)
  - [LICENSE](#license)


## **Usage** ##
To install and use it follow below steps as per convenience.

### 1.1.1 **Installation** ###
To download it, either fork this github repo or simply use Pypi via pip in a python3 supported environment.
```
pip install AESRLib
```
#### 1.2 **Using it** ####
First, import the module using:
```
import AESRLib as aesr
```
And you are ready to go! The interactive function to trigger AESR for ready-to-use purpose is:
```
aesr.AESRandomizer.initializer(filename)
```
filename - Its the input filename given with extension for processing like 'test.txt'
Providing the abstract function for instant use makes the user's task too easy and readily accessible
Ensure that the script using AESR is run in the **same root folder** as the file.

### 1.1.2 **Alternative** ###
Executable file (*.exe) for windows based systems is also available at 
https://mega.nz/file/1k8nzYib#evvzAgQiqgSldDx1Xi9odKMhOZLxDss1qJPkWv5ZhCA for instant usage, so just download it and run directly or open cmd/powershell and type .\AESR if screen is exiting too fast after showing error or isn't executing.
_N.S. The file often gets blocked by windows defender smartscreen or shows PUP/virus alert. In that case please install it using above steps._

## **Future Proposals** ##
1. Includes enhancement for randomization function
2. Bug fixes

## **LICENSE** ##
MIT License Copyright (c) 2018

 **Updated**: 3.5.22 6.54.00 PM
