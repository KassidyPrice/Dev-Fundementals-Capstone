import datetime, sqlite3, bcrypt, csv

print('Welcome to the Competency Tracker')
print('-----------------------------------')
print('Please Login\n')
email = input('Enter User email: ')
password = input('Enter User password: ')

def change_own_password(email):
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 sql_update = f'UPDATE Users SET password=? WHERE email ="{email}"'
 new_password = input('Enter New Password: ')
 encrypted = new_password.encode('utf-8')
 salt = bcrypt.gensalt()
 hashed = (bcrypt.hashpw(encrypted, salt),)
 cursor.execute(sql_update, hashed)
 connection.commit()

def change_user_password():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 user_id = input('Enter User ID: ')
 sql_update = f'UPDATE Users SET password=? WHERE user_id ="{user_id}"'
 new_password = input('Enter New Password: ')
 encrypted = new_password.encode('utf-8')
 salt = bcrypt.gensalt()
 hashed = (bcrypt.hashpw(encrypted, salt),)
 cursor.execute(sql_update, hashed)
 connection.commit() 

def change_own_fname(email):
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 sql_update = f'UPDATE Users SET first_name = ? WHERE email ="{email}"'
 new_fname = (input('Enter New First Name: '),)
 cursor.execute(sql_update, new_fname)
 connection.commit() 

def change_user_fname():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 user_id = input('Enter User ID: ')
 sql_update = f'UPDATE Users SET first_name = ? WHERE user_id ="{user_id}"'
 new_fname = (input('Enter New First Name: '),)
 cursor.execute(sql_update, new_fname)
 connection.commit() 

def change_own_lname(email):
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 sql_update = f'UPDATE Users SET last_name = ? WHERE email ="{email}"'
 new_lname = (input('Enter New Last Name: '),)
 cursor.execute(sql_update, new_lname)
 connection.commit()

def change_user_lname():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 user_id = input('Enter User ID: ')
 sql_update = f'UPDATE Users SET last_name = ? WHERE user_id ="{user_id}"'
 new_lname = (input('Enter New Last Name: '),)
 cursor.execute(sql_update, new_lname)
 connection.commit()  

def change_own_email(email):
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 sql_update = f'UPDATE Users SET email = ? WHERE email ="{email}"'
 new_email = (input('Enter New Email: '),)
 cursor.execute(sql_update, new_email)
 connection.commit() 

def change_user_email(email):
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 user_id = input('Enter User ID: ')
 sql_update = f'UPDATE Users SET email = ? WHERE user_id ="{user_id}"'
 new_email = (input('Enter New Email: '),)
 cursor.execute(sql_update, new_email)
 connection.commit() 

def change_own_phone(email):
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 sql_update = f'UPDATE Users SET phone = ? WHERE email ="{email}"'
 new_phone = (input('Enter New Phone Number: '),)
 cursor.execute(sql_update, new_phone)
 connection.commit()

def change_user_phone():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 user_id = input('Enter User ID: ')
 sql_update = f'UPDATE Users SET phone = ? WHERE user_id ="{user_id}"'
 new_phone = (input('Enter New Phone Number: '),)
 cursor.execute(sql_update, new_phone)
 connection.commit()   

def change_role():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 user_id = input('Enter User ID: ')
 new_role = (input('Enter New User Role: '),)
 sql_update = f'UPDATE Users SET user_type = ? WHERE user_id ="{user_id}"'
 cursor.execute(sql_update, new_role)
 connection.commit() 

def deactivate(): 
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 user_id = input('Enter User ID: ')
 sql_update = f'UPDATE Users SET is_active = 0 WHERE user_id ="{user_id}"'
 cursor.execute(sql_update)
 connection.commit() 
 print(f'\nUser {user_id} Successfully Deactivated.')

