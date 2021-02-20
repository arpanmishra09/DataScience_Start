n1=float(input('enter the 1st number'))
n2=float(input('enter the 2nd number'))
n3=float(input('enter the 3rd number'))

if n1>n2 and n1>n3:
    print('num1 is greater than num2 and num3')
elif n2>n1 and n2>n3:
    print('num2 is greater than num1 and num3')
elif n3>n1 and n3>n2:
    print('num3 is greater than num1 and num2')
else:
    print('num1,num2,num3 are equal')
