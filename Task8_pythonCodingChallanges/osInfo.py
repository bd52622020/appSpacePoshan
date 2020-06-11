'''
Created on Jun 11, 2020

@author: Poshan
'''
import platform
import sys


class MyOsInfo:
    
    def myPlatForm(self):
        try:
            print(platform.platform())
            print("OS : ", platform.system())
            print("Release : ", platform.release())
            print("Version ", platform.version())
            print("MAC : ", platform.mac_ver())
            print("U name : ", platform.uname())
        except:
            return "N/A"
    

obj = MyOsInfo()
obj.myPlatForm()  