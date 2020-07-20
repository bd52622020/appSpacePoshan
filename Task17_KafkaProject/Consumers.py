from flask import Flask, render_template, Response
from pykafka import KafkaClient
import con
import json
from result import Result
import pandas as pd
import matplotlib.pyplot as plt

global_df = " "
def get_kafka_client():
    return KafkaClient(hosts=con.MyKafka.HOST_NAME)

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

#Consumer API
@app.route('/topic/<topicname>')
def get_messages(topicname):
    client = get_kafka_client()

    def events():
        for i in client.topics[topicname].get_simple_consumer():
            yield 'data:{0}'.format(i.value.decode())
            message = i.value.decode()
            print(type(message))
            json_array = json.loads(message)
            print(json_array["section"])
            print(json_array["title"])
            columns = ', '.join("`" + x.replace('/', '_') + "`" for x in json_array.keys())
            values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in json_array.values())
            query = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('news_detail', columns, values)
            print((query))
            obj = con.DbConnection()
            obj.insertData(query)
    return Response(events(), mimetype="text/event-stream")

@app.route('/result')
def get_result():
    data = Result()
    mydata = data.Db()
    dfplot = mydata.groupby("section").sum("counter").sort("section")
    x = dfplot.toPandas()["section"].values.tolist()
    y = dfplot.toPandas()["sum(counter)"].values.tolist()
    plt.bar(x, y)
    plt.savefig('/home/poshan/PycharmProjects/untitled/img/new_plot.png')
    return render_template('result.html', dfs = mydata.collect())

@app.route('/reports')
def get_chart():
    data = Result().myReports()
    return render_template('reports.html', df = data.collect())

if __name__ == '__main__':
    app.run(debug=True, port=5001)