import sqlite3 as lite
import sys

try:
    con = lite.connect('team.db')
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print ("SQLite version:{}".format(data))                
    
except lite.Error:
    
    print("Error {0}:".format(e.args[0]))
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
    

