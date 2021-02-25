lst=[]
i=0
n=0

def load(b): #to check whethe the input is a digit
    global n

    if b.isdigit():
        lst.append(b) # adding the element
    else:
        n += 1
        print('not a number')
        to_user(n,lst)


def to_user(m,m1):#number of tries
   if m<=3:
       user()
   else:
       print('exit')
       begin(m1)



def check(ele):# check for negative and decimal inputs
    if '.' in ele:
        a= ele.replace('.','',1)
        load(a)
    elif '-' in ele:
        b= ele.replace('-', '', 1)
        load(b)
    else:
        load(ele)

def user(): #user input

    while i == 0:
        ele = input('enter next number')

        check(ele)


def begin(lst):
    print(lst)
    exit()


print('enter any alphabet 4 times to print the list')
user()