list1=[]
n=int(input('enter the length: '))
for i in range (0,n):
    e=int(input('enter the next number: '))
    list1.append(e)

#list1= [10,21,4,45,66,93,1]

def count(list1):
    even_count, odd_count = 0, 0
    for num in list1:
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1
    print(even_count,odd_count)

count(list1)
