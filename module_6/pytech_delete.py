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

#test doc
test_doc = {
    "student_id": "1010",
    "first_name": "Tyler",
    "last_name": "Grey"
}

#insert test doc to MongoDB
test_doc_id = students.insert_one(test_doc).inserted_id
print("\n -- INSERT STATEMENTS --")
print(" Inserted student record into the students collection with document_id " + str(test_doc_id))

#find student ID 1010
students_test_doc = students.find_one({"student_id": "1010"})

#display results
print("\n -- DISPLAYING STUDENT TEST DOC -- ")
print(" Student ID: " + students_test_doc["student_id"] + "\n First Name: " + students_test_doc["first_name"] + "\n Last Name: " + students_test_doc["last_name"] + "\n")

#delete test doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

#find new student
new_student_list = students.find({})

#display output
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")

for doc in new_student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

#exit message
input("\n\n End of program, press any key to continue...")
