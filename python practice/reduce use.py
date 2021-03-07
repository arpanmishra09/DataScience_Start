from functools import reduce
# a=0
# b=1
# print(a)
# print(b)
# for i in range(10):
#     c=a+b
#     a,b=b,c
#     print(c)


f= lambda N: reduce(lambda x,y: x+[x[-1]+x[-2]],range(N-2),[0,1])
print(f(10))

# lambda N: is takind up the range as input
# x+[x[-1]+x[-2]]: this is adding the last two number in the list adding the sum to the list
# like by adding 1,1, 2 gets added to the list[0,1,1,2]
# range(N-2) as we have taken two values already i.e. 0 and 1 so we reduce the range by 2
# {0,1} we are initializing x with this list
# here y has no function and is being taken as reduce needs two arguments