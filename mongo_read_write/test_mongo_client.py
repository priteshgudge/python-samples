import unittest
import jsondiff
from mongo_read_write import mongo_client

class TestMongoClient(unittest.TestCase):
    def setUp(self) -> None:
        self.mongo_client = mongo_client.MongoClient('test','test')
    def tearDown(self) -> None:
        self.mongo_client.delete_database('test')

    def test_read_not_found(self):
        value = self.mongo_client.get('doc_id_test')
        self.assertIsNone(value, "Not None")

    def test_read_write_value(self):
        value_dict = {"key": "value1"}
        self.mongo_client.insert('doc1',value_dict)
        value = self.mongo_client.get(doc_id='doc1')
        #value.pop('_id')
        self.assertDictEqual(value_dict, value)

    def test_write_and_find(self):
        value_dict = {"key": "value1"}
        self.mongo_client.insert('doc1', value_dict)
        value_dict = {"key": "value1"}
        self.mongo_client.insert('doc2', value_dict)
        result = self.mongo_client.find_by_key("key","value1")
        self.assertEqual(len(result), 2)

    def test_write_update_value(self):
        value_dict = {"key": "value1"}
        self.mongo_client.insert('doc1',value_dict)
        value_dict_update = {"key": "value2"}
        self.mongo_client.upsert('doc1',value_dict_update)
        value = self.mongo_client.get(doc_id='doc1')
        #value.pop('_id')
        self.assertDictEqual(value_dict_update, value)