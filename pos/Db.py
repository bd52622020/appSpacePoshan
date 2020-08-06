import mysql.connector

class DbConnection:
    mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="pos_db")
    mycursor = mydb.cursor()

    def checkDbConnection(self):
        if self.mydb:
            print("Connection Successful")
        else:
            print("Connection lost")

    def create_table_content(self):
        query = "CREATE TABLE IF NOT EXISTS `pos_tbl` (`id` int(11) NOT NULL auto_increment," \
             "`p_id` varchar(60) NOT NULL default '0'," \
             "`common_name` text NOT NULL ," \
             "`abstract` text ," \
             "`seriousness` varchar(255)  ," \
             "`item_type` varchar(255) ," \
             " PRIMARY KEY  (`id`)" \
             " );"
        self.mycursor.execute(query)



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


#obj = DbConnection()
#obj.deleteTable("news_detail")
#obj.createTables()
#obj.create_table_content()
#obj.truncateTable("news_detail")
#obj.createTesttable()
#obj.insertTestdata()


