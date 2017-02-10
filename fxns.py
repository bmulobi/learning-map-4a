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
        
def see_skills():

    
    
    con = lite.connect('team.db')
    
    with con:

        con.row_factory = lite.Row
           
        cur = con.cursor() 
        cur.execute("SELECT * FROM skills")

        rows = cur.fetchall()

        for row in rows:
            print ("{} {}".format(row["skillid"], row["skillname"]))        