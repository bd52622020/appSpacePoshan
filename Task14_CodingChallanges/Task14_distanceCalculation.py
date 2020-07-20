'''
Created on Jun 18, 2020

@author: Poshan
'''
import math
class DistanceCalculation:
    
    def getLatitudeAndLongitude(self):
        latitudeFrom = input("Enter Latitude Origin :" ) 
        longitudeFrom = input("Enter Longitude Origin :" )
        
        latitudeTo = input("Enter Latitude Destination :" ) 
        longitudeTo = input("Enter Longitude Destination :" )
        
        radius = 6371
        
        dlat = math.radians(latitudeTo-latitudeFrom)
        dlon = math.radians(longitudeTo-longitudeFrom)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitudeFrom)) \
        * math.cos(math.radians(longitudeTo)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c
        
        print(d)
        
obj = DistanceCalculation()
obj.getLatitudeAndLongitude()
        
