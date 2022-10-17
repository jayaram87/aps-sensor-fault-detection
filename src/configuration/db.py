import pymongo
import certifi
from src.constant.constants import db_name, db_url

class DBClient:
    client = None

    def __init__(self, db_name=db_name) -> None:
        try:
            if DBClient.client is None:
                DBClient.client = pymongo.MongoClient(db_url, tlsCAFile=certifi.where())
            self.client = DBClient.client
            self.db = self.client[db_name]
            self.db_name = db_name
        except Exception as e:
            raise e