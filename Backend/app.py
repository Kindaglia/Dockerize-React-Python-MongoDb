from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

if 'MONGO_URI' in os.environ and 'MONGO_DB' in os.environ:
    client = MongoClient(os.environ['MONGO_URI'])
    db = client[os.environ['MONGO_DB']]
    collection = db.collection_name

    # crea il documento con {username: "billi"}
    try:
        collection.insert_one({"username": "billi"})
    except Exception as e:
        print(f"Errore durante l'inserimento del documento: {e}")

    @app.route('/user')
    def get_user():
        # recupera il documento creato in precedenza
        try:
            user = collection.find_one({"username": "billi"})
            return jsonify(user)
        except Exception as e:
            print(f"Errore durante la ricerca del documento: {e}")
            return jsonify({"error": str(e)})
else:
    print("Le variabili d'ambiente MONGO_URI e/o MONGO_DB non sono state impostate.")
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
