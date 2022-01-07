from pymongo import MongoClient
import re

client = MongoClient("mongodb+srv://admin:IV889anniker@cluster0.vgw9a.mongodb.net/test")
database = client.get_database("prasim")
collection = database["prasimvolgograd"]

db_documents = list(collection.find({}))

with open('Arcticles.txt', 'w', encoding="utf-8") as f:
    for i in range(len(list(db_documents))):
        f.write(db_documents[i]['headline'])
        f.write('\n')
        f.write(re.sub(r'\', \'', ' ', str(db_documents[i]['text'])))
        f.write('\n\n')
    f.close()