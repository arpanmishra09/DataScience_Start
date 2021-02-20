class student:

    school = 'telusko'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  #instance variable
        return (self.m1+self.m2+self.m3)/3

    @staticmethod
    def info():
        print('static method')

    @classmethod   #decorator
    def school_name(cls):   #whenever we want to access class variables we use cls
        return cls.school


s1 = student(23,56,78)
s2 = student(45,7,89)

print(s1.avg())
print(student.school_name())
#when methods or functions deal with class its called class menthods and when they deal with instance variables they are known as
#instance variable

