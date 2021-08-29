#!/usr/bin/ python3

import sqlite3
import time
import pandas as pd
from tqdm import tqdm


# MAIN PROGRAM GOES HERE

# @ Bello Yusuf (Mr_coder) 
# This project is done for educational purpose and its available for every one

print()
name = input("Please may i know your Name: ")
print()
print(f""" You are welcome Mr {name}. \n
           Please be patient while the programm is loading.... 😊""")
print()

# Progress bar code

# for i in tqdm(range( 100), desc="Loading..."):
#     time.sleep(0.1)
# print()

# what are you doing in school of informations`
# MAIN FUNCTION
def main():
    main_menu()
    while True:
        print()
        command = input("Please Enter your command >>> ")
        print()
        if command == "add" or command == "ad":
            addNew()
        elif command == "list" or command == 'lis':
            displayAll()
        elif command == "update" or command == 'up':
            updateRecord()
        elif command == "search" or command == 'sea':
            searchRecord()
        elif command == "delete" or command == 'del':
            deleteRecord()
        elif command == "help" or command == 'hel':
            help()
        elif command == "home" or command == 'hom':
            main_menu()
        elif command == "exit" or command == 'quit':
            break
        else:
            print(f"Mr {name} Please make a proper command!!! 😠")
    
    print(f"Thanks 👍 for using this Application Mr {name}")
    print()

# main menu function 

def main_menu():
    ''' Declaration of main menu functions '''
    print()
    print("\t STUDENT MANAGER ")
    print()
    print("Add    - Add new record ")
    print("List   - Display All record ")
    print("Update - Update existing record ")
    print("Search - Make a search ")
    print("Delete - Delete existed record")
    print("help   - User guid")
    print("home   - back to main menu")
    print()

# adding module
def addNew():
    ''' Function that would add new record'''
    print()
    print("\t ADD NEW RECORD")
    print()
    
    ''' Connect with sqlite3 database'''

    conn = sqlite3.connect("student.db")
 
    full_name = input("Enter your Full Name: ")
    gender = input("Enter your Gender: ")
    address = input("Enter your Address: ")
    phone = input("Enter your Phone_No: ")
    email = input("Enter your Email: ")
    print()

    print("Please wait while adding is processing")
    print()

    ''' time.sleep would take a one second before saving the record to the datebase '''
    time.sleep(1)
    
    c = conn.cursor()


    # c = conn.execute('''CREATE TABLE student
    #                   (Full_name text,
    #                   Gender TEXT,
    #                   Address TEXT, 
    #                   Phone BIGINT,
    #                   Email TEXT )
    #                   '''
    #                   )
    
    result = full_name, gender, address, phone, email

    query = f"INSERT INTO student VALUES(?,?,?,?,?)"
    
    c.execute(query,(result))
    print(f"{full_name} Record, added to Database successfully")

    conn.commit()
    conn.close()

    # End of database

# dispaly function
def displayAll():
    ''' Function that would display all record '''
    print()
    print("\t\t\t DISPLAY ALL STUDENT")
    print()
    conn = sqlite3.connect("student.db")
    c = conn.cursor()

      # displaying by using pandas
    df = pd.read_sql_query('''SELECT * FROM student 
                            ORDER BY Full_name ASC''',conn)
    print(df)

    print()
    print("All record have been displayed")
    
    conn.commit()
    conn.close()

# UPDATE EXISTED RECORD
def updateRecord():
    ''' function that would update an existed record in the database'''
    print()
    print("\t UPDATE RECORD")
    # fetching data from database
    conn = sqlite3.connect("student.db")
    
    old_name = input("Enter the name you want to update: ")
    phone_NO = input("Enter phone number: ")
    
    query = (f'''SELECT * FROM student WHERE 
                Full_name ='{old_name}' 
                AND 
                Phone='{phone_NO}' ''')

    c = conn.cursor()
    c.execute(query)

    ''' This would show one record that is similar to what you asked'''
    result = c.fetchall()
    if (result):
        print()
        print("Please be patient while your request is processing... ")
        print()

        time.sleep(3)

        df = pd.read_sql_query(f'''SELECT * FROM student WHERE 
                Full_name ='{old_name}' 
                AND
                Phone='{phone_NO}' ''',conn)
        print(df)

        print()
        new_name = input("Record found Enter new name: ")
        new_gender = input("Enter new gender: ")
        new_address = input("Enter new address: ")
        new_phone = input("Enter new phone NO: ")
        new_email = input("Enter new email: ")

        new_query = (f'''UPDATE student SET  Full_name ='{new_name}', 
                        Gender ='{new_gender}',
                        Address = '{new_address}', 
                        Phone ='{new_phone}', 
                        Email ='{new_email}'
                        WHERE Full_name = '{old_name}' 
                        AND 
                        Phone ='{phone_NO}' ''')

        c.execute(new_query)
        print()
        print("Record Updated successfully ")

    else:
        print()
        print("Be patient while your request is processing")
        time.sleep(3)
        print("No such Record in the Database !!!")
    
    conn.commit()
    conn.close()

# searching module
def searchRecord():
    """ A function that would make a search """
    print()
    print("\t\t SEARCHING RECORD's")
    conn = sqlite3.connect("student.db")
    c = conn.cursor()
    name = input("Enter the name you want to search: ")
    print()
    print("Please wait a little bit while your request is processing... 😊")
    print()

    for i in tqdm(range(30), desc="Loading..."):
        time.sleep(0.1)
    
    query = (f"SELECT * FROM student WHERE Full_name ='{name}'")
    c.execute(query)
    result = c.fetchall()
    
    if(result):
        print()
        print("\t\t Record Found")
        time.sleep(0.30)
        print()
        df = pd.read_sql_query(f'''SELECT * FROM student 
                                WHERE 
                                Full_name = '{name}' 
                                ORDER BY '{name}' ASC''',conn)
        print(df)
        print()
    else:
        print()
        print("Record Not Found!!! 😒 ")
        print()


# Deleting module
def deleteRecord():
    print()
    print("\t\t DELETE EXISTED RECORD")

    conn = sqlite3.connect("student.db")

    phone = input("Enter the Phone Number: ")

    c = conn.cursor()

    # query = f"DELETE FROM student WHERE Phone = '{phone}' "
    
    query = f'''DELETE FROM student
             WHERE phone = '%{phone}%' '''
             
    result = c.fetchone()
   
    while (conn):
        if  (result):
            print()
            conn = c.execute(query)
            print(" Record Deleted successfully ✅")
            print()
        
        elif(result):
            print()
            print("No such Record 😒")
        else:
            break
    print("Please input a right Number !!!")

    # data base closing
    conn.commit()
    conn.close()


# user guid function
def help():
    """ A user guid function """
    print()
    print("\t\t USER GUID")
    print()
    print('''
    This Application is student manager,
    application, it would allow you to add, 
    delete, make a searching, update an 
    existed record. And at the end you can 
    terminate the App.
    ''')


# End of program
main()