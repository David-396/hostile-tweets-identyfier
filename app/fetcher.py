import pymongo


class Fetcher:
    def __init__(self, user : str, password : str, db_name : str, connection_str = None):
        self.user = user
        self.password = password
        self.db_name = db_name

        if not connection_str:
            connection_str = f'mongodb+srv://{user}:{password}@{db_name}.gurutam.mongodb.net/'
        self.connection_str = connection_str

    # get all data from mongo
    def fetch_all(self, table_name : str):
        client = None
        try:
            client = pymongo.MongoClient(self.connection_str)
            db = client[self.db_name]
            table = db[table_name]
            data = list(table.find({},{'_id':0}))
            return data

        except Exception as e:
            print(e)

        finally:
            if client is not None:
                client.close()