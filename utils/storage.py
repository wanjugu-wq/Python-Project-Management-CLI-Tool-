import json

Database = "data/database.json"


def load_data():
    with open(Database, "r") as file:
        return json.load(file)


def save_data(data):
    with open(Database, "w") as file:
        json.dump(data, file, indent=4)