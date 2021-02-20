n= 'This is Python class'
a= n.split(' ')
i=0
for i in range(len(a)-1):
    if a[i]=='is':
        a.remove(a[i])


for i in range(len(a)-1):
     if a[i]=='Python':
         j= a.index('Python')
         a[j:(j+2)] = [' '.join(a[j:(j+2)])]
         print(str(a))
