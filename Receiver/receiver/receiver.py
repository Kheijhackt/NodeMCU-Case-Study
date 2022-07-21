import urllib.request
import http
import mysql.connector
from time import sleep

base = "http://192.168.1.100/" # EDIT

def transfer(data1):
    try:
        n = urllib.request.urlopen(base + data1).read()
        n = n.decode("utf-8")
        return n

    except http.client.HTTPException as e:
        return e
    
def receiveFromDatabase():
    db = mysql.connector.connect(
        host = "sql6.freemysqlhosting.net",
        user = "sql6496157",
        password = "VScNHRCZqQ",
        database = "sql6496157",
        port = 3306
    )
    cursor = db.cursor()
    select = """SELECT * FROM cpe101_case_study_g3 ORDER BY timeStamp DESC
                    LIMIT 1"""
    cursor.execute(select)
    retrieve = cursor.fetchone()
    return retrieve

while(True):
    received = receiveFromDatabase()
    
    transfer(str(received[1]))
    transfer(str(received[2]))
    transfer(str(received[3]))
    transfer(str(received[4]))
        