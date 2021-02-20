lst=[]
n= int(input('enter the length of the list'))
for i in range(n):
    x= int(input('ebter the next number'))
    lst.append(x)

lst.sort()
print('the second largest number is {x}'.format(x=lst[-2]))