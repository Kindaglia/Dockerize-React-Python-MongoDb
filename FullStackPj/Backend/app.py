from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
# cors
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

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





@app.route('/documento', methods=['POST'])
def caricamento_documento():
    name = request.json['name']
    age = request.json['age']
    city = request.json['city']
    return jsonify(insertPerson(name, age, city))



@app.route('/documento/<id>', methods=['GET'])
def get_documento_by_id(id):
    # verifica che l'id sia valido
    if not ObjectId.is_valid(id):
        return jsonify({'error': 'invalid ObjectId'}), 400
    # recupero del documento dal database
    document = db.documenti.find_one({'_id': ObjectId(id)})
    # verifica che il documento esista
    if not document:
        return jsonify({'error': 'documento non trovato'}), 404
    # conversione dell'oggetto ObjectId in stringa
    document['_id'] = str(document['_id'])
    # restituzione del documento come risposta JSON
    return jsonify(document)


@app.route('/documento', methods=['GET'])
def get_all_documenti():
    # recupero di tutti i documenti dal database
    documents = list(db.documenti.find())

    # conversione degli oggetti ObjectId in stringhe
    for document in documents:
        document['_id'] = str(document['_id'])

    # restituzione dei documenti come risposta JSON
    return jsonify(documents)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
