## My-Convex-Hull
Convex Hull Algorithm, build from scratch ,using the Monotone-Chain method.

## Overview
The algorithm works by **Four** steps:
- In order to get the boundary around our 2D points, we must first **sorting** the points, using to their X values.

- Now, we will **divide the calculation**, so that it focuses on a different hull each time, once on the top and once on the bottom, as follows:

&emsp;&emsp; ![upperlower](https://github.com/EtzionR/My-Convex-Hull/blob/main/pictures/upperlower.png)

- We perform the calculation for each such sub-boundary (hull). In order to verify that this we take the desired path, we use **invalid function** (lambda function). This function identifies for each point if there is a better route to it. When a "better path" means relativity lower slope than the slope to the previous point. You can see such example in the following figure:

&emsp;&emsp; ![better_path](https://github.com/EtzionR/My-Convex-Hull/blob/main/pictures/better.png)

&emsp;&emsp;As you can see, the slope between point 7 to 9 is lower then the slope between 7 to 8. So we choose to remove point 8 from the hull.

&emsp;&emsp;These properties converted into an equations, which can be developed into our **invalid function**: 

&emsp;&emsp;<img src="https://render.githubusercontent.com/render/math?math=\frac{Y_{2}-Y_{0}}{\X_{2}-X_{0}}\leq\frac{Y_{1}-Y_{0}}{\X_{1}-X_{0}}">

&emsp;&emsp; Which equal to: 

&emsp;&emsp;<img src="https://render.githubusercontent.com/render/math?math=(Y_{2}-Y_{0})*(X_{1}-X_{0})\leq(Y_{1}-Y_{0})*(X_{2}-X_{0})">

&emsp;&emsp; When in our example, point 7 = (x0,y0), point 8 = (x1,y1) & point 9 = (x2,y2)

- After the calculation of the top & bottom hulls, all we need is **merge** them to one final hull.

It should be noted that the given example describe calculation of the lower hull. The function also works in the upper case, because we using reverse points list. The order of the coordinates ensures a negative denominator in the slope equation. So the denominator makes the left slope negative and the right positive if there is a better path.

You can also see a simple example of how the calculation is done:

?

Now, it is also possible to calculate the area of the results hull polygon. The calculation is performed using the following equations, which are used to calculate an irregular polygon area:

<img src="https://render.githubusercontent.com/render/math?math=A=\sum_{i = 1}^{m-1} X_{i}*Y_{i+1}">

<img src="https://render.githubusercontent.com/render/math?math=B=\sum_{i = 1}^{m-1} X_{i+1}*Y_{i}">

<img src="https://render.githubusercontent.com/render/math?math=Polygon Area=\frac{A-B}{2}">

Also, the results of the algorithm can also be generated as an output plot, in a simple using of built-in function:

``` sh
# load libraries:
import numpy as np
from ch import ConvexH

# create xy coordinates:
points = np.random.normal(0,1,(100,2))

# calculate convex-hull & plot results:
ConvexH(points).plot()
```

![plot](https://github.com/EtzionR/My-Convex-Hull/blob/main/pictures/plot.png)


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
