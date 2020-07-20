import mysql.connector

class DbConnection:
    mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="news")
    mycursor = mydb.cursor()

    def checkDbConnection(self):
        if self.mydb:
            print("Connection Successful")
        else:
            print("Connection lost")

    def createTables(self):
        query = "CREATE TABLE IF NOT EXISTS `news_detail` (`id` int(11) NOT NULL auto_increment," \
             "`section` varchar(255) NOT NULL default '0'," \
             "`title` text NOT NULL ," \
             "`abstract` text ," \
             "`byline` varchar(255)  ," \
             "`item_type` varchar(255) ," \
             "`source` varchar(255) ," \
             "`published_date` datetime ," \
             "`material_type_facet` varchar(255) NOT NULL ," \
             "`counter` int(11) NOT NULL ," \
             " PRIMARY KEY  (`id`)" \
             " );"
        self.mycursor.execute(query)

    def createTesttable(self):
        query = "CREATE TABLE IF NOT EXISTS `test_table` (`id` int(11) NOT NULL auto_increment," \
                "`firstName` varchar(255) NOT NULL default '0'," \
                "`MiddleName` text NOT NULL ," \
                "`LastName` text ," \
                "`Address` varchar(255)  ," \
                " PRIMARY KEY  (`id`)" \
                " );"
        self.mycursor.execute(query)

    def insertTestdata(self):
        query = "INSERT INTO `test_table` ( `firstName`,`MiddleName`,`LastName`,`Address` ) " \
                " VALUES ('JACK','NONE','WILSON','LONDON') " \
                " ;"

        self.insertData(query)


    def deleteTable(self, tableName):
        query = " DROP TABLE %s " %(tableName)
        self.mycursor.execute(query)

    def truncateTable(self,tableName):
        query = "TRUNCATE %s" %(tableName)
        self.mycursor.execute(query)

    def insertData(self,query):
        self.mycursor.execute(query)
        self.mydb.commit()

        return True

class MyKafka:
    HOST_NAME = "localhost:9092"
    TOPIC_NAME = "KafkaTutorial"

obj = DbConnection()
#obj.deleteTable("news_detail")
#obj.createTables()
obj.truncateTable("news_detail")
#obj.createTesttable()
#obj.insertTestdata()


