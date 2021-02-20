def count(b):
    i=0
    j=1
    if b==1:
        print(i)
    elif b<0:
        print('please provide poistive number')
    else:
        print(i)
        print(j)
        for a in range(b):
            x=i+j
            i=j
            j=x
            print(x)

n=int(input('enter the required range of series: '))
b=count(n)

