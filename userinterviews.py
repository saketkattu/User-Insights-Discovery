from flair.models import TextClassifier
from flair.data import Sentence
from segtok.segmenter import split_single
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy


import streamlit as st

classifier = TextClassifier.load('en-sentiment')
textt=st.text_input(label='textt')

def make_sentences(text):
    """ Break apart text into a list of sentences """
    sentences = [sent for sent in split_single(text)]
    return sentences

pp = make_sentences(textt)

pos=[]
neg=[]
for s in pp:
  text = Sentence(s)
  classifier.predict(text)
  value = text.labels[0].to_dict()['value'] 
  print(text.labels)
  if value == 'POSITIVE':
      pos.append(s)
  elif value == 'NEGATIVE':
    neg.append(s)


def predict(input_str,):
  text = Sentence(s)
  classifier.predict(text)

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sent = nltk.word_tokenize(textt)
sent = nltk.pos_tag(sent)


tok_list = []
for se in sent:
    if se[1]=='NN' or se[1]=='NNP':
        tok_list.append(se[0])

if st.button("Get Insights"):
   pass
   
   