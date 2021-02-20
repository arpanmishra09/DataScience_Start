n= 'peter piper picked a peck of pickled peppers.\n'
j = 0
for i in range(len(n)):
    if n[i]=='p':
        j+=1
        print(i)