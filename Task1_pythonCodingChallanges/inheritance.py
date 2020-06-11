'''
Created on 31 May 2020

@author: poshan
'''
# Inheritance

class Humans:
    firstName = ""
    lastName = ""
    
    def generalInfo(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def __str__(self):
        return self.firstName + " " + self.lastName

class Student(Humans):
    nickName = ""
    
    def personalInfo(self, nickName):
        self.nickName = nickName
        
    def __str__(self):
        return "This is a student info: " + super().__str__() + " " + self.nickName
        
    
class Researcher(Humans):
    subjects = " "
    
    def personalInfo(self, subjects):
        self.subjects = subjects
        
    def __str__(self):
        return "This is a Researcher info: " + super().__str__() + " " + self.subjects
    
    
myObj = Student()
myObj.generalInfo("John", "Steve")
myObj.personalInfo("Johny")
myObj2 = Researcher()
myObj2.generalInfo("Albert", "Einstein")
myObj2.personalInfo("Pyhysics, Chemistry, Mechanical, Electrical")
print(myObj.__str__())
print(myObj2.__str__())    