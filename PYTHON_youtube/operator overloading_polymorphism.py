a='a'
b='b'
print(a+b)
print(str.__add__(a,b)) # so here the __add__ is a magic method which works in the background when we use the sign +


#operator overload

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):  #since we cannot add two classes together we created a add function like behind the scene of +
        #and then we add the inputs by assigning them to different variables
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3= Student(m1,m2)
        return (s3)


s1 = Student(58,59)
s2 = Student(60,65)

s3= s1+s2   #behind the scene--> student.__add__(s1,s2)
print(s3.m1)