from mongoengine import Document, StringField, IntField

class Food(Document):
    food_name = StringField()
    location = StringField()
    distance = IntField()
    rate = IntField()