def list_users():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 rows = cursor.execute(f'SELECT * FROM Users').fetchall()
 for row in rows:
  print(f"ID: {row[0]:<3} First Name: {row[1]:<10} Last Name: {row[2]:<10} Phone: {row[3]:<10} Email: {row[4]:<20} Hire Date:{row[6]:<10} Date_created: {row[7]:<10} Active: {row[8]:<3} User Type: {row[9]:<10}")

def list_comps():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 rows = cursor.execute(f'SELECT * FROM Competencies').fetchall()
 for row in rows:
  print(f"ID: {row[0]:<3} Competency: {row[1]:<30} Date_created: {row[2]:<10}")

def list_assess():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 rows = cursor.execute(f'SELECT * FROM Assessments').fetchall()
 for row in rows:
  print(f"ID: {row[0]:<5} Name: {row[1]:<20} Date_created: {row[2]:<10} Competency: {row[3]:<30}")   

def list_results():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 rows = cursor.execute(f'SELECT * FROM Assessment_Results').fetchall()
 for row in rows:
  print(f"Result ID: {row[0]:<3} User ID: {row[1]:<3} Assessment ID: {row[2]:<3} Score: {row[3]:<3} Date Taken: {row[4]:<10} Manager ID: {row[5]:<3}")   

def all_users():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 comp_id = input('Enter Competency ID for the report you wish to see: ')
 rows = cursor.execute(f'SELECT u.user_id, first_name, comp_name, score FROM Users u, Assessment_results r, Assessments a,Competencies c WHERE u.user_id = r.user_id AND a.assess_id = r.assess_id AND c.comp_id = a.comp_id AND c.comp_id ="{comp_id}"').fetchall()
 for row in rows:
  print(f"ID: {row[0]:<3} First Name: {row[1]:<10} Competency: {row[2]:<30} Score: {row[3]:<3}")

def indiv_users():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 user_id = input('Enter User ID for individual competency report you wish to see: ')
 rows = cursor.execute(f'SELECT u.user_id, first_name, email, comp_name, score FROM Users u, Assessment_results r, Assessments a,Competencies c WHERE u.user_id = r.user_id AND a.assess_id = r.assess_id AND c.comp_id = a.comp_id AND u.user_id ="{user_id}"').fetchall()
 for row in rows:
  print(f"ID: {row[0]:<3} First Name: {row[1]:<10} Email: {row[2]:<15} Competency: {row[3]:<30} Score: {row[4]:<3}")

def indiv_assess():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 user_id = input('Enter User ID for assessment report you wish to see: ')
 rows = cursor.execute(f'SELECT u.user_id, first_name, assess_name, score FROM Users u, Assessment_results r, Assessments a WHERE u.user_id = r.user_id AND a.assess_id = r.assess_id AND u.user_id ="{user_id}"').fetchall()
 for row in rows:
  print(f"ID: {row[0]:<3} First Name: {row[1]:<10} Assessment: {row[2]:<30} Score: {row[3]:<3}")    
 
def print_user(email):
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 row = cursor.execute(f'SELECT * FROM Users WHERE email = "{email}" ').fetchone()
 print(f"ID: {row[0]:<5} First Name: {row[1]:<10} Last Name: {row[2]:<10} Phone: {row[3]:<10} Email: {row[4]:<15} Hire Date:{row[6]:<10} Date_created: {row[7]:<10} Active: {row[8]:<3} User Type: {row[9]:<10}")

def search_users():
  connection = sqlite3.connect('comp_tracking.db')
  cursor = connection.cursor()
  search = input('Enter the Name of the User you are searching for: ')
  query = cursor.execute(f"SELECT * FROM Users WHERE first_name LIKE '%{search}%' OR last_name LIKE '%{search}%'").fetchall()
  for row in query:
    print(f"ID: {row[0]:<3} First Name: {row[1]:<10} Last Name: {row[2]:<10} Phone: {row[3]:<10} Email: {row[4]:<15} Hire Date:{row[6]:<10} Date_created: {row[7]:<10} Active: {row[8]:<3} User Type: {row[9]:<10}")
  connection.commit()
  
