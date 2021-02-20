class student():

    def __init__(self,name,rollno):
        self.name= name
        self.rollno = rollno
        self.lap = self.laptop

    def show(self):
        print(self.name,self.rollno)

    class laptop():

        def __init__(self):
            self.brand ='hp'
            self.cpu='i3'
            self.ram=8




s1= student('Naevin',2)
s2= student ('genny', 5)

s1.show()
lap1 = student.laptop #can be called the inner in both ways
lap2= s2.lap
print(id(lap1))
print(id(lap2))