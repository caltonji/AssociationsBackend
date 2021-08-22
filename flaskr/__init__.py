import os, uuid

from flask import Flask
from flaskr.model_factory import get_stemmer, get_twitter_model, get_news_model
from flask_cors import CORS
from flaskr.associations import setup_associations_models

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    # setup_associations_models()

    # Setup storage
    # with app.app_context():
    #     get_twitter_model()
    #     get_news_model()
    #     get_stemmer()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/', methods=['GET'])
    def hello():
        return "Hello!"

    from . import associations
    app.register_blueprint(associations.bp)

    CORS(app)
    return app