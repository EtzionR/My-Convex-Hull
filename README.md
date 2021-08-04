## My-Convex-Hull
Convex Hull Algorithm, build from scratch ,using the Monotone-Chain method.

## Overview
- In order to get the boundary around our 2D points, we must first **sorting** the points, using to their X values.
Now, we will divide the calculation so that it focuses on a different **hull** each time, once on the top and once on the bottom, as follows:

Boundary illustration

Now, we will go over each such sub-boundary and perform the calculation on it. In order to verify that this is indeed the desired delimitation, a invalid function was constructed, which identifies cases in which lambda function is attached to the delimitation points. The function works so that it checks for each point if there is a better route to it. When a better trajectory is characterized by a lower slope than the slope relative to the previous point, as can be seen in the following figure:

Illustration examples

These properties can of course be converted into an equation, which can be developed into the Invalid function used:

Equations

It should be noted that the example is given from the calculation of the lower limit. The function also works in the upper limit calculation, where there is the fact that we are operating on the reverse list. The inversion of the coordinates ensures a negative denominator in the slope always, which makes the left slope negative and the right positive if there is a better trajectory.

Now, it is also possible to calculate the area of the generated polygon. The calculation is performed using the following equations, which are used to calculate an irregular polygon area:

Equations

You can also see a simple example of how the calculation is done:

?

Also, the results of the algorithm can also be generated as an output in a simple way using a built-in function:

``` sh

```

picture


## Libraries
The code uses the following library in Python:

**matplotlib**


## Application
An application of the code is attached to this page under the name: 

[**implementation**]()

the examples outputs are also attached here.


## Example for using the code
To use this code, you just need to import it as follows:
``` sh

```

When the variables displayed are:

**data:** explanation



## License
MIT © [Etzion Harari](https://github.com/EtzionData)
