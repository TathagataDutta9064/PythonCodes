#encapsulation
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showData(self):
        print(" Your Name:",self.name)
        print(" Your Age:",self.age)
s1=student("swarnadeep",21)
s2=student("Avisekh",19)
s1.showData()
s2.showData()