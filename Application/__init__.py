from flask import Flask

app = Flask( __name__ )
# app = Flask(__name__, static_url_path='/Application/static')
from Application import routes