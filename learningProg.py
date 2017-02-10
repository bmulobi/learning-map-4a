import sqlite3
connection = sqlite3.connect("team.db")

cursor = connection.cursor()

uid = input("Enter User ID: ")
uid = int(uid)

learntSkills_command  = "SELECT COUNT(user_id) FROM userskill WHERE user_id =  '%s' AND status = 1;" % (uid)
cursor.execute(learntSkills_command)
learntSkills = cursor.fetchall() 

allSkill_command  = "SELECT COUNT(user_id) FROM userskill WHERE user_id =  '%s';" % (uid)
cursor.execute(allSkill_command)
allSkills = cursor.fetchall() 

print ("\n-------------------------------")
print ("User ", uid, "learning progress")
print ("-------------------------------")


if len(learntSkills) == 0 and len(allSkill_command) > 0:
	print ("You have completed 0/", allSkill_command[0], " skills")
elif len(learntSkills) != 0 and len(allSkill_command) > 0:
	print ("You have completed", learntSkills[0] , "/", allSkills[0], " skills")
elif len(allSkill_command) == 0:
	print ("Please add skills or check if user is added")
else:
	print("\n\nPlease enter 0 or 1 for skill status")

cursor.close()
connection.close()
