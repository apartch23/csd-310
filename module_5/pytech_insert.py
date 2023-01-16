import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.yn0tfol.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

john = {
    "student_id": "1007",
    "first_name": "John",
    "last_name": "Doe",
    "enrollments": [
        {
            "term": "winter",
            "gpa": "4.0",
            "start_date": "December 12, 2021",
            "end_date": "March 08, 2022",
            "courses": [
                {
                    "course_id": "CYBR350",
                    "description": "Database Security",
                    "instructor": "Professor Taylor",
                    "grade": "A"
                },
                {
                    "course_id": "CSD310",
                    "description": "Programming Java",
                    "instructor": "Professor Brown",
                    "grade": "A-"
                }
            ]
        }
    ]
}
bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "winter",
            "gpa": "4.0",
            "start_date": "December 12, 2021",
            "end_date": "March 08, 2022",
            "courses": [
                {
                    "course_id": "CYBR350",
                    "description": "Database Security",
                    "instructor": "Professor Taylor",
                    "grade": "C"
                },
                {
                    "course_id": "CSD310",
                    "description": "Programming Java",
                    "instructor": "Professor Brown",
                    "grade": "A"
                }
            ]
        }
    ]
}
frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggs",
    "enrollments": [
        {
            "term": "winter",
            "gpa": "4.0",
            "start_date": "December 12, 2021",
            "end_date": "March 08, 2022",
            "courses": [
                {
                    "course_id": "CCSD320",
                    "description": "Programming Python",
                    "instructor": "Professor Mace",
                    "grade": "B"
                },
                {
                    "course_id": "CSD310",
                    "description": "Programming Java",
                    "instructor": "Professor Brown",
                    "grade": "A"
                }
            ]
        }
    ]
}

students = db.students

print("--INSERT STATEMENTS--")
john_student_id = students.insert_one(john).inserted_id
print(" Interted student record John Doe into the students collection with student_id " + str(john_student_id))

bilbo_student_id = students.insert_one(bilbo).inserted_id
print(" Inserted student record Bilno Baggins into the students collection with student_id "+ str(bilbo_student_id))

frodo_student_id = students.insert_one(frodo).inserted_id
print(" Inserted student record Frodo Baggs into the student collection with student_id " + str(frodo_student_id))

input("\n\n End of program, press any key to exit...")


