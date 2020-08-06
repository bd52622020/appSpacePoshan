from kafka import KafkaProducer
import json
import time
import con
from api_con import ApiCon


class Producers:

    def get_api_data(self):
        producer = KafkaProducer(bootstrap_servers=[con.MY_SERVER])
        raw_data = ApiCon().get_api()
        filtered_data = raw_data
        myData = {}
        for data in filtered_data:
            myData["p_id"] = data["id"]
            myData["common_name"] = data["common_name"]
            myData["seriousness"] = data["seriousness"]
            print(myData)
            new_data = json.dumps(myData, sort_keys=True, indent=3)
            producer.send(con.MY_TOPIC,new_data.encode("utf-8"))
            time.sleep(2)


if __name__ == "__main__":
    Producers().get_api_data()

# obj = Producers()
# obj.get_api_data()
    # if __name__ == "__main__":
    #     get_api_data(self="")

