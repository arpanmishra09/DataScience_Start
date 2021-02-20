class Computer:

    def __init__(self):
        self.name= 'Navin'
        self.age= 28

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1= Computer()
c2= Computer()
c1.age = 30
print(c1.name)
print(c2.age)

if c1.compare(c2):
    print('yes')
else:
    print('no')
