from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaClient
import urllib.request
from numpy import array
import requests
import pprint
import json
import mysql.connector
from datetime import datetime

# app_url = urllib.request.urlopen("https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=7r1u7ZUeGhA8VKvOGyJKO7kOu9VRbsUB")
app_url = requests.get(
    "https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=7r1u7ZUeGhA8VKvOGyJKO7kOu9VRbsUB")
json_array = app_url.json()

filteredData = json_array["results"]


def validate_string(val):
    if val != None:
        if type(val) is int:
            # for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


def consuemMyData(message):
    json_array = json.loads(message)
    print(json_array["section"])
    print(json_array["title"])
    columns = ', '.join("`" + x.replace('/', '_') + "`" for x in json_array.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in json_array.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('news_detail', columns, values)
    print((sql))
    mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="news")
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    # if :
    #     print("Data inserted successfully")
    # else:
    #     print("Data insertion failed")

    # for keys, values in json_array.items():
    #     print(keys)
    #     print(values)
    # for key in keys:
    #     columns = " ,".join("'" + key + "'")

    # columns = ', '.join("`" + x.replace('/', '_') + "`" for x in keys())
    # values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
    # sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)

    for k, v in json_array.items():
        section = v


myData = {}
message = []


def generate_data(filteredData):
    for data in filteredData:
        myData["section"] = data["section"]
        myData["title"] = data["title"]
        myData["abstract"] = data["title"]
        myData["byline"] = data["byline"]
        myData["item_type"] = data["item_type"]
        myData["source"] = data["source"]
        # myData["published_date"] = data["published_date"]
        d1 = data["published_date"].replace("T", " ")[0:19]
        myData["published_date"] = d1  # datetime.strptime( d1, '%Y-%m-%d %H:%M:%S')
        # print(mydate)
        myData["material_type_facet"] = data["material_type_facet"]
        # myData["geo_facet"] = data["geo_facet"]
        message = json.dumps(myData)
        consuemMyData(message)


generate_data(filteredData)
