import sqlite3 as lite
import sys

def view_studied_skills(user_id):
	con = lite.connect("team.db")
	with con:
		cur = con.cursor()
		sql = "SELECT * FROM userskill WHERE user_id={} AND status=1".format(user_id)
		cur.execute(sql);

		rows = cur.fetchall()

		for row in rows:
			print(row)
			
def view_unstudied_skills(user_id):
    con = lite.connect("team.db")
    with con:
	    cur = con.cursor()
	    sql = "SELECT * FROM userskill WHERE user_id={} AND status=0".format(user_id)
	    cur.execute(sql);

	    rows = cur.fetchall()

	    for row in rows:
		    print(row)
