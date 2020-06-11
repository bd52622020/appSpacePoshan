'''
Created on 31 May 2020

@author: poshan
'''

class ModifyExcelFile:
    import csv
    file_name = "file_name.csv"
    f = open("New File", "a")
    with open(file_name,"r") as file:
        csv_reader = csv.reader(file,delimiter = ',')
        for line in csv_reader:
            newLine = line[2].replace("*", "-")
            f.write(newLine + '\n')
    f.close()
