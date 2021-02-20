a = int(input('enter the number'))
for i in range (2,a):
    if a%i==0:
        print('it is not a prime number')
        break
else:
    print('it is a prime number')