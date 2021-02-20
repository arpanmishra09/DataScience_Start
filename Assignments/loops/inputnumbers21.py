lst = []
i=0
n=0
# iterating till the range
while True :
    ele = input('enter next number')
    if not ele.isalpha():
        lst.append(ele)
    else:
        print('not a number')
        n+=1

print(lst)