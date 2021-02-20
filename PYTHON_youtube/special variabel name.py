print(__name__) #this shows the strating point of execution, the module that starts with this is the strating point


#use the below if you want to greet the user first at the begining of the program
def main():
    print('hello')
    print('welcome user')

if __name__ == '__main__':   #this is used when we want the module to be executed as a whole only
                             # when the module is indually tun
    main()