import spacy
import logging
import pyLDAvis.gensim  # don't skip this
import pyLDAvis
from pprint import pprint
from gensim.models import CoherenceModel
from gensim.utils import simple_preprocess
import gensim.corpora as corpora
import gensim
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import json
import pandas as pd
import numpy as np
import re
from pandas import *

# word clouds
import heapq
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import collections
import matplotlib.cm as cm
from matplotlib import rcParams
from tqdm import tqdm

# sentiment analysis
from textblob import TextBlob

# text preprocessing
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')

# hide warning
warnings.filterwarnings("ignore", category=DeprecationWarning)


def get_biz_name_df(biz_name):
    try:
        if df_business['name'].str.contains(biz_name).any():
            print("Matches were found for the input business name.")
            df_biz_name = df_business[df_business['name'] == biz_name]
            print('Business name is:', biz_name)
            print('The shape of the dataframe for',
                  biz_name, 'is', df_biz_name.shape)
            df_biz_name.to_csv('biz_name.csv')
        else:
            print("Sorry, no entries for that business name were found.")
    except:
        return None

# Join together the photo and business dataframes on the "business_id" column


def get_biz_text_df(biz_name):
    try:
        if df_business['name'].str.contains(biz_name).any():
            print("Matches were found for the input business name.")
            df_biz_name = df_business[df_business['name'] == biz_name]
            print('Business name is:', biz_name)
            print('The shape of the dataframe for',
                  biz_name, 'is:', df_biz_name.shape)
            # print(df_biz_name)
            df_biz_final = df_biz_name.merge(
                df_business, on='business_id').merge(df_photos, on='business_id')
            print('New dataframe with business name, photo, and text data.')
            print(df_biz_final)
            df_biz_final.to_csv('final_df.csv')
        else:
            print("Sorry, no entries for that business name were found.")
    except:
        return None


def castle(n):
    print("eat"*n)


if __name__ == '__main__':
    df_business = pd.read_json(
        'data/business.json', lines=True)
    print('The shape of the FULL business dataframe is:', df_business.shape)

    df_photos = pd.read_json('data/photos.json', lines=True)
    print('The shape of the FULL photos dataframe is:', df_photos.shape)

    df_review = pd.read_csv('data/yelp_review.csv')
    print('The shape of the FULL reviews dataframe is:', df_review.shape)
    biz_mcdonalds = "McDonald's"

    df_final = df_review.join(
        df_business, on='business_id')
    print('The shape of the JOINED dataframe on business_id column is:', df_final.shape)
