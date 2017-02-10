import os, time ,sqlite3

conn = sqlite3.connect('team.db')


#user_id=input("") #Enter id

print("Enter Name")
user_id=input("") # Enter name
print("User ID")

user_name=input("") # Enter name

conn = sqlite3.connect('team.db')
conn.execute("INSERT INTO user VALUES ('%s','%s');" % (user_name,user_id))

print("Success")

conn.commit()
