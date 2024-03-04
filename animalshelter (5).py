from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self, username, pwd):
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'nimbus'            
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30641           
        DB = 'AAC'              
        COL = 'animals'        
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
    
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Error inserting document:", e)
                return False
        else:
            raise ValueError("Data parameter is empty")

    def read(self, query):
        """
        Retrieve animal records based on the specified query.

        Parameters:
        - query (dict): A dictionary representing the query parameters.

        Returns:
        - pymongo.cursor.Cursor: A cursor object containing the query results.
        """
        try:
            result = self.collection.find(query)
            return result
        except Exception as e:
            return str(e)
    
    def update(self, query, data):
        """
        Update document(s) based on the specified query.

        Parameters:
        - query (dict): A dictionary representing the query parameters.
        - data (dict): A dictionary containing the key/value pairs to be updated.

        Returns:
        - int: The number of objects modified in the collection.
        """
        try:
            result = self.collection.update_many(query, {"$set": data})
            return result.modified_count
        except Exception as e:
            return str(e)
    
    def delete(self, query):
        """
        Delete document(s) based on the specified query.

        Parameters:
        - query (dict): A dictionary representing the query parameters.

        Returns:
        - int: The number of objects removed from the collection.
        """
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            return str(e)




       
    
