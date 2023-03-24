from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from bson import ObjectId
from flask_cors import CORS

def createDb():
    client = MongoClient(
    host=os.environ["MONGODB_HOST"],
    username=os.environ["MONGODB_USERNAME"],
    password=os.environ["MONGODB_PASSWORD"],
    )
    db = client[os.environ["MONGODB_DBNAME"]]
    docName = db["documents"]


def insertPerson(name, age, city):
    # Creazione del documento da caricare nella collezione
    data = {"name": name, "age": age, "city": city}
    document = db.documenti.insert_one(data)
    inserted_document = db.documenti.find_one({'_id': document.inserted_id})
    inserted_document['_id'] = str(inserted_document['_id'])
    return inserted_document
