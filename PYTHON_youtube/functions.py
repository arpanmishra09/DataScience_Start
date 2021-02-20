def add(x,y):
    c=x+y
    return(c)
#function is of two types: one like above returns a value which can be stored and used again
#and another like below which prints the value

def plus(x,y):
    c=x+y
    print(c)

#return two values
def add_sub(x,y):
    c= x+y
    d=x-y
    return c,d
#since we are returning two values we need to two variables to accept them

result1,result2 = add_sub(2,3)
