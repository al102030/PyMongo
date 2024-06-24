import pymongo


conn_str = "mongodb://localhost:27017/"
try:
    client = pymongo.MongoClient(conn_str)
except Exception:
    print("Error" + Exception)

my_db = client["bookstore"]
my_collection = my_db["books"]

# my_doc = {"title": "Stars", "author": "Borono D.Kooshali", "pages": 405, "rating": 8,
#           "genres": ["spirituality", "progress"], "reviews": [{"name": "ali", "body": "bah bah"}]}

# res = my_collection.insert_one(my_doc)

record = my_collection.find_one()
print(record)
# print(res.inserted_id)
print(client.list_database_names())
