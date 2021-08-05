from ch import ConvexH
import numpy as np

# example 1:
points = np.load(r'examples\example_1.npy')
ConvexH(points).plot(file=r'outputs\plot1_noraml',rnd=1)

# example 2:
points = np.load(r'examples\example_2.npy')
ConvexH(points).plot(file=r'outputs\plot2_circle',rnd=1)

# example 3:
points = np.load(r'examples\example_3.npy')
ConvexH(points).plot(file=r'outputs\plot3_square',rnd=1)

# example 4:
points = np.load(r'examples\example_4.npy')
ConvexH(points).plot(file=r'outputs\plot4_hex',rnd=1)
