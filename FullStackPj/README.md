
```yaml
version: '3.8'

services:
  mongodb:
    image: mongo:latest
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: adminpassword
      MONGO_INITDB_DATABASE: testdb
    volumes:
      - ./init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js:ro
    ports:
      - "27017:27017"

  flask_app:
    build: ./flask_app
    environment:
      MONGODB_HOST: mongodb
      MONGODB_USERNAME: admin
      MONGODB_PASSWORD: adminpassword
      MONGODB_DBNAME: testdb
    ports:
      - "5000:5000"
    depends_on:
      - mongodb
```

Crea un file `init-mongo.js` nella directory principale:

```javascript
db.createUser({
    user: "admin",
    pwd: "adminpassword",
    roles: [
        {
            role: "readWrite",
            db: "testdb"
        }
    ]
});
```

Crea una directory `flask_app` e aggiungi un `Dockerfile`:

```Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Crea un file `requirements.txt` nella directory `flask_app`:

```
Flask==2.1.1
pymongo==4.1.0
```

Infine, crea un file `app.py` nella directory `flask_app`:

```python
from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(
    host=os.environ["MONGODB_HOST"],
    username=os.environ["MONGODB_USERNAME"],
    password=os.environ["MONGODB_PASSWORD"],
)
db = client[os.environ["MONGODB_DBNAME"]]
collection = db["documents"]

@app.route("/insert", methods=["POST"])
def insert_document():
    document = request.json
    result = collection.insert_one(document)
    return {"_id": str(result.inserted_id)}

@app.route("/retrieve/<string:doc_id>")
def retrieve_document(doc_id):
    document = collection.find_one({"_id": ObjectId(doc_id)})
    if document:
        document["_id"] = str(document["_id"])
        return jsonify(document)
    else:
        return "Document not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")
```

Per utilizzare questa configurazione:

1. Esegui `docker-compose up --build` per avviare i servizi.
2. Usa un client HTTP o un browser per inviare richieste POST a `http://localhost:5000/insert` per inserire un documento e GET a `http://localhost:5000/retrieve/<doc_id>` per recuperare un documento.











```yaml
version: '3.8'
services:


  mongodb:
    image: mongo:latest
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: adminpassword
    volumes:
      - mongodb_data:/data/db

    flask_app:
    build:
      context: ./Backend #path dockerfile
      dockerfile: Dockerfile #nome Dokcerfile
    environment:
      MONGODB_HOST: mongodb
      MONGODB_USERNAME: admin
      MONGODB_PASSWORD: adminpassword
      MONGODB_DBNAME: testdb
    ports:
      - "5000:5000"
    depends_on:
      - mongodb

volumes:
  mongodb_data:
```