'''
Created on Jun 18, 2020

@author: Poshan
'''
import statistics
from statistics import stdev
class standardDeviationResult:
    def calculate(self):
        data = [4, 2, 5, 8, 6]
        standardDeviationResult = stdev(data)
        
        print("The standard Deviation of of gieven data is : " , standardDeviationResult)
        
obj = standardDeviationResult()
obj.calculate()