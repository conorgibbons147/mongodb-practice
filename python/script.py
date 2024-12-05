from pymongo import MongoClient

client = MongoClient("mongodb+srv://USERNAME:PASSWORD@cluster0.zzzzzz.mongodb.net/")
db = client["hjd3db"]

collection_name = "friends"
collection = db[collection_name]

collection.insert_many([
    {"name": "Bowman", "age": 19, "hobby": "fishing"},
    {"name": "Patrick", "age": 19, "hobby": "guitar"},
    {"name": "Turner", "age": 19, "hobby": "volleyball"},
    {"name": "Zach", "age": 20, "hobby": "running"},
    {"name": "William", "age": 19, "hobby": "drinking"}
]
)

results = collection.find().limit(3)

for i in results:
    print(i)

