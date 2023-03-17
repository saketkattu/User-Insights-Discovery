import streamlit as st
import pandas as pd
import numpy as np

#Scaping Modules
import snscrape.modules.twitter as snstweet
import snscrape.modules.reddit as snsred

from flair.models import TextClassifier
from flair.data import Sentence
from segtok.segmenter import split_single
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy
# ----------------------------------------------------------------------------------------------------------------------------
#                                                  DATA EXTRACTION FUNCTIONS 
# ----------------------------------------------------------------------------------------------------------------------------

def get_tweets(keyword,count):
  """
  Function to get tweets based on a keyword
  """
  s=snstweet.TwitterListPostsScraper(keyword)
  tweets=[]
  for i,tweet in enumerate(s.get_items()):

    data=[
        tweet.rawContent ,
        'Twitter'
    ]
    tweets.append(data)

    if i > count :
      break
  
  return tweets

def get_reddit(keyword,count):
  """
  Function to get reddit search based on a keyword
  """
  red = snsred.RedditSearchScraper(keyword)
  reds=[]
  
  for i,red in enumerate(red.get_items()):
    data =[
        red.body,
        'Reddit'
    ]
    reds.append(data)
    
    if i > count :
      break
  
  return reds

# ----------------------------------------------------------------------------------------------------------------------------
#                                               DATA UNIFICATION AND LOCAL STORE FUNCTIONS 
# ----------------------------------------------------------------------------------------------------------------------------

def unified_data_model():
    """
    Function to create a unified data model across scources - Twitter , Reddit and Google Paystore Ids 
    """
    pass

# ----------------------------------------------------------------------------------------------------------------------------
#                                                          MAIN APP CODE 
# ----------------------------------------------------------------------------------------------------------------------------
# PlayStore 

from google_play_scraper import app

result = app(
    'com.zerodha.kite3',
    lang='en', # defaults to 'en'
    country='in' # defaults to 'us'
)


st.title('User Insights Discovery')

st.text("Try entering the below : Zerodha com.zerodha.kite3")
twitter_keyword=st.text_input("twitter", key="twitter")
reddit_keyword=st.text_input("reddit", key="reddit")
playstore=st.text_input("App url on Google Playstore", key="playstore")


#if st.button('Import Data'):
 #   st.write(get_tweets(twitter_keyword,100))


from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    playstore,
    lang='en', # defaults to 'en'
    country='in', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    count=100, # defaults to 100

)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

result, _ = reviews(
    playstore,
    continuation_token=continuation_token # defaults to None(load from the beginning)
)

play_df = pd.DataFrame(np.array(result),columns=['review'])
play_df = play_df.join(pd.DataFrame(play_df.pop('review').tolist()))
play_df['source']=['playstore']*int(len(play_df))
playstore_df=play_df[['content','source']]


if st.button('Import Data'):
    st.dataframe(playstore_df)



