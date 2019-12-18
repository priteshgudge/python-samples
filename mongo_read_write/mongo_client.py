import pymongo
import uuid

class MongoClient():
    def __init__(self, db_name, collection_name):
        self._client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self._client.get_database(db_name)
        self.cursor = self.db.get_collection(collection_name)

    def set_doc_id(self, doc_id, document):
        if doc_id:
            document.update({'_id': doc_id})
        else:
            document.update({'_id': uuid.uuid4()})

    def get(self, doc_id):
        return self.cursor.find_one({'_id':doc_id})

    def insert(self, doc_id, document):

        self.set_doc_id(doc_id, document)

        self.cursor.insert(document)

    def upsert(self,doc_id, document):
        self.set_doc_id(doc_id, document)

        self.cursor.update({'_id': doc_id},document,upsert=True)

    def update(self,doc_id,document):
        self.set_doc_id(doc_id, document)
        self.cursor.update_one({"_id": doc_id},document)

    def delete(self,doc_id):

        self.cursor.delete_one(doc_id)

    def find_by_key(self,key, value):

        return list(self.cursor.find({key:value}))

    def delete_database(self, db_name):
        self._client.drop_database(db_name)


