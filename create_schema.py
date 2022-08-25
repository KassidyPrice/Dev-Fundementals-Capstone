import sqlite3

def create_schema():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 with open ('create_schema.txt') as schema:
  query = schema.read()

 # for query in queries:
 cursor.executescript(query)
 connection.commit() 
 return True

create_schema()