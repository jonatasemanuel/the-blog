import pymongo
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)


def get_db():
    client = MongoClient(
        host="mongo", port=27017, user="mongo", password="pass123", authSource="admin"
    )
    db = client["mongo"]
    return db


@app.route("/")
def ping_server():
    return "Hello world number 239"


@app.route("/animals")
def fetch_animals():
    db = get_db()
    _animals = db.mongo_table.find()
    animals = [
        {"id": animal["id"], "name": animal["name"], "type": animal["type"]}
        for animal in _animals
    ]
    return jsonify({"animals": animals})


if __name__ == "__main__":
    app.run(debug=True)
