
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

obj3 = RangeOfThirdEdge()
obj3.findTheSide(10, 30) 