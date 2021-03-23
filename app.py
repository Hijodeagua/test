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
    return render_template("test.html")


@app.route("/api/project")
def project():
    results = db.session.query(project.brewery,project.name, project.lat, project.lon).all()

    hover_text = [result[1] for result in results]
    lat = [result[2] for result in results]
    lon = [result[3] for result in results]

    project_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": lat,
        "lon": lon,
        "text": hover_text,
        "hoverinfo": "text",
        "marker": {
            "size": 20,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(project_data)

if __name__ == "__main__":
    app.run()
