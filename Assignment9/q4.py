'''
Created on Jun 11, 2020

@author: Poshan
'''

    

def checkKey(dict, key): 
       
    if key in dict: 
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 
   
# Driver Code 
dict = {1: 10, 2:20, 3:30, 4:40, 5:50, 6:60} 
   
key = 1
checkKey(dict, key) 
   
key = 7
checkKey(dict, key)    