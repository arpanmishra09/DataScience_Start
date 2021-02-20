n= input('enter an integer')

if (n.isdigit()) and n.count('-')==0:
    a = int(n)
    if a%2==0:
        print('even number')
    else:
        print('odd number')
elif (n.replace('-','',1).isdigit()) and (n.index('-')==0) and (n.count('-')==1):
    a = int(n)
    if a%2==0:
        print('even number')
    else:
        print('odd number')
else:
    print('ERROR: invalid input')