from flask import Flask, render_template
from catalog_utils import gen_catalog
import json

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/gen_catalog")
def initalize():
	global cat
	cat = gen_catalog()
	return json.dumps(cat)

@app.route("/entries/<pulsar_name>")
def get_entry(pulsar_name):
	pulsar = [p for p in cat["entries"] if p["Name"] == pulsar_name][0]
	return render_template("entry.html", pulsar=pulsar)