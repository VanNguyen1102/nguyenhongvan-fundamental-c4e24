from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()

post_collection = db["posts"]
    
new_document = {
    "title": "匆匆那年",
    "author": "阮红云",
    "content": "每一个人都有青春，每一个青春都有一个故事，每个故事都有一个遗憾，每个遗憾都有它的青春美。希望你们好好学习，加油！"
}

post_collection.insert_one(new_document)

client.close()

