# Compilers
## Authors
Andrew Dunkerley

Manuel Barrera

Miguel Bustamante
## Development Report
### Introduction
The purpose of this document is to explain and explore the creation of a translator that acts like a compiler. The experiment has the capability of graphing the path that the compiler uses to access the values defined in our gramatic.
### Translator Design
---
The translator use the following structure:
* Importing libraries to be used.
* Define imported tokens from libraries. 
* Define the accepted tokens. 
* Define accepted special simbols.
* Define Token management.
* Node visiting process.
* Checking the text file. 
### Image Processing
---
The code being worked on has the capability to run a command and return the matrix of the values of a image using the command of: 
```
execute

load nameofthefile
```
Example 

```
load cv2.png
```

After being executed the translator will show the following if ran from terminal:

![Load image](imageesmkd/load.png)


### List Manipulation
---
The purpose of this module is to enable the translator to use the values allready assigned and apply them in python lists. 

Lists have the option of arithmetic operations, value assignation, value reassignation, and list manipulation. 

```
execute

mylist=[1,2,3,4,5]
```
The returned graph image should look as the following:

![Load image](imageesmkd/ListCreation.png)

Creating the list then there is the capability to return and save values. To use individual values of a list it must be assigned to a variable and then it can be operated as normal.

```
>x=mylist[2]  
Result 3
```

Afterwards then the value can use different arithmetical operations such as sumations

```
>x+2
Result 5
```

Summation graph representation.

![Load image](imageesmkd/valueAccess.png)

In case of the sumAB the following visualization is the following: 

```
list=[1,2,3,4,22]

>sumAB(x,list[4])
Result 25
```
![Load image](imageesmkd/SumAB.png)

### Numpy installation
---
Numpy is an almost elementary library needed for the use of statistics, and other values for basic mathematics. The need to have them in access imperative and therefore the following installations have been done.

The code has the following to bring the library acts as the following.

Import 9 different libraries are the following:

* mean
* standard deviation
* variance
* min
* max
* array
* summation 
* product
* cumulative sum
* where


### Numpy implementation
### Unit Testing Devlopment
### Unit Testing of Capacities