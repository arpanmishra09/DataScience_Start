fiveteen= []
not_fiveteen=[]
n= int(input('enter the length of the list'))
for i in range (0,n):
    e= int(input('enter the next numnber'))
    if e%15==0:
        fiveteen.append(e)
    else:
        not_fiveteen.append(e)

print(fiveteen)
print(not_fiveteen)