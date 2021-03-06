## My-Convex-Hull
Convex Hull Algorithm, build from scratch ,using the Monotone-Chain method.

## Overview
Convex Hull is the minimum boundary of given set of data points. After it calculated, every point in the given set should be inside the hull, or part of its border. To find this hull, we should use proper convex-hull algorithm. The code [**ch.py**](https://github.com/EtzionR/My-Convex-Hull/blob/main/ch.py) is version of such convex hull 2D algorithm that build from scratch. 

The algorithm process build from **Four** steps:
- In order to get the boundary around our 2D points, we must first **sorting** the points, using to their X values.

- Now, we will **divide the calculation**, so that it focuses on a different hull each time, once on the top and once on the bottom, as follows:

&emsp;&emsp; ![upperlower](https://github.com/EtzionR/My-Convex-Hull/blob/main/pictures/upperlower.png)

- We perform the calculation for each such sub-boundary (hull). In order to verify that we choose the desired path, we use **invalid function** (lambda function). This function identifies for each point if there is a better route to it. When a "better path" means relativity lower slope than the slope to the previous point. You can see such example in the following figure:

&emsp;&emsp; ![better_path](https://github.com/EtzionR/My-Convex-Hull/blob/main/pictures/better.png)

&emsp;&emsp;As you can see, the slope between point 7 to 9 is lower then the slope between 7 to 8. So we choose to remove point 8 from the hull.

&emsp;&emsp;These properties converted into an equations, which can be developed into our **invalid function**: 

&emsp;&emsp;<img src="https://render.githubusercontent.com/render/math?math=\frac{Y_{2}-Y_{0}}{\X_{2}-X_{0}}\leq\frac{Y_{1}-Y_{0}}{\X_{1}-X_{0}}">

&emsp;&emsp; Which equal to: 

&emsp;&emsp;<img src="https://render.githubusercontent.com/render/math?math=(Y_{2}-Y_{0})*(X_{1}-X_{0})\leq(Y_{1}-Y_{0})*(X_{2}-X_{0})">

&emsp;&emsp; When in our example, point 7 = (x0,y0), point 8 = (x1,y1) & point 9 = (x2,y2)

- After the calculation of the top & bottom hulls, all we need is **merge** them to one final hull.

It should be noted that the given example describe calculation of the lower hull. The function also works in the upper case, because we using reverse points list. The order of the coordinates ensures a negative denominator in the slope equation. So the denominator makes the left slope negative and the right positive if there is a better path.

You can also see a simple example of how the calculation is done, in each step of building the hull:

![convex_gif](https://github.com/EtzionR/My-Convex-Hull/blob/main/pictures/convex_process.gif)

Now, it is also possible to calculate the area of the results hull polygon. The calculation is performed using the following equations, which are used to calculate an irregular polygon area:

<img src="https://render.githubusercontent.com/render/math?math=A=\sum_{i = 1}^{m-1} X_{i}*Y_{i%2B1}">

<img src="https://render.githubusercontent.com/render/math?math=B=\sum_{i = 1}^{m-1} X_{i%2B1}*Y_{i}">

<img src="https://render.githubusercontent.com/render/math?math=Polygon Area=\frac{A-B}{2}">

When m = number of points in the hull and X&Y coordinates of the hull.

You can see example to area calculation in the following figure. It describe Convex-Hull boundary that created around point that sampled inside Unit-Circle. The actual area of the polygon should be close to pi (3.14) and we can see that the calculate area we get is 3.12:

![area](https://github.com/EtzionR/My-Convex-Hull/blob/main/pictures/area.png)

The object also calculate the perimeter of the hull (length), by sum all the length of each line in the hull, as you can see in the equation:

<img src="https://render.githubusercontent.com/render/math?math=Length=\sum_{i=1}^{m-1}\sqrt{(X_{i%2B1}-X_{i})^{2}%2B(Y_{i%2B1}-Y_{i})^{2}}">

The Convex-Hull object also can also generated as an output plot of the results, in a simple using of the built-in function:

``` sh
# load libraries:
import numpy as np
from ch import ConvexH

# create xy coordinates:
points = np.random.normal(0,1,(100,2))

# calculate convex-hull & plot results:
ConvexH(points).plot()
```

![plot](https://github.com/EtzionR/My-Convex-Hull/blob/main/pictures/plote.png)

## Libraries
The code uses the following library in Python:

**matplotlib**


## Application
An application of the code is attached to this page under the name: 

[**implementation.py**](https://github.com/EtzionR/My-Convex-Hull/blob/main/implementation.py)

The examples and the outputs are also attached here: [examples](https://github.com/EtzionR/My-Convex-Hull/tree/main/examples) & [outputs](https://github.com/EtzionR/My-Convex-Hull/tree/main/outputs).


## Example for using the code
To use this code, you just need to import it as follows:
``` sh
# load libraries:
import numpy as np
from ch import ConvexH

# create xy coordinates:
points = np.random.normal(0,1,(100,2))

# calculate convex-hull get the hull boundary:
hull = ConvexH(points).vertex
```

When the variables displayed are:

**points:** list or array of 2D x,y coordinates

## License
MIT ?? [Etzion Harari](https://github.com/EtzionR)
