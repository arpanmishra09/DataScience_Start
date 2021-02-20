class A:
    def feature1(self):
        print('f1')

    def feature2(self):
        print('f2')
#single level inheritance
class B(A): #by this the class b will inherit all featres of class A which makes B a sub class and A super class
    def feature3(self):
        print('f3')

    def feature4(self):
        print('f4')
#2nd level
class C(B): #now C has features of both A and B as B had inherited a's properties: multilevel
#if b had not inherited A then the same thing could had been done by writing class C(A,B) thus giving C both A and B features: multiple
    def feature5(self):
        print('f1')

    def feature5(self):
        print('f2')

a1= A()


a1.feature1()
a1.feature2()
b1 = B()
b1.feature1()  #now though b1 is an object of B it can also use features of A since B has inherited A

