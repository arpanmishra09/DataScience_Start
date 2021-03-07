s= input('enter your name')
a= s.split(' ')
b=[]
c=''
print(a)
for i in a:
    a= i.capitalize()
    b.append(a)

for ele in b:
        if ele.isalpha():
            c+= ele+' '

