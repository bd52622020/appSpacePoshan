from kafka import KafkaConsumer
import json
import con
#import Db

class Consumer:

    def consumer_data(self):
        consumer = KafkaConsumer(
            con.MY_TOPIC,
            bootstrap_servers=con.MY_SERVER,
            auto_offset_reset='earliest',
            group_id=con.GROUP_ID)
        print("starting the consumer")
        counter = 0

        for msg in consumer:
            counter += 1
            print("Message Consumed", counter)
            message = msg.value.decode()
            json_array = json.loads(message)
            columns = ', '.join("`" + x.replace('/', '_') + "`" for x in json_array.keys())
            values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in json_array.values())
            query = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('pos_tbl', columns, values)
            print(query)
            #Db.DbConnection().insertData(query)



    def test(self):
        print("Test")


if __name__ == "__main__":
    Consumer().consumer_data()



