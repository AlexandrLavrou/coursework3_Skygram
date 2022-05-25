from flask import Flask

from app.posts.views import post_blueprint
from app.api.views import api_blueprint
from app.logger import logging_it

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

logging_it()

app.register_blueprint(post_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True)