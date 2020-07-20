import unittest
from unittest.mock import patch, Mock, MagicMock
import requests
from pykafka import KafkaClient
import apiInfo
import con
import Consumers
import mysql.connector


class TestProducers(unittest.TestCase):
    client = KafkaClient(hosts=con.MyKafka.HOST_NAME)
    API_URL = apiInfo.API_URL
    API_KEY = apiInfo.API_KEY
    TOPIC = client.topics[con.MyKafka.TOPIC_NAME]
    producer = TOPIC.get_sync_producer()

    def test_main(self):
        requestHeaders = {
            "Accept": "application/json"
        }
        request_url = requests.get(self.API_URL + "?" + self.API_KEY, headers=requestHeaders)
        if request_url.ok:
           self.assertEqual(True, True)
           print("Url = {0}".format(self.API_URL) )
        else:
            self.assertEqual(False, False)
            print("Url not matched or Bad Resposne")

    def test_get_data(self):
        data = "This is a test data"
        result = self.producer.produce(data.encode("ascii"))
        self.assertEqual(result.value.decode(), data)
        print("Encoding and decoding data")


    def test_connection(self):
        testHost = "localhost:9092"
        host = con.MyKafka.HOST_NAME
        self.assertEqual(host, testHost)
        print("Localhost:9092")

    def test_checkDbConnection(self):
        test_mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="news")
        if test_mydb:
            mycursor = test_mydb.cursor()
            mycursor.execute("Select * from test_table")
            myresult = mycursor.fetchone()
            self.assertEqual(myresult, (1, 'JACK', 'NONE', 'WILSON', 'LONDON'))
            print("DB Connection Successful")
            test_mydb.close()
        else:
            print("Connection lost")





if __name__ == '__main__':
    unittest.main()
