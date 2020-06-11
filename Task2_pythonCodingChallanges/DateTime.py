'''
Created on 1 Jun 2020

@author: poshan
'''
from datetime import datetime, timedelta
import string

class DateAndTime:
    dateValue =  datetime.now()
#     today = datetime.now()
    currentYear = dateValue.year
    currentMonth = dateValue.month
    monthOfYear = dateValue.strftime("%B")
    weekOfYear = dateValue.strftime("%U")
    weekdayOfweek = dateValue.strftime("%w")
    dayOfyear = dateValue.strftime("%j")
    dayOfMonth = dateValue.strftime("%d")
    dayOfweek = dateValue.strftime("%A")
    
              
        
myObj = DateAndTime()
print("Current Date and time: ", myObj.dateValue)
print("Current Year :", myObj.currentYear )
print("Current Month: ", myObj.currentMonth)
print("Month of the year: ", myObj.monthOfYear)
print("Week of the year: ", myObj.weekOfYear)
print("week day of the year: ", myObj.weekdayOfweek)
print("day of the year: ", myObj.dayOfyear)
print("day of the Month: ", myObj.dayOfMonth)
print("day of the Week: ", myObj.dayOfweek)









