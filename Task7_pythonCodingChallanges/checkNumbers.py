class GetNumbers:
    
    def getNo(self):
         
         myList = [2,3,5,8,1,2]
         firstNo = myList[0]
         lastNo = myList[-1]
         
         if firstNo == lastNo:
             print("Numbers are equals")
         else:
             print("Numbers are not equals")
  
             
obj4 = GetNumbers()
obj4.getNo()