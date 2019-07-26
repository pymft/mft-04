import sqlite3


path = "C:/Users/Student/Downloads/chinook.db"
conn = sqlite3.connect(path)

rows = conn.execute("""
SELECT * from tracks AS t 
JOIN albums AS a ON t.albumId = a.albumid
Join artists AS s ON a.ArtistId = s.ArtistId
""")

for row in rows:
    print(row )