def add_user():
  connection = sqlite3.connect('comp_tracking.db')
  cursor = connection.cursor()
  insert_sql = 'INSERT INTO Users (first_name, last_name, phone, email, password, date_created, hire_date) VALUES (?,?,?,?,?,?,?)'
  first_name = input('Enter User First Name: ')
  last_name = input('Enter User Last Name: ')
  phone = input('Enter User Phone Number: ')
  email = input('Enter User email: ')
  password = input('Enter User password: ')
  encrypted = password.encode('utf-8')
  date_created = datetime.datetime.today()
  hire_date = input('Enter User Hire Date: ')
  
  salt = bcrypt.gensalt()
  hashed = bcrypt.hashpw(encrypted, salt)
  
  values = (first_name, last_name, phone, email, hashed, date_created, hire_date)
  cursor.execute(insert_sql, values)
  connection.commit() 

def add_competency():
  connection = sqlite3.connect('comp_tracking.db')
  cursor = connection.cursor()
  insert_sql = 'INSERT INTO Competencies(comp_name, date_created) VALUES (?,?)'
  comp_name = input('Enter Competency: ')
  date_created = datetime.datetime.today()
  values = (comp_name, date_created)
  cursor.execute(insert_sql, values)
  connection.commit() 

def edit_competency():
 list_comps()
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 comp_id = input('Enter Competency ID you want to edit: ')
 sql_update = f'UPDATE Competencies SET comp_name = ?, date_created = ? WHERE comp_id ="{comp_id}"'
 new_comp_name = input('Enter New Competency Name: ')
 date_created = datetime.datetime.today()
 values = (new_comp_name, date_created)
 cursor.execute(sql_update, values)
 connection.commit()  

def add_assess():
  connection = sqlite3.connect('comp_tracking.db')
  cursor = connection.cursor()
  insert_sql = 'INSERT INTO Assessments(assess_name, date_created, comp_id) VALUES (?,?,?)'
  assess_name = input('Enter Assessment Name: ')
  list_comps()
  comp_id = input('Enter the Measured Competency ID: ')
  date_created = datetime.datetime.today()
  values = (assess_name, date_created, comp_id )
  cursor.execute(insert_sql, values)
  connection.commit() 

def edit_assess():
 list_assess()
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 assess_id = input('Enter Assessment ID you want to edit: ')
 sql_update = f'UPDATE Assessments SET assess_name = ?, date_created = ?, comp_id = ? WHERE assess_id ="{assess_id}"'
 assess_name = input('Enter Assessment Name: ')
 date_created = datetime.datetime.today()
 comp_id = input("Enter the Measrued Competency ID: ")
 values = (assess_name, date_created, comp_id)
 cursor.execute(sql_update, values)
 connection.commit()  

def delete_assess():
  connection = sqlite3.connect('comp_tracking.db')
  cursor = connection.cursor()
  list_assess()
  assess_id = input('Enter Assessment ID: ')
  insert_sql = f'DELETE FROM Assessments WHERE assess_id = "{assess_id}"'
  cursor.execute(insert_sql)
  connection.commit() 
  print(f'Assessment {assess_id} deleted.') 

def add_result():
  connection = sqlite3.connect('comp_tracking.db')
  cursor = connection.cursor()
  insert_sql = 'INSERT INTO Assessment_Results(user_id, assess_id, score, date_taken, manager_id) VALUES (?,?,?,?,?)'
  user_id = input('Enter Assessment Taker User ID: ')
  assess_id = input('Enter Assessment ID: ')
  score = input('Enter Assessment Score: ')
  date_taken = input('Enter Date Taken: ')
  manager_id = input("Enter Manager ID of Assessment Taker, put 0 if N/A: ")
  values = (user_id, assess_id, score, date_taken, manager_id)
  cursor.execute(insert_sql, values)
  connection.commit()

