## IMPORTS! #######################
import json
from pymongo import MongoClient
###################################


client = MongoClient("mongodb://localhost:27017")
db = client.osm                                     # Database name: osm

def insert_data(data, db):
    # remove previous data
    db.delhi.drop()
    # Insert the data into a 'delhi' collection
    db.delhi.insert_many(data)

with open('delhi_map.osm.json') as f:
    data = json.loads(f.read())
    insert_data(data, db)


############### END! ####################


