#we are using lambda here as the functions like filter reduce and
#maps need two inputs one a fuction and other the set of values as seen below
import functools as func
nums = [2,5,7,8,5,77,9,34,67,56,87]
evens= list(filter(lambda n:n%2==0,nums))#the filter option filters the data as per the required criteria
double= list(map(lambda n:n*2,evens))#maps performs operations on a chunck of data
sum= func.reduce(lambda a,b:a+b,double)#reduce function gives out a single value like the sum of the numbers and
#only works once funtools is imported
print(evens)
print(double)
print(sum)