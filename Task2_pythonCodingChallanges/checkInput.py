# check whether the input contains characterm number or _

import re

class MatchChar:
    
    def myChar(self, myInput):
        
        pattern1 = re.compile('[a-z]+')
        pattern2 = re.compile('[A-Z]+')
        pattern3 = re.compile('[0-9]+')
        pattern4 = re.compile('_+')
        
        if(pattern1.match(myInput) or pattern2.match(myInput) or pattern3.match(myInput) or pattern4.match(myInput)):
            print("Valid input")
        else:
            print("Invalid Input")
        
                
myObj = MatchChar()
myObj.myChar("_")