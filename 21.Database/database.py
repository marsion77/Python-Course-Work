from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # default Compass connection
print("Connected to MongoDB")

# Step 2: Create (or access) a database
db = client["companyDB"]

# Step 3: Create (or access) a collection
collection = db["employees"]

# Step 4: Insert multiple records
employees_data = [
    {"name": "John Doe", "role": "Developer", "salary": 60000},
    {"name": "Jane Smith", "role": "Designer", "salary": 55000},
    {"name": "Alice Brown", "role": "Manager", "salary": 75000}
]

insert_result = collection.insert_many(employees_data)
print(f"Inserted {len(insert_result.inserted_ids)} records")

# Step 5: Read (find) all records
print("\nEmployees:")
for emp in collection.find():
    print(emp)

# Step 6: Update one record
update_result = collection.update_one(
    {"name": "John Doe"},
    {"$set": {"salary": 000}}
)
print(f"\nUpdated {update_result.modified_count} record(s)")

# Step 7: Delete one record
delete_result = collection.delete_one({"name": "Jane Smith"})
print(f"Deleted {delete_result.deleted_count} record(s)")

# Step 8: Display final data
print("\nFinal Employee List:")
for emp in collection.find():
    print(emp)

# Step 9: Close connection
client.close()
print("\nMongoDB connection closed")
