import requests
from pprint import pprint
import mysql.connector
import json

 

url = "https://api.deezer.com/chart/0/tracks?index=0&limit=50"
r = requests.get(url)
 
data = r.text
parsed = json.loads(data)
print(json.dumps(parsed, indent=4))

 
mydb = mysql.connector.connect(
  host="sql5.freemysqlhosting.net",
  user="sql5455004",
  password="X7ASR8ST4w",
  database="sql5455004"
)
 
print(mydb)
 
mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)


for i in parsed['data']:
  print(i['position'])
  print(i['title'])
  print(i['album']['title'])
  print(i['artist']['name'])
  print(i['artist']['link'])
  
  position = i['position']
  track_title = i['title']
  album_title = i['album']['title']
  artist_name = i['artist']['name']
  artist_link = i['artist']['link']
  
  sql = "INSERT INTO deezer (position, track_title, album_title, artist_name, artist_link) VALUES (%s, %s, %s, %s, %s)"
  val = (position, track_title, album_title, artist_name, artist_link)
  mycursor = mydb.cursor()
  mycursor.execute(sql, val)
  mydb.commit()

    
 
    
 
 
   
    
 
 
   
 
