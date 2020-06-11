
# Substtract 30 day from current month

from datetime import datetime, timedelta

class SubDays:
    def SubstractDay(self):
        dt = datetime.today() - timedelta(30)
        print(dt)
               
myobj = SubDays()            
myobj.SubstractDay()