import os
from fastapi import FastAPI
from starlette.responses import JSONResponse
from app.manager import Manager

app = FastAPI()

MONGO_USER = os.environ.get('MONGO_USER')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
CONNECTION_STR = os.environ.get('CONNECTION_STR')
MONGO_COLLECTION_NAME = os.environ.get('MONGO_COLLECTION_NAME')
WEAPONS_BLACK_LIST_FILE_PATH = os.environ.get('WEAPONS_BLACK_LIST_FILE_PATH')
TEXT_COL_IN_DF = os.environ.get('TEXT_COL_IN_DF')

@app.get('/tweets')
def run():
    manager = Manager(mongo_user=MONGO_USER,
                      mongo_password=MONGO_PASSWORD,
                      mongo_db_name=MONGO_DB_NAME,
                      connection_str=CONNECTION_STR,
                      mongo_collection_name=MONGO_COLLECTION_NAME,
                      weapons_black_list_file_path=WEAPONS_BLACK_LIST_FILE_PATH,
                      text_col_in_df=TEXT_COL_IN_DF)

    manager.fetch_all_tweets()

    manager.get_weapons_black_list()

    clean_df = manager.process_data()

    tweets_result = clean_df.to_dict(orient='records')

    return JSONResponse(tweets_result)
