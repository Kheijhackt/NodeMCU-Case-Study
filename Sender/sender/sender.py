# Import modules
import urllib.request
import pymysql

# Declarations
url = "http://192.168.1.103/"
lastData = ""

# Functions
def getData():
    
    n = urllib.request.urlopen(url).read()
    n = n.decode("utf-8")
    
    return n
    
def sendToDatabase(signal1, signal2, signal3, signal4):
    db = pymysql.connect(
        host = "sql6.freemysqlhosting.net",
        user = "sql6496157",
        password = "VScNHRCZqQ",
        database = "sql6496157",
        port = 3306
    )
    cursor = db.cursor()
    insert = """INSERT INTO cpe101_case_study_g3
                (signal1, signal2, signal3, signal4)
                VALUES ({}, {}, {}, {})""".format(signal1, signal2, signal3, signal4)
    cursor.execute(insert)
    db.commit()
    return True

# Main loop
while(True):
    data = getData()

    if(lastData != data):
        print("Data sent: " + data)
        send = data.split('|')
        sendToDatabase(int(send[0]), int(send[1]), int(send[2]), int(send[3]))
    lastData = data
