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
load("cv2.png")
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
* summation 
* product
* cumulative sum
* linspace

Mean, standard deviation and variance were chosen as they are basic operations in staticstics and that also work with lists. 

Minimum and Maximum are search operations that work on lists and return the lowest and highest values in a list. These operations should return a single value as result. 

Summation, Cumulative Sum and Product are perfect to test the list acessing capabilities by the imported libraries. 

Linspace test out the list creation automatically.



### Numpy implementation
---
#### Step in common

Every library is imported with the following code: 

```
import numpy as np
```

With this step the code can add otheer numpy libraries if needed.

#### Mean
The first step is

#### Standard Deviation

`np.std()` is another function from the numpy library, specifically used to calculate the standard deviation of a list or array of numbers. 
In this case `np.std` is added to the symbol_table in your code:

`symbol_table["np.std"] = np.std`

This means that it can be invoked from the expressions being parsed by the parser.

The np.std() function computes the standard deviation of the given data. The standard deviation is a measure of the amount of variation or dispersion in a set of values. It tells you how much the values in a dataset differ from the mean value.

Let's consider an example where you have a list of numbers and you want to calculate the standard deviation:

```
import numpy as np

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the standard deviation using np.std
std_deviation = np.std(numbers)
print("The standard deviation is:", std_deviation)
```

In this example, `np.std(numbers)` will return the standard deviation of the numbers in the list, providing a measure of how spread out the numbers are from the mean value.

#### Variance
The `np.var()` function computes the variance of the given data. Variance is a measure of how much the values in a dataset vary from the mean value. It is calculated as the average of the squared differences from the mean.

Let's consider an example:

```
import numpy as np

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the variance using np.var
variance = np.var(numbers)
print("The variance is:", variance)
```
In this example, np.var(numbers) will return the variance of the numbers in the list, providing a measure of how spread out the numbers are from the mean value.

This functionality enhances the parser's capabilities for statistical calculations, allowing it to handle tasks such as mean, standard deviation, and variance computations within the expressions it processes.

#### Minimum value
`np.min()` is a function from the `numpy` library that calculates the minimum value of a list or array of numbers:

Like other numpy functions, np.min is added to the symbol_table in the code:

`symbol_table["np.min"] = np.min`

The `np.min()` function computes the minimum value of the given data. It returns the smallest value in an array or along a specified axis.

Let's consider an example where you have a list of numbers and you want to find the minimum value:

```
import numpy as np

# Example list of numbers
numbers = [5, 3, 8, 1, 6]

# Calculate the minimum value using np.min
minimum_value = np.min(numbers)
print("The minimum value is:", minimum_value)
```
In this example, np.min(numbers) will return the minimum value from the list, which is `1`.

#### Sum
`np.sum()` is another function from the `numpy`library, designed to compute the sum of elements within a list or array of numbers. Let's break down its usage within the context of the code:

`np.sum` is included in the `symbol_table`using the following code:

`symbol_table["np.sum"] = np.sum`

This inclusion allows for the invocation of `np.sum` from the expressions parsed by your parser.

The `np.sum()` function calculates the sum of all elements in the provided array or along a specified axis. It returns the sum of the elements as a single scalar value.

Consider an example where you have a list of numbers and you want to compute their sum:

```
import numpy as np

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum using np.sum
sum_value = np.sum(numbers)
print("The sum of the numbers is:", sum_value)
```

In this example, `np.sum(numbers)` will return `15`, which is the sum of all the numbers in the list.



### Unit Testing Devlopment
### Unit Testing of Capacities