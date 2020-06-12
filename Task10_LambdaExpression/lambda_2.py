'''
Created on Jun 12, 2020

@author: Poshan
'''
class Lambda2:
    
    def ValueDetections(self):
        
        mylist =[2,3,4,6,7,19,13]
        
        for i in mylist:
            
            x = lambda i: i % 19 == 0 or i % 13 == 0
            print(i, "is divisible by by 19 or 13", x(i))
            

obj = Lambda2()
obj.ValueDetections()

