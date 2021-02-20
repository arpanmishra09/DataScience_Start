import array as arr
a= arr.array('i',[])
n = int(input('enter the length of the array: '))
for i in range(n):
    x= int(input('enter the next value: '))
    a.append(x)
print(a)

#delete the value at index 2
k=0
for k in a:
    if k==2:
        a.pop(2)
        print(a)
        break
k+=1

#reverse array
r= list(reversed(a))
print(r)

#to output the value from the position as the input from the user
b=int(input('enter the position of the value required'))
p=a[b]
print(p)

#to check whether the input by the user is present in th array
x= int(input('enter the value to search'))
for v in a:
    if v == x:
        print (v, 'is available at position', a.index(x))
        break


