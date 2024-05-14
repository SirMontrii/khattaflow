from datetime import datetime
import time
import numpy as np
import mysql.connector as sql

def execute_query(query):
    try:
        db = sql.connect(host="localhost",
                         user="root",
                         password="1111",
                         auth_plugin = "mysql_native_password",
                         database = "student_society")

        cur = db.cursor()

        cur.execute(query)

        if cur.description is not None:  # Check if the query returns results
            result = cur.fetchall()
            if result:
                for row in result:
                    print(row)
            else:
                print("Empty result set.")
                
        else:
            if query.strip().lower().startswith(("insert", "update", "delete")):
                db.commit()
                print("Query executed successfully.")
            else:
                print("No result set to fetch from.")

        '''result = cur.fetchall()
        if query.strip().lower().startswith("select"):
            result = cur.fetchall()
            if result:
                for row in result:
                    print(row)

        else:
            db.commit()
            print("Query executed successfully: ")'''

        cur.close()

    except Exception as e:
        print("An error occurred: ", e)

    finally:
        if db.is_connected():
            db.close()

        '''result = cur.fetchall()

        for row in result:
            print(row[0])

        cur.close()

        db.close()'''

def main() :
    try:
        query1 = "SELECT Student_name FROM student,enrollment where student.roll_no = enrollment.roll_nO"
        print("Query 1: ")
        execute_query(query1)

    except Exception as e:
        print("An error occurred: ", e)

    try:
        query2 = "select DISTINCT soc_name FROM society"
        print("\nQuery 2: ")
        execute_query(query2)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query3 = "UPDATE society SET mentor_name = 'radha' WHERE soc_name='music'"
        print("\nQuery 3: ")
        execute_query(query3)

    except Exception as e:
        print("An error has occured: ", e)

    
    try:
        query4 = "SELECT * FROM student where course like '%cs' OR 'chem'"
        print("\nQuery 4: ")
        execute_query(query4)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query5 = "SELECT student_name FROM student WHERE (roll_no like 'X%' OR roll_no like 'Z%') AND roll_no like '%9'" 
        print("\nQuery 5: ")
        execute_query(query5)

    except Exception as e:
        print("Empty set ", e)

    try:
        query6 = "SELECT SID, soc_name, mentor_name, total_seats FROM society WHERE total_seats>@20"
        print("\nQuery 6: ")
        execute_query(query6)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query7 = "select soc_name from society,enrollment GROUP BY soc_name HAVING COUNT(enrollment.sid) >5"
        print("\nQuery 7: ")
        execute_query(query7)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query9 = "SELECT s.Student_name FROM student s JOIN enrollment e ON s.roll_no = e.roll_no JOIN society soc ON e.sid = soc.sid WHERE soc.soc_name = 'NSS' ORDER BY s.dob DESC LIMIT 1"
        print("\nQuery 9: ")
        execute_query(query9)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query10 = "SELECT soc_name FROM society, enrollment GROUP BY soc_name ORDER BY COUNT(enrollment.sid) desc limit 1" 
        print("\nQuery 10: ")
        execute_query(query10)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query11 = "select student_name from student, enrollment where SID NOT IN (select SID from enrollment)"
        print("\nQuery 11: ")
        execute_query(query11)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query12 = "select s.student_name, so.soc_name FROM student AS S LEFT JOIN enrollment AS E ON s.roll_no = E.roll_no LEFT JOIN society so ON E.SID = so.SID GROUP BY s.student_name, so.soc_name;"
        print("\nQuery 12: ")
        execute_query(query12)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query13 = " select soc_name, total_seats - COUNT(e.Roll_no) AS VacantSeats from society as so LEFT JOIN enrollment e ON so.SID = e.SID GROUP BY so.SID, so.soc_name, so.total_seats"
        print("\nQuery 13: ")
        execute_query(query13)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query14 = "select COUNT(DISTINCT SID) FROM enrollment GROUP BY SID HAVING COUNT(*) > 5"
        print("\nQuery 14: ")
        execute_query(query14)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query15 = "SELECT COUNT(*) AS no_soc FROM society as s left join enrollment as e ON s.roll_no = e.roll_no left join  where soc_name like 's%t' GROUP BY SID HAVING COUNT(*) >= 5"
        print("\nQuery 15: ")
        execute_query(query15)

    except Exception as e:
        print("An error has occured: ", e)

    try:
        query16 = "SELECT soc_name as SocietyName, mentor_name, Total_seats AS TotalCapacity, COUNT(Roll_no) AS TotalEnrolled, Total_Seats - COUNT(Roll_no) AS Unfilled_Seats FROM society left join enrollment as e ON Society.SID = e.SID GROUP BY SocietyName, Mentor_name, TotalCapacity"
        print("\nQuery 16: ")
        execute_query(query16)

    except Exception as e:
        print("An error has occured: ", e)

         

        
if __name__ =="__main__":
    main()
        
        


