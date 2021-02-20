av=10
y= int(input('please enter the required number of candies:'))
i= 1
while i <=y :
    if y > av:
        print('out of stock')
        print('available amount=', av)
        break
    else:
        print('candies')
        i+=1


#pass is used when there is no code to write under a if or else statement or for an empty function and just want to ignore it
#continue is used when we want the loop to continue but the statement below continue to be skipped