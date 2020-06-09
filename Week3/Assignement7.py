'''
Created on Jun 9, 2020

@author: Poshan
'''
import math
from _ast import Try
from IPython.external.qt_loaders import import_pyside2
class Checkspeed:
    speed = 0
    points = 0
    def mySpeed(self, speed):
        print(speed)
        if(speed > 70):
            extratSpeed = speed - 70
            points = math.ceil(extratSpeed/5)
            if points > 12:
                print("License suspended")
            else:
                print("Your Demerit point is :", points)
            
        else:
            print("You are driving Ok")
            
import os
class ReadFile():
    
    def fileRead(self):
        try:
            filesize = os.path.getsize("demo.txt")
            if filesize == 0:
                print("The file is empty : " + str(filesize))
            else:
                print("This file contains some information : " + str(filesize))
                        
            f = open("demofile.txt", "r")
            print(f.read(10))
        except:
            print("The File Does not Exist")
        
       

class RangeOfThirdEdge:
    def findTheSide(self, side1, side2):
        highValue = 0
        lowValue = 0
        if side1 >= side2:
            highValue = side1 + side2
            lowValue = side1 - side2
            
        else:
            highValue = side2 + side1
            lowValue = side2 - side1
            
        for i in range(lowValue + 1, highValue):
            print("The range of Third edge is :", i)
    
    
    
class FootBallTeam:
    tName = "Unkonwn "
    nWins = 0
    nLoss = 0
    nDraw = 0
    def teamName(self):
        self.tName = input("Enter the name of the Team: ")
        self.nWins = int(input("Enter the no of wins: "))
        self.nDraw = int(input("Enter the no of draw: "))
        self.nLoss = int(input("Enter the no of loss: "))
        
        self.totalPoints()
        
    def totalPoints(self):
        totalWinninfPoint = self.nWins * 3
        totalDrawPoint = self.nDraw * 1
        
        overallPoints = totalWinninfPoint + totalDrawPoint
         
        print("Win :" , totalWinninfPoint)
        print("Draw :" , totalDrawPoint)
        print("loss :", self.nLoss)
        print("overallPoints :" , overallPoints)
         
        tauntDict = {"Taunt1": "!! This team is not made for playing football !!",
                     "Taunt2": "You Suck"}
        BadDict = {"Bad Comments1": "!! This team is not doing their best !!",
                  "Bad Comments2": "The management of team is a failure"}
        
        GoodDict = {"Good Comments1": "!! Bravo, keep it up !!",
                  "Good Comments2": "Amazing Performance, this team is a legend"}
        
        if overallPoints >= 1000:
            if overallPoints >= 1200:
                comment = GoodDict.get("Good Comments1")
            else:
                comment = GoodDict.get("Good Comments1")
         
        elif overallPoints >= 700:  
            if overallPoints >= 900:
                comment = BadDict.get("bad Comments1")
            else:
                comment = BadDict.get("bad Comments1")
        else:
            comment = tauntDict.get("Taunt2")
            
        print(comment)

    
       
         
obj1 = Checkspeed()
obj1.mySpeed(70)  

obj2 = ReadFile()
obj2.fileRead() 

obj3 = RangeOfThirdEdge()
obj3.findTheSide(10, 30) 

obj4 = FootBallTeam()
obj4.teamName()       
        
            
            
    