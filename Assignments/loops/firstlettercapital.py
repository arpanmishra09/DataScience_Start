n = 'peter piper picked a peck of pickled peppers'
a= n.split()
i=0
b=''
for i in range(len(a)):
    b = a[i].capitalize()
    print(b,'',end='')
    i+=1