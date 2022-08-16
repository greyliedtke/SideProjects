import pymongo

from pymongo import MongoClient
client = MongoClient()


db = client.test_database

people = db.people

# save as dictionary
grey = {
    "person_id": 0,
    "Name": "Grey",
    "age": 26,
    "origin": 'MN',
    "weight": 180
}
grey2 = {
    "person_id": 1,
    "Name": "Grey1",
    "age": 26,
    "origin": 'MN',
    "weight": 180
}

# delete
people.delete_one({"Name": "Grey"})
people.delete_many({"age": 26})


# Create mandatory ID field
p_i = db.people.create_index([('person_id', pymongo.ASCENDING)],
                                   unique=True)

# inserting
# people.insert_one(grey)
people.insert_many([grey, grey2])

for p in people.find({"age": 26}):
    print(p)
