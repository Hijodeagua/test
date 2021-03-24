from models import create_classes
import os 
from flask import (Flask,render_template,jsonify,request,redirect)


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


app = Flask(__name__)


# create route that renders index.html template
@app.route("/", methods=['GET'])
def get_home():
    return render_template("Project_2.html")

@app.route("/page_two", methods=['GET'])
def get_page_two():
    return render_template("page_two.html")

if __name__ == "__main__":
    app.run()
