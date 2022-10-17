from src.configuration.db import DBClient

if __name__ == '__main__':
    client = DBClient()
    print(f'collections: {client.db.list_collection_names()}')