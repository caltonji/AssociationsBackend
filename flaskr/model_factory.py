# from flask import g
import gensim.downloader as api
from gensim.models import KeyedVectors
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


model_cache = {}

def get_stemmer():
    print(model_cache.keys())
    if 'stemmer' not in model_cache:
        model_cache["stemmer"] = PorterStemmer()
        print("Stemmer loaded")
    return model_cache["stemmer"]

def get_twitter_model():
    print(model_cache.keys())
    if 'twitter_model' not in model_cache:
        try:
            model_cache["twitter_model"] = KeyedVectors.load("glove.model")
            print("Twitter model downloaded")
        except:
            model_cache["twitter_model"] = api.load("glove-twitter-25")
            model_cache["twitter_model"].save("glove.model")
            print("Twitter model saved to io")
    return model_cache["twitter_model"]

def get_news_model():
    print(model_cache.keys())
    if 'news_model' not in model_cache:
        try:
            model_cache["news_model"] = KeyedVectors.load("news.model")
            print("News model downloaded")
        except:
            model_cache["news_model"] = api.load('word2vec-google-news-300')
            model_cache["news_model"].save("news.model")
            print("News model saved to io")
    return model_cache["news_model"]

def get_random_words():
    if 'random_words' not in model_cache:
        model = get_news_model()
        model_cache["random_words"] = list(model.key_to_index.keys())[250:2000]
        model_cache["random_words"] = [word.lower() for word in model_cache["random_words"] if word.isalpha()]
    return model_cache["random_words"]