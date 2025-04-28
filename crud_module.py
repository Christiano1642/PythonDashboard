# crud_module.py

from pymongo import MongoClient, errors

class MongoCRUD:
    def __init__(self, uri="mongodb://christianCW:1642W@nv-desktop-services.apporto.com:34359/?directConnection=true&appName=mongosh+1.8.0", 
                 db_name="AAC", collection_name="animals"):
        """
        Initialize the connection to MongoDB.
        """
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]
        except errors.ConnectionError as e:
            print(f"Connection Error: {e}")

    def create(self, document):
        """
        Insert a document into the collection.
        Args:
            document (dict): The document to insert.
        Returns:
            bool: True if the insert is successful, False otherwise.
        """
        try:
            result = self.collection.insert_one(document)
            return True if result.inserted_id else False
        except Exception as e:
            print(f"Error in create method: {e}")
            return False

    def read(self, query):
        """
        Retrieve documents from the collection that match the query.
        Args:
            query (dict): The lookup query.
        Returns:
            list: A list of documents, or an empty list if none found.
        """
        results = []
        try:
            cursor = self.collection.find(query)
            for doc in cursor:
                results.append(doc)
        except Exception as e:
            print(f"Error in read method: {e}")
        return results

    def update(self, query, update_values, many=False):
        """
        Update document(s) matching the query with the provided values.
        Args:
            query (dict): The lookup query.
            update_values (dict): Key/value pairs to update.
            many (bool): If True, update all matching documents. If False, update one.
        Returns:
            int: The number of documents modified.
        """
        try:
            if many:
                result = self.collection.update_many(query, {"$set": update_values})
            else:
                result = self.collection.update_one(query, {"$set": update_values})
            return result.modified_count
        except Exception as e:
            print(f"Error in update method: {e}")
            return 0

    def delete(self, query, many=False):
        """
        Delete document(s) that match the query.
        Args:
            query (dict): The lookup query.
            many (bool): If True, delete all matching documents. If False, delete one.
        Returns:
            int: The number of documents deleted.
        """
        try:
            if many:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error in delete method: {e}")
            return 0

# Quick test if this file is run directly
if __name__ == '__main__':
    crud = MongoCRUD()
    test_doc = {"animal_id": "TEST001", "breed": "Border Collie", "age_upon_outcome_in_weeks": 52}
    print("Create Test:", crud.create(test_doc))
    print("Read Test:", crud.read({"animal_id": "TEST001"}))
    update_count = crud.update({"animal_id": "TEST001"}, {"age_upon_outcome_in_weeks": 90})
    print("Update Test - Modified Count:", update_count)
    delete_count = crud.delete({"animal_id": "TEST001"})
    print("Delete Test - Deleted Count:", delete_count)
