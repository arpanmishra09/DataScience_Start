

class computer: # class can contain attributes that is variables and behaviour that is methods(functions)

    def config(self):
        print('i5 16gb 1Tb')


com1 = computer() # this means that now com1 is an object of class computer
com2 = computer()
computer.config(com1) # to use the function in a class we need to use it along with the class name
computer.config(com2)
com1.config()  # another way of calling a function in a class
