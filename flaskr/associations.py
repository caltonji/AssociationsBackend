from flask import (
    Blueprint, request, abort, jsonify
)
from flaskr import model_factory
from flaskr.utils import validate_request_args
import gensim.downloader as api
import random

bp = Blueprint('associations', __name__)

@bp.route('/random', methods=["GET"])
def get_random_words():
    validate_request_args(['count'])
    word_count = int(request.args['count'])
    random_words = model_factory.get_random_words()
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
    stemmer = model_factory.get_stemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    new_scores = {}
    for word in scores:
        if stemmer.stem(word) not in stemmed_words:
            new_scores[word] = scores[word]
    return new_scores

def get_nearest_word(words):
    scores = {}
    model1 = model_factory.get_twitter_model()
    model2 = model_factory.get_news_model()
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
        append_to_scores(scores, model1.most_similar(positive=positive_words, negative=negative_words))
        append_to_scores(scores, model2.most_similar(positive=positive_words, negative=negative_words))
    # this is O(N) when it could be O(1)
    scores = remove_stem_matches(scores, words)
    
    return max(scores, key=scores.get)