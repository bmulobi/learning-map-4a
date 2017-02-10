import sqlite as lite
import sys

def view_studied_skills(user_id){
	con = lite.connect("team")
	with con:
		cur = con.cursor()
		sql = "SELECT * FROM user_skills WHERE userid="+user_id+"AND status=1"
		cur.execute(sql);

		rows = cur.fetchall()

		for row in rows:
			print(row)
}
def view_unstudied_skills(user_id){
	con = lite.connect("team")
	with con:
		cur = con.cursor()
		sql = "SELECT * FROM user_skills WHERE userid="+user_id+"AND status=1"
		cur.execute(sql);

		rows = cur.fetchall()

		for row in rows:
			print(row)
}