def edit_result():
 list_results()
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 result_id = input('Enter Result ID you want to edit: ')
 sql_update = f'UPDATE Assessment_Results SET user_id = ?, assess_id = ?, score = ?, date_taken = ?, manager_id = ? WHERE result_id ="{result_id}"'
 user_id = input('Enter Assessment Taker User ID: ')
 assess_id = input('Enter Assessment ID: ')
 score = input('Enter Assessment Score: ')
 date_taken = input('Enter Date Taken: ')
 manager_id = input("Enter Manager ID of Assessment Taker, put 0 if N/A: ")
 values = (user_id, assess_id, score, date_taken, manager_id)
 cursor.execute(sql_update, values)
 connection.commit()   

def edit_user_menu():
  while True:
    print('[P] Update Password')
    print('[F] Update User First Name')
    print('[L] Update User Last Name')
    print('[E] Update User Email')
    print('[Ph] Update User Phone Number')
    print('[U] Edit User Role')
    print('[D] Deactivate a User')
    print('[B] Go Back')
    user_input = input('What would you like to Update? ')
    if user_input.lower() == 'p':
      change_user_password()
    if user_input.lower() == 'f':
      change_user_fname()
    if user_input.lower() == 'l':
      change_user_lname()
    if user_input.lower() == 'e':
      change_user_email()
    if user_input.lower() == 'ph':
      change_user_phone()
    if user_input.lower() == 'u':
      change_role()
    if user_input.lower() == 'd':
      deactivate()  
    if user_input.lower() == 'b':
      break
    else:
      print('Please enter a valid choice')             

def edit_menu():
  while True:
    print('[U] Edit a User')
    print('[C] Edit a Competency')
    print('[R] Edit Assessment Results')
    print('[A] Edit an Assessment')
    print('[B] Go Back')
    user_input = input('What would you like to add? ')
    if user_input.lower() == 'u':
      list_users()
      edit_user_menu()
    if user_input.lower() == 'c':
      edit_competency()
    if user_input.lower() == 'r':
      edit_result()
    if user_input.lower() == 'a':
      edit_assess()
    if user_input.lower() == 'b':
      break
    else:
      print('Please enter a valid choice')  

def add_menu():
  while True:
    print('[U] Add a User')
    print('[C] Add a Competency')
    print('[R] Add Assessment Results')
    print('[A] Add a New Assessment')
    print('[B] Go Back')
    user_input = input('What would you like to add? ')
    if user_input.lower() == 'u':
      add_user()
    if user_input.lower() == 'c':
      add_competency()
    if user_input.lower() == 'r':
      add_result()
    if user_input.lower() == 'a':
      add_assess()
    if user_input.lower() == 'b':
      break
    else:
      print('Please enter a valid choice')

def report_menu():
  while True:
    print('[A] View a report of all users and their competency levels for a given competency')
    print('[I] View a competency level report for an individual user')
    print('[L] View a list of assessments for a given user')
    print('[B] Go Back')
    user_input = input('What report would you like to view? ')
    if user_input.lower() == 'a':
      all_users()
    if user_input.lower() == 'i':
      indiv_users()
    if user_input.lower() == 'l':
      indiv_assess()
    if user_input.lower() == 'b':
      break
    else:
      print('Please enter a valid choice')

def user_menu():
  while True:
    print('[U] Update User Info')
    print('[v] View Competency Data')
    print('[B] Go Back')
    user_input = input('What would you like to do? ') 
    if user_input.lower() == 'u':
      print_user(email)
      update_menu()
    if user_input.lower() == 'v':
      indiv_users()
    if user_input.lower() == 'b':
      break    
    else:
      print('Please enter a valid choice')

