import pymongo

from pymongo import MongoClient
client = MongoClient()
db = client['model_db']

def getAllCourses():
    db.usermodel.distinct("course")

def getUserModel(user, course):
    db.usermodel.findOne({"user": user, "course": course})

def updateUserModel(user, course, newModel):
    db.usermodel.updateOne(
        {"user": user, "course": course},
        {$set: newModel},
        {upsert: true}
    )

