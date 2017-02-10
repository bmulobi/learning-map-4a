import sqlite3 as lite
import sys


con = lite.connect('team.db')

with con:
    
    cur = con.cursor()    
    
    
    cur.execute("CREATE TABLE IF NOT EXISTS user(userid INTEGER PRIMARY KEY, name TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS skills(skillid INTEGER PRIMARY KEY, skillname TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS userskill(rowid INTEGER PRIMARY KEY,user_id INT, skill_id INT, status INT);")
    
    print("Done")