from flask import (
    Blueprint, request, abort, jsonify
)
from flaskr import model_factory
from flaskr.utils import validate_request_args
import gensim.downloader as api
from nltk.stem import PorterStemmer
import random

bp = Blueprint('associations', __name__)

@bp.route('/random', methods=["GET"])
def get_random_words():
    validate_request_args(['count'])
    word_count = int(request.args['count'])
    words = random.sample(random_words, word_count)
    return jsonify(words)

@bp.route('/associations', methods=["GET"])
def get_association():
    validate_request_args(['words'])
    words = parse_words()
    
    return jsonify(get_nearest_word(words))



def parse_words():
    words_str = request.args['words']
    if not isinstance(words_str, str):
        abort(400, description="Can't parse words field")
    words = [x.strip() for x in words_str.split(',')]
    return words


def append_to_scores(scores, probs):
    for word, prob in probs:
        if word in scores:
            scores[word] += prob
        else:
            scores[word] = prob
    return scores

def remove_stem_matches(scores, words):
    # stemmer = get_stemmer()
    new_scores = {}
    for word in scores:
        if stemmer.stem(word) not in words:
            new_scores[word] = scores[word]
    return new_scores

def get_nearest_word(words):
    scores = {}
    # model = get_twitter_model()
    # word2vec_model = get_news_model()
#     append_to_scores(scores, model.most_similar(positive=words))
#     append_to_scores(scores, word2vec_model.most_similar(positive=words))
    test_items = [
        {
            "positive": ["vegetable"],
            "negative": ["carrot"]
        },
        {
            "positive": ["fruit"],
            "negative": ["apple"]
        },
        {
            "positive": ["color"],
            "negative": ["blue"]
        }
    ]
    for test in test_items:
        positive_words = test["positive"] + words
        negative_words = test["negative"]
        append_to_scores(scores, model.most_similar(positive=positive_words, negative=negative_words))
        append_to_scores(scores, word2vec_model.most_similar(positive=positive_words, negative=negative_words))
    scores = remove_stem_matches(scores, words)
    
    return max(scores, key=scores.get)

def setup_associations_models():
    print("setting up models")
    global stemmer
    stemmer = PorterStemmer()
    global model
    model = api.load("glove-twitter-25")
    global word2vec_model
    word2vec_model = api.load('word2vec-google-news-300')
    global random_words
    random_words = list(word2vec_model.key_to_index.keys())[250:2000]
    random_words = [word.lower() for word in random_words if word.isalpha()]