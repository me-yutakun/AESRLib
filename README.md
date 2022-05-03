# AESRLib - The blend of AES-**R** #
##### v1.0-beta [beta-release] #####
PyPi package for variable key based triple layer capsule encryption with power of AES, base64 and user-defined **randomizer (R)** functions.

**Index**

- [AESRLib - The blend of AES-**R**](#aesrlib---the-blend-of-aes-r)
        - [v1.0-beta [beta-release]](#v10-beta-beta-release)
  - [**1.1 Usage**](#11-usage)
    - [1.2 Installation](#12-installation)
    - [1.3 Using it](#13-using-it)
  - [**2.1 Future Proposals**](#21-future-proposals)
  - [**3.1 LICENSE**](#31-license)


## **1.1 Usage** ##
To install and use it follow below steps as per convenience.

### 1.2 Installation ###
To download it, either fork this github repo or simply use Pypi via pip in a python3 supported environment.
```
$ pip install AESRLib
```
### 1.3 Using it ###
First, import the module using:
```
import AESRLib as aesr
```
And you are ready to go! The interactive function to trigger AESR for ready-to-use purpose is:
```
aesr.AESRandomizer.initializer(filename)
```
filename - Its the input filename given with extension for processing like 'test.txt'
Providing the abstract function for instant use makes the user's task too easy and handy.

## **2.1 Future Proposals** ##
1. Includes enhancement for randomization function
2. Bug fixes

## **3.1 LICENSE** ##
MIT License Copyright (c) 2018

 **Updated**: 3.5.22 5.04.00 PM