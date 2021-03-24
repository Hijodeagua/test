from models import create_classes
import os 
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("Project_2.html")

@app.route("/page_two")
def page_two():
    """go to Page two."""
    return render_template("page_two.html")

if __name__ == "__main__":
    app.run()
