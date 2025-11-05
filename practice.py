from pymongo import MongoClient

cleint = MongoClient('mongodb://localhost:27017')
db = cleint['MyData']
collection = db['students']
collection.insert_one({"name": "Rahul", "course": "Python Full Stack"})
print("Data inserted successfully!")