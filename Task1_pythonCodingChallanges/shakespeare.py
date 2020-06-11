'''
Created on 27 May 2020

@author: poshan
'''

Words = 0
Lines = 0
vowels = 0
number_value = 0
file_name = "Shakespeare.csv"

with open(file_name, 'r') as file:
    for line in file:
        Words += len(line.split())
        
        for i in line:
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                vowels += 1 
            if i.isdigit() == True:
               
                number_value += 1
                       
        if line:
             Lines += 1
            
           

print ("Number of words :", Words)
print ("Number of Lines :", Lines)
print ("Number of vowels :", vowels)
print ("Total number of Numbers :", number_value)
# 
  