def update_menu():
  while True:
    print('[P] Update Password')
    print('[F] Update User First Name')
    print('[L] Update User Last Name')
    print('[E] Update User Email')
    print('[Ph] Update User Phone Number')
    print('[B] Go Back')
    user_input = input('What would you like to Update? ')
    if user_input.lower() == 'p':
      change_own_password(email)
    if user_input.lower() == 'f':
      change_own_fname(email)
    if user_input.lower() == 'l':
      change_own_lname(email)
    if user_input.lower() == 'e':
      change_own_email(email)
    if user_input.lower() == 'ph':
      change_own_phone(email)
    if user_input.lower() == 'b':
      break           
    else:
      print('Please enter a valid choice')

def csv_report_menu():
  while True:
   print('[C] Create Competencies CSV Report')
   print('[U] Create User CSV Report')
   print('[B] Go Back')
   user_input = input('What would you like to do? ')
   if user_input.lower() == 'c':
    export_comp_csv()
   if user_input.lower() == 'u':
    export_user_csv()
   if user_input.lower() == 'b':
     break         
   else:
     print('Please enter a valid choice')


def manager_menu():
  while True: 
    print('[V] View All Users')
    print('[S] Search for Users')
    print('[R] View  Reports and Assessments')
    print('[A] Add User, Competency, Assessment or Assesment Result')
    print('[E] Edit User, Competency, Assessment or Assesment Result')
    print('[D] Delete an Assesment Result')
    print('[C] Create CSV Reports')
    print('[I] Import A CSV FIle of Assessment Results')
    print('[B] Go Back')
    user_input = input('What would you like to do? ')
    if user_input.lower() == 'v':
      list_users()
    if user_input.lower() == 's':
      search_users()
    if user_input.lower() == 'r':
      report_menu()
    if user_input.lower() == 'a':
      add_menu()
    if user_input.lower() == 'e':
      edit_menu()  
    if user_input.lower() == 'd':
      delete_assess()  
    if user_input.lower() == 'c':
      csv_report_menu() 
    if user_input.lower() == 'i':
      import_csv()    
    if user_input.lower() == 'b':
      break         
    else:
      print('Please enter a valid choice')     

def login():
  try: 
    connection = sqlite3.connect('comp_tracking.db')
    cursor = connection.cursor()
    encrypted = password.encode('utf-8')
    row = cursor.execute(f'SELECT * FROM Users WHERE email = "{email}" ').fetchone()
    user_type = row[9]
    if bcrypt.checkpw(encrypted, row[5]):
      if user_type.lower() == 'user':
        user_menu() 
      if user_type.lower() == 'manager':
        manager_menu() 
    else:
      print("password does not match")
  except:
    print("Email not found")  
      

def export_user_csv():
 conn = sqlite3.connect('comp_tracking.db')
 cursor = conn.cursor()
 cursor.execute("SELECT * from Users;")
 with open("users.csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    csv_writer.writerows(cursor)
 conn.close()

def export_comp_csv():
 conn = sqlite3.connect('comp_tracking.db')
 cursor = conn.cursor()
 cursor.execute("SELECT * from Competencies;")
 with open("comp.csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    csv_writer.writerows(cursor)
 conn.close() 

def import_csv():
 connection = sqlite3.connect('comp_tracking.db')
 cursor = connection.cursor()
 with open('results.csv', 'r') as file:
  number_of_results = 0
  for row in file:
    cursor.execute("INSERT INTO Assessment_Results(user_id, assess_id, score, date_taken) VALUES (?,?,?,?)", row.split(','))
    connection.commit()
    number_of_results += 1
 connection.close()

# class User:
#  def __init__(self, u_id, u_first_name, u_last_name, u_phone, u_email, u_password, u_active, u_hire_date, u_user_type):
#   self.id = u_id
#   self.first_name = u_first_name
#   self.last_name = u_last_name
#   self.phone = u_phone
#   self.email = u_email
#   self.password = u_password
#   self.active = u_active
#   self.date_created = datetime.datetime.today()
#   self.hire_date = u_hire_date
#   self.user_type = u_user_type

  # self.attributes = [self.id, self.first_name, self.last_name, self.city, self.state, self.email, self.date_created, self.age, self.gender]

   # pprint(self.attributes) 