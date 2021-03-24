from models import create_classes
import os 
from flask import (Flask,render_template,jsonify,request,redirect)
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
topbar = Navbar(logo,
                View('home', 'get_home),
                View('page_two', 'page_two'),
                )

# registers the "top" menubar
nav = Nav()
nav.register_element('top', topbar)

app = Flask(__name__)
Bootstrap(app)


# create route that renders index.html template
@app.route("/home", methods=['GET'])
def get_home():
    return render_template("Project_2.html")

@app.route("/page_two", methods=['GET'])
def get_page_two():
    return render_template("page_two.html")

nav.init_app(app)

if __name__ == "__main__":
    app.run()
