from flask import g
import gensim.downloader as api
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


def get_stemmer():
    if 'stemmer' not in g:
        print("Loading stemmer")
        g.stemmer = PorterStemmer()

    return g.stemmer

def get_twitter_model():
    if 'twitter_model' not in g:
        print("loading twitter model")
        g.twitter_model = api.load("glove-twitter-25")

    return g.twitter_model

def get_news_model():
    if 'news_model' not in g:
        print("loading news model")
        g.news_model =  api.load('word2vec-google-news-300')

    return g.news_model