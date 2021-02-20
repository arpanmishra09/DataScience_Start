
def fact(x):
    j=1
    for i in range(1,x+1):
        j=j*i
    return j

x=int(input('enter the required factorial'))
ans=fact(x)
print(ans)