class FindLeapYear:
    
    def getYear(self):
        year = int(input("Enter the year : " ))
        if (year % 4) == 0:
            print(year, " is a leap Year")
        else:
            print(year, "is not a leap year")
            
obj2 = FindLeapYear()
obj2.getYear()