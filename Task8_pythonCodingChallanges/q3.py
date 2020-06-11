'''
Created on Jun 11, 2020

@author: Poshan
'''
class ConcatenateDectioanry:
    
    def concat(self):
        a = {1:10, 2:20}
        b = {3:30, 4:40}
        c = {5:50, 6:60}
        
        result = {**a, **b, **c}
        
        print(result)
        
        
obj = ConcatenateDectioanry()
obj.concat()        