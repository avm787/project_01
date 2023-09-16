import sqlite3
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """CREATE TABLE  IF NOT EXISTS school 
(school_id int NOT NULL PRIMARY KEY,
school_name varchar (100) NOT NULL,
place_count int NOT NULL
);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """REPLACE INTO school (school_id, school_name, place_count)
VALUES
('1', 'Протон', 200),
('2', 'Пeрспектива', 300),
('3', 'Спектр', 400),
('4', 'Содружество', 500);
"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """CREATE TABLE IF NOT EXISTS students
(student_id int NOT NULL,
 student_name varchar (100) NOT NULL,
 school_id int NOT NULL PRIMARY KEY
);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()


connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """REPLACE INTO students (student_id, student_name, school_id)
VALUES
('201', 'Иван', 1),
('202', 'Петр', 2),
('203', 'Анастасия', 3),
('204', 'Игорь', 4);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_students(student_id):
  try:
    con = get_connection()
    cursor = con.cursor()
    sqlquery = '''SELECT * FROM students JOIN school ON students.school_id = school.school_id  WHERE student_id = ?'''
    cursor.execute(sqlquery, (student_id,))
    students_info = cursor.fetchall()
    
    for row in students_info:
      print ("ID студента", row[0])
      print ("Имя студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы:", row[4])
      close_connection(con)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка вида ", error)


get_students(204)


# Использовала  команды CREATE TABLE IF NOT EXISTS и REPLACE INTO students,
# чтобы не вылетали ошибки: "table school already exists" и  "UNIQUE constraint failed: school.school_id"
# Создала базу данных из двух таблиц (для выполнения д/з двух достаточно) 
# и с помощью  функции get_students(student_id) получила следующие результаты: 

# ID студента 201
# Имя студента: Иван    
# ID школы: 1
# Название школы: Протон

# ID студента 202
# Имя студента: Петр
# ID школы: 2
# Название школы: Пeрспектива

# ID студента 203
# Имя студента: Анастасия
# ID школы: 3
# Название школы: Спектр 

# ID студента 204
# Имя студента: Игорь        
# ID школы: 4
# Название школы: Содружество

# Для работы в SQLite в базу добавила таблицу students (вновь созданную базу данных прилагаю).











 
