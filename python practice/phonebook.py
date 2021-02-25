n= int(input())#the length of the phonebook
name=[]
phone_num=[]
for i in range(0,n):
    num= input()
    num = num.split()
    phone_num.append(num[-1])
    name.append(num[0])
phonebook= dict(zip(name,phone_num))
print(phonebook)
enter= input('')
if enter in phonebook:
    a= phonebook.get(enter)
    print(f'{enter} = {a}')
else:
    print('Not found')
          