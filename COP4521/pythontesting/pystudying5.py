import dask
from dask import delayed

@delayed
def square(x):
    return x*x


nums = [3,4,1,2,3,6,7,89,6,4,76,89,6,4,7,89,6,5,4]
squared_nums = [square(num) for num in nums]

result = delayed(sum)(squared_nums)

print("sum: ",result.compute())
