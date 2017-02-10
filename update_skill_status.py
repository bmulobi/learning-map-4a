import sqlite3
connection = sqlite3.connect("team.db")

cursor = connection.cursor()

uid = input("Enter User ID: ")
uid = int(uid)

sid = input("Enter the skill ID you want to update: ")
sid = int(sid)

stat = input("Enter 0 for skill NOT studied or 1 for skill studied: ")
stat = int(stat)

if stat == 0 or stat == 1:
	
	#update_command = """UPDATE userskill SET status='stat' WHERE userid = uid AND skillid = sid;"""
	update_command = "UPDATE userskill SET status ='%s' WHERE user_id  = '%s' AND skill_id  = '%s';" % (stat, uid, sid)
	cursor.execute(update_command)

	#cursor.execute("""UPDATE userskill SET status =% WHERE userid = % AND skillid = %;""", (stat, uid, sid))

	#data = (stat, uid, sid)

	select_command  = "SELECT COUNT(user_id) FROM userskill WHERE user_id =  '%s' AND skill_id  =  '%s';" % (uid, sid)
	cursor.execute(select_command)
	result = cursor.fetchall() 

	if len(result) > 0:
		print(len(result), "records updated")
	else:
		print("No records were updated. Check if skill exists for the user")

else:
	print("\n\nPlease enter 0 or 1 for skill status")





