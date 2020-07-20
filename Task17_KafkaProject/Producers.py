from time import sleep
from pykafka import KafkaClient
import requests
import json
import apiInfo
import con

class Producers:
    client = KafkaClient(hosts=con.MyKafka.HOST_NAME)
    API_URL = apiInfo.API_URL
    OPENING_DATE = apiInfo.OPENING_DATE
    ORDER_BY = apiInfo.ORDER_BY
    API_KEY = apiInfo.API_KEY
    TOPIC = client.topics[con.MyKafka.TOPIC_NAME]
    producer = TOPIC.get_sync_producer()

    def get_data(self, filtered_data):
        myData = {}
        for data in filtered_data:
            myData["section"] = data["section"]
            myData["title"] = data["title"]
            myData["abstract"] = data["title"]
            myData["byline"] = data["byline"]
            myData["item_type"] = data["item_type"]
            myData["source"] = data["source"]
            d1 = data["published_date"].replace("T", " ")[0:19]
            myData["published_date"] = d1
            myData["material_type_facet"] = data["material_type_facet"]
            myData["counter"] = 1
            new_data = json.dumps(myData, sort_keys=True, indent=3)
            print(new_data)
            self.producer.produce(new_data.encode("ascii"))
            sleep(2)

    def get_api(self):
        requestHeaders = {
            "Accept": "application/json"
        }
        api_url = requests.get(self.API_URL + self.API_KEY, headers=requestHeaders)
        if api_url.ok:
            json_array = api_url.json()
            filtered_data = json_array["results"]
            self.get_data(filtered_data)
        else:
            print('Bad Response!')

obj = Producers()
obj.get_api()