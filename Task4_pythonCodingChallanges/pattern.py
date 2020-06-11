'''
Created on 3 Jun 2020

@author: poshan
'''
import re

pattern = "^We.*Data$"
txt = "We love programming with Big Data"
if re.search(pattern,txt):
    print(pattern+ " Match Found")
else:
    print("Match Not Found")