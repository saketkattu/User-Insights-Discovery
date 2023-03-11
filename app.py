import streamlit as st
import pandas as pd
import numpy as np

#Scaping Modules
import snscrape.modules.twitter as snstweet
import snscrape.modules.reddit as snsred

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

st.title('User Insights Discovery')


twitter_keyword=st.text_input("twitter", key="twitter")
reddit_keyword=st.text_input("reddit", key="reddit")
playstore=st.text_input("App url on Google Playstore", key="playstore")


if st.button('Import Data'):
    st.write(get_tweets(twitter_keyword,100))






