import pickle
import math
from collections import OrderedDict

def gen_catalog(prestring):
	catalog = {"entries":[]}
	entries = catalog["entries"]

	file = open("psrcat.db", "r")
	line = file.readline()
	curr = None
	while line:
	    if line[0] == "#":
	        line = file.readline()
	        continue
	    if line[0] == "@":
	        smaller_length = min(len(prestring), len(curr["PSRJ"][0]))
	        if (smaller_length == 0 or prestring[0:smaller_length] == curr["PSRJ"][0][0:smaller_length]) and ("RAJ" in curr.keys()):  #temp fix, will want to convert ecliptic coords to raj and decj
	        	entries.append(curr)
	        curr = None
	        line = file.readline()
	        continue
	    if curr == None:
	        curr = OrderedDict()
	    row = line.split()
	    curr[row[0]] = row[1:len(row)]
	    line = file.readline()

	catalog["entries_per_page"] = 10 #to be selectable
	catalog["pages"] = math.ceil(len(catalog["entries"]) / catalog["entries_per_page"])
	catalog["curr_page"] = 1

	return catalog

def render_catalog(catalog):
	print("<table><tr><th>JName</th><th>RA</th><th>Dec</th></tr>")
	start = (catalog["curr_page"] - 1) * catalog["entries_per_page"]
	end = min(start + catalog["entries_per_page"], len(catalog["entries"]))
	for i in range(start, end):
		entry = catalog["entries"][i]
		print("<tr><td>" + entry["PSRJ"][0] + "</td><td>" + entry["RAJ"][0] + "</td><td>" + entry["DECJ"][0] + "</td></tr>")
	print("</table>")

def save_catalog(catalog, filename):
	file = open(filename, "wb")
	pickle.dump(catalog, file)

def load_catalog(filename):
	file = open(filename, "rb")
	return pickle.load(file)