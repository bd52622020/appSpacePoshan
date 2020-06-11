import math

class Checkspeed:
    speed = 0
    points = 0
    def mySpeed(self, speed):
        print(speed)
        if(speed > 70):
            extratSpeed = speed - 70
            points = math.ceil(extratSpeed/5)
            if points > 12:
                print("License suspended")
            else:
                print("Your Demerit point is :", points)
            
        else:
            print("You are driving Ok")
            
obj1 = Checkspeed()
obj1.mySpeed(70)  