x, y, z = int((input('enter the first number'))),int((input('enter the second number'))),int((input('enter the third number')))
if x>y and x>z:
       print('the greatest number:')
       print(x)
elif y>x and y>z:
    print('the greatest number:')
    print(y)
else:
    print('the greatest number:')
    print(z)