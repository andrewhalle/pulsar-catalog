from flask import Flask, request, render_template
from catalog_utils import gen_catalog
from webcrawler import *
import json

app = Flask(__name__)
cat = gen_catalog()

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/gen_catalog")
def initalize():
	return json.dumps(cat)

@app.route("/versioning", methods=["GET"])
def versioning():
	catalog = request.args["catalog"]
	if catalog == "ATNF":
		return get_ATNF_version()

@app.route("/render-version-box", methods=["GET"])
def render_version_box():
	is_curr = request.args["isCurrent"]
	catalog = request.args["catalog"]
	if is_curr:
		return render_template("version-box.html", image="check.png", text=catalog+" is up-to-date.")

@app.route("/entries/<pulsar_name>")
def get_entry(pulsar_name):
	pulsar = [p for p in cat["entries"] if p["Name"] == pulsar_name][0]
	return render_template("entry.html", pulsar=pulsar)