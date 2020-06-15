# Write a map function that returns the squares of the items in the list.
# lst1=[10, 20, 30, 40, 50, 60]

import math
class MapFun:
     
    def square(self, n):
        return math.pow(n,2)
         
    def callMapFun(self):
         
        list1 = [10,20,30,40,50,60]
         
        squareValueofList = map(self.square, list1)
         
        print(list(squareValueofList))
 
obj = MapFun()
obj.callMapFun()