"""
Name:Merrick Moncure
Date: 2/9/25
Assignmnent: Module 5: Python Dask Multi Task Script
Returns a number in a series from a parameter and uses @delayed and dask.compute
Assumptions: NA
All work below was performed by Merrick Moncure
"""
from dask.distributed import Client
import dask.array as da
from ComputeScript import func1, func2, func3
import matplotlib.pyplot as plt

if __name__ == "__main__":
    client = Client()
    print (client)

    values1 = func1(1, 334)
    values2 = func2(334, 667)
    values3 = func3(667, 1001)

    result = values1 + values2 + values3

    result.visualize(filename='graph.png') #creates the task graph


    print("Task graph saved as graph.png")
"""
    img = plt.imread('graph.png') #displays the image for testing purposes
    plt.imshow(img)
    plt.show()
"""