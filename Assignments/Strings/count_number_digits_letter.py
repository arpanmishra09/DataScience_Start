n = input('enter the word')
j=0
for i in range(len(n)):
    if n[i].islower():
        j+=1

print(j)