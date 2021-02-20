n = 'peter piper picked a peck of pickled peppers'
a= n.split()
i=0
stri='peck'
if stri in a:
    for i in range(len(a)):
        if stri == a[i]:
            b=n.replace(stri,'pack')
            print(b)
            break
        else:
            pass
else:
    print(f'{stri} not found')
