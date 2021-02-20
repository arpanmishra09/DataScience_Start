from numpy import *
#shallow copy: change in one array does affect the other array
arr=array ([1,2,3,4,5])
arr2= arr.view() #.view() helps to create an array at a different location
arr[1]=7
print(arr)
print(arr2)
print(id(arr))
print(id(arr2))

#deep copy: change in one array does not affect the other array
arr=array ([1,2,3,4,5])
arr2= arr.copy()
arr[1]=7
print(arr)
print(arr2)
print(id(arr))
print(id(arr2))