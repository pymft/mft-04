import sqlite3


conn = sqlite3.connect("bmi.sqlite")

conn.execute("""
CREATE TABLE IF NOT EXISTS bmi 
( NAME TEXT NOT NULL,
HEIGHT REAL NOT NULL,
WEIGHT REAL NOT NULL);
""")


conn.execute("""
INSERT INTO bmi (NAME, HEIGHT, WEIGHT) VALUES ('Asghar', 1.8, 90);
""")

conn.commit()