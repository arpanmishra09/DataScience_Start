lst= []
n= int(input('enter the length'))
for i in range (0,n):
    e= int(input('enter the number'))
    lst.append(e)
print(lst)

s= int(input('enter the number to be searched'))

for i in range(n):
    if lst[i] == s:
        print('True')
        break
    else:
        print('false')
        break