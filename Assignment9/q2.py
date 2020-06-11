'''
Created on Jun 11, 2020

@author: Poshan
'''
class FindRightTriangle:
    
    def getThreeSides(self):
        print("Insert three side of triangle with space:")
        int_num = list(map(int,input().split()))
        side1,side2,side3 = sorted(int_num)
        if side1**2 + side2**2 == side3**2:
            print("The triangle is right angle")
        else:
            print("The triangle is not right angle")
    



obj = FindRightTriangle()
obj.getThreeSides()
        
        