import os
import sqlite3 as lite
import sys
from view_skills import *
from learningProg import *
from update_skill_status import *
from fxns import *

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
        print("Press[5] view studied skills")
        print("Press[6] view unstudied skills")
        print("Press[7] to view progress")
        print("\npress 'q' to quit!")
        selection = input("\nEnter 1,2,3,4,5,6 or 7\n")
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
        print("A list of all the available skills \n")
        # app.display_last_event()
        input("Press Enter to continue")

    elif selection == 3:
        print("Add a skill to be learned")
        # add_event()
        input("Press Enter to continue")

    elif selection == 4:
        print("Update skills here\n")
        # app.display_last_event()
        input("Press Enter to continue")

    elif selection == 5:
        print("A list of all the studied skills\n")
        id= input("Enter User ID")
        view_studied_skills(id)
       # app.display_last_event()
        input("Press Enter to continue")

    elif selection == 6:
        print("A list of all the unstudied skills\n")
        id = input("Enter User ID")
        view_studied_skills(id)
        # app.display_last_event()
        input("Press Enter to continue")

    elif selection == 7:
        # learningProgress
        # print("Progress is \n")
        # app.display_last_event()
        input("Press Enter to continue")



    else:
        print("Invalid choice try again\n")
    selection = app.user_command()
