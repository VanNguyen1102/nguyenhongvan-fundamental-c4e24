from matplotlib import pyplot

from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()

customer_collection = db["customers"]
count_events = 0
count_ads = 0
count_wom = 0
for i in customer_collection.find():
    if i["ref"].count("events") == 1:
        count_events += 1
    elif i["ref"].count("ads") == 1:
        count_ads += 1
    elif i["ref"].count("wom") == 1:
        count_wom += 1

customer_ref_counts = [count_events, count_ads, count_wom]
customer_ref_names = ["events", "ads", "wom"]
print(customer_ref_names, customer_ref_counts)

pyplot.pie(customer_ref_counts, labels=customer_ref_names, autopct="%.0f%%", shadow=True, explode=[0.1, 0, 0])
pyplot.title("References ratio")
pyplot.axis("equal")

pyplot.show()

client.close()