nums = [12,2,18,21,26]
for  num in nums:
    if num%5 ==0:
        print(num)
        break
else:
    print('not found')
#break is a must in for else loop.
#when else is used in this case for if then the output will be printed 5 time so we use it with for