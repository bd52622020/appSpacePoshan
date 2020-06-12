'''
Created on Jun 12, 2020

@author: Poshan
'''
class myList:
     
    def removeDublicates(self):
        giveList = [0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]
        mylist = list(dict.fromkeys(giveList))
        print(mylist)
         
obj = myList()
obj.removeDublicates()

