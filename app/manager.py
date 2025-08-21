import pandas as pd
from app.processor import Processor
from app.fetcher import Fetcher

class Manager:
    def __init__(self,
                 mongo_user:str,
                 mongo_password:str,
                 mongo_db_name:str,
                 mongo_collection_name:str,
                 connection_str:str,
                 weapons_black_list_file_path:str,
                 text_col_in_df:str):

        self.mongo_user = mongo_user
        self.mongo_password = mongo_password
        self.mongo_db_name = mongo_db_name
        self.mongo_collection_name = mongo_collection_name
        self.connection_str = connection_str
        self.weapons_black_list_file_path = weapons_black_list_file_path
        self.text_col_in_df = text_col_in_df
        self.df = None
        self.weapons_black_list = None

    # get the all tweets from mongo
    def fetch_all_tweets(self):
        fetcher = Fetcher(user=self.mongo_user,
                          password=self.mongo_password,
                          db_name=self.mongo_db_name,
                          connection_str=self.connection_str)

        all_tweets = fetcher.fetch_all(self.mongo_collection_name)
        self.df = pd.DataFrame(all_tweets)

    # get the weapon black list
    def get_weapons_black_list(self):
        with open(self.weapons_black_list_file_path, 'r', encoding='utf-8') as f:
            weapons_black_list = {f.readline().strip()}
            for weapon in f:
                weapons_black_list.add(weapon.strip())
            self.weapons_black_list = weapons_black_list

    # make the whole process on the data
    def process_data(self):
        processor = Processor(df=self.df, weapons_black_list=self.weapons_black_list, text_col=self.text_col_in_df)

        processor.rarest_word()
        processor.sentiment_intensity_analyzer()
        processor.detect_weapons()

        return processor.df
