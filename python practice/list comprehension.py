fish1 = ('blowfish', 'catfish','goldfish')
fish_list = [item for item in fish1 if item != 'blowfish']
print(fish_list)

#with operators

number_list= [x**2 for x in range(10) if x%2==0]
print(number_list)

#with two if statements

number_list1= [x**2 for x in range(10) if x%2==0 if x%5==0]
print(number_list1)

#with nested for

number_list2= [x*y for x in range(10) for y in range(3)]
print(number_list2)

