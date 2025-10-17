from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client["college_db"]
students_collection = db["students"]
student = {
    "first_name": "Aarav",
    "last_name": "Sharma",
    "age": 20,
    "city": "Delhi",
    "course": "Python",
    "marks": 85
}

student2 = {
    "first_name": "Marison",
    "last_name": "Marikozhundu",
    "age": 20,
    "city": "Puducherry",
    "course": "Python",
    "marks": 100
}

students_collection.insert_one(student)
students_collection.insert_one(student2)

