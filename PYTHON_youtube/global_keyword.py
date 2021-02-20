b = 5 #global variable
def some():
    a = 15 #local variable, this cannot be acessed outside the function
           # but a global variable cab be accessed inside the function
           #if we want to change the value of global variable then we need to mention 'global a' separately
           #to us local and global variable together in a function use global i.e. x=globals()['a']
    print(a)
print(b)