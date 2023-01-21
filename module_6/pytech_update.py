#import pymong and mongoclient 
import pymongo
from pymongo import MongoClient

#connection string to MongoDB
url = "mongodb+srv://admin:admin@cluster0.yn0tfol.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

# connect pytech database 
db = client.pytech

# get student collection
students = db.students 

#find students
student_list = students.find({})
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

#update student id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

john = students.find_one({"student_id": "1007"})

#find updated document 
print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")

print("  Student ID: " + john["student_id"] + "\n  First Name: " + john["first_name"] + "\n  Last Name: " + john["last_name"] + "\n")

input("\n\n End of program, press any key to continue...")


