import mysql.connector

db = mysql.connector.connect(user='root',host='localhost',password='ninja4545')
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
cursor.execute("USE school")
cursor.execute("""CREATE TABLE IF NOT EXISTS studentdata(
        studentId int primary key,
        firstname text,
        lastname text,
        rollno int,
        std text,
        section text,
        gender text,
        address text,
        dob date
        )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS parentinfo(
        studentId int primary key,
        fatherName text,
        fatherNo varchar(10),
        fatherProfession text,
        motherName text,
        motherNo varchar(10),
        motherProfession text
        )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS feeStatus(
                    studentId int,
                    status text,
                    totalFees int)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS attendence(
        studentId int,
        year int,
        january int,
        february int,
        march int,
        april int,
        may int,
        june int,
        july int,
        august int,
        september int,
        october int,
        november int,
        december int
        )""")


db.commit()
