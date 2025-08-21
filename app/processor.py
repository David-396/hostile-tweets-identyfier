import os
from collections import Counter
import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer



class Processor:
    def __init__(self, df : pd.DataFrame, weapons_black_list : set, text_col : str):
        self.df = df
        self.weapons_black_list = weapons_black_list
        self.text_col = text_col

        self.analyzer = SentimentIntensityAnalyzer()

    # found the rarest word in the text
    def rarest_word(self):
        self.df['rarest_word'] = self.df[self.text_col].apply(lambda a:Counter(a.split()).most_common()[-1])

    # finding the sentiment of text
    def sentiment_intensity_analyzer(self):
        self.df['sentiment_score'] = self.df[self.text_col].apply(lambda a: dict(self.analyzer.polarity_scores(a))['compound'])

        bins = [-1,-0.5,0.5,1]
        labels = ['Negative', 'Neutral', 'Positive']

        self.df['sentiment_score'] = pd.cut(self.df['sentiment_score'], bins=bins, labels=labels, include_lowest=True)

    # find a weapon that exist in the black list weapons
    def detect_weapons(self):
        self.df["weapons_detected"] = self.df[self.text_col].apply(lambda txt : self.extract_weapons_from_text(txt, self.weapons_black_list))

    @staticmethod
    def extract_weapons_from_text(text : str, weapons_list : set):
        text = text.split()
        weapons = [weapon for weapon in text if weapon in weapons_list]
        if weapons:
            return weapons[0]
        return None

