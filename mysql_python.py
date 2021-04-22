import MySQLdb
#SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "root"
PASSWORD = "root"
# Open database connection
db = MySQLdb.connect(HOST, USERNAME, PASSWORD)
# prepare a cursor object using cursor() method
cursor = db.cursor()
cursor.execute("DROP DATABASE hospital")
cursor.execute("CREATE DATABASE hospital")
print("Database Created")
cursor.execute("USE hospital")
#-------------------------------------------
print("Task 1")
cursor.execute("CREATE TABLE patient (P_ID INT PRIMARY KEY, P_NAME VARCHAR(255), P_FEES INT)")
print("Table Created")
#-------------------------------------------
print("Task 2")
sql = "INSERT INTO patient (P_ID,P_NAME,P_FEES) VALUES (%s, %s, %s)"
data1 = [101,"John", 670]
data2 = [102,"Manya",200]
data3 = [103,"Roma", 550]
cursor.execute(sql, data1)
db.commit()
cursor.execute(sql, data2)
db.commit()
cursor.execute(sql, data3)
db.commit()
print("Records inserted.")

print("Fetching Records")
cursor.execute("SELECT * from patient")
m = cursor.fetchall()
for x in m:
    print(x)

#----------------------------------------
print("Task 3")
print("Changing the Fees of Manya")
cursor.execute("UPDATE patient set P_FEES = 650 WHERE P_NAME = 'Manya'")
db.commit()
print("Record Updated successfully ")

print("Fetching Records")
cursor.execute("SELECT * from patient")
m = cursor.fetchall()
for x in m:
    print(x)


