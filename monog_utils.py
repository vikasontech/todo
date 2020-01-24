import pymongo

class MongoUtils:

   @staticmethod
   def get_database():
      client = pymongo.MongoClient(
         "mongodb://root:example@localhost:27017/test?authSource=admin&authMechanism=SCRAM-SHA-256")
      return client.get_database("test")

   def get_collection(self, collection_name):
      return self.get_database().get_collection(collection_name)

