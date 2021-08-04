# Create by Etzion Harari
# https://github.com/EtzionR

# Load Library
import matplotlib.pyplot as plt

# Define useful function
# [check if hull last angle invalid or not]
invalid = lambda p1 ,p2 ,p3: ((p2[0]-p1[0])*(p3[1]-p1[1])) <= ((p2[1]-p1[1])*(p3[0]-p1[0]))

class ConvexH:
    """

    Convex Hull object
    calculate the minimum boundary around 2D points sample
    build from scratch, using Monotone-Chain Algorithm

    this object also calculate the boundary polygon area
    and allowing plot the results

    """
    def __init__(self,points):
        """
        The initilaize of the object
        Calculated all the required results
        :param points: input 2D xy points
        """
        self.points = sorted(points, key = lambda x: x[0])
        self.vertex = self.get_hull(self.points )+self.get_hull(self.points[::-1])[1:]
        self.length = len(self.vertex)
        self.area = self.calculate_area()

    def get_hull(self,points):
        """
        Calculate one-side hull
        (upper or lower hull)
        :param points: input xy points with sorted order
        :return: upper/lower hull for this points
        """
        hull = [points[0]]
        for point in points:
            while len(hull)>1 and invalid(hull[-2],hull[-1],point):
                hull.pop()
            hull.append(point)
        return hull

    def calculate_area(self):
        """
        calculate the area of the convex hull polygon
        :return: polygon area
        """
        sum1 = sum([self.vertex[i][1]*self.vertex[i-1][0] for i in range(1,self.length)])
        sum2 = sum([self.vertex[i][0]*self.vertex[i-1][1] for i in range(1,self.length)])
        return (sum1-sum2)/2

    def plot(self,size=6,file=False):
        """
        plot the convex hull results
        :param size: required plot size
        """
        org_x = [x for x,y in self.points]
        org_y = [y for x,y in self.points]
        con_x = [x for x,y in self.vertex]
        con_y = [y for x,y in self.vertex]
        ratio = (max(con_y)-min(con_y))/(max(con_x)-min(con_x))

        plt.figure(figsize=(size, size*ratio))
        plt.title(f'Convex-Hull results:\nCompose of {self.length} points, Area = {int(self.area)}')
        plt.scatter(org_x ,org_y ,s=size,color='b' ,label='original points')
        plt.plot(con_x ,con_y ,color='r' ,label='Convex-Hull boundary')
        plt.legend(fontsize=12)
        if file: plt.savefig(f'{file}.png')
        plt.show()

# MIT © Etzion Harari
