import os
import sqlite3 as lite
import sys

class AppRun(object):
    def display_title(self):
        os.system('cls')
        print("\t+++++++++++++++++++++++++++++++++")
        print("\t+++++++++++++++++++++++++++++++++")
        print("\t+++++++++ Group 4A ++++++++++++++")
        print("\t+++++++++ Learning Map ++++++++++")
        print("\t+++++++++++++++++++++++++++++++++")
        print("\t+++++++++++++++++++++++++++++++++")

    def user_command(self):
        print("Press[1] to add a user")
        print("Press[2] to view all available skills")
        print("Press[3] to add a skill")
        print("Press[4] to update skills")
        print("Press[5] view studied and unstudied skills")
        print("Press[6] to view progress")
        print("\npress 'q' to quit!")
        selection = input("\nEnter 1,2,3 or 4 \n")
        return selection

# Main app part
app = AppRun()
app.display_title()
selection = app.user_command()

while selection != 'q':

    app.display_title()
    if selection == 1:
        print("Add User:\n")
        # display_events()
        input("Press Enter to continue")

    elif selection == 2:
        def see_skills():

            con = lite.connect('team.db')

            with con:
                con.row_factory = lite.Row

                cur = con.cursor()
                cur.execute("SELECT * FROM skills")

                rows = cur.fetchall()

                for row in rows:
                    print ("{} {}".format(row["skillid"], row["skillname"]))
                    # print("A list of all the available skills \n")
        # app.display_last_event()
        input("Press Enter to continue")

    elif selection == 3:
        def add_skill():
            your_name = input("Type your name")
            skill_to_add = input("Type one of this skills: php,python,javascript,css,html,c++,c,java,perl")

            if skill_to_add == "php":
                sid = 1
            if skill_to_add == "python":
                sid = 2
            if skill_to_add == "javascript":
                sid = 3
            if skill_to_add == "css":
                sid = 4
            if skill_to_add == "html":
                sid = 5
            if skill_to_add == "c++":
                sid = 6
            if skill_to_add == "c":
                sid = 7
            if skill_to_add == "java":
                sid = 8
            if skill_to_add == "perl":
                sid = 9

            con = lite.connect('team.db')

            with con:

                con.row_factory = lite.Row

                cur = con.cursor()
                cur.execute("SELECT * FROM user WHERE name = 'your_name'")

                rows = cur.fetchall()

                for row in rows:
                    id = row["userid"];

                cur.execute("INSERT INTO userskill(user_id, skill_id, status) VALUES ('id','sid',0)")
                print('Done')
        # print("Add a skill to be learned")
        # add_event()
        input("Press Enter to continue")

    elif selection == 4:
        print("Update skills here\n")
        # app.display_last_event()
        input("Press Enter to continue")

    elif selection == 5:
        print("A list of all the studied and unstudied skills\n")
        # app.display_last_event()
        input("Press Enter to continue")

    elif selection == 6:
        print("Progress is \n")
        # app.display_last_event()
        input("Press Enter to continue")

    else:
        print("Invalid choice try again\n")
    selection = app.user_command()
