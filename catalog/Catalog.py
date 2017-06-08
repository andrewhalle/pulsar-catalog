import json
import math
from collections import OrderedDict

def gen_catalog():
	#build catalog dictionary
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
	        if "RAJ" in curr.keys():  #temp fix, will want to convert ecliptic coords to raj and decj
	        	entries.append(curr)
	        curr = None
	        line = file.readline()
	        continue
	    if curr == None:
	        curr = OrderedDict()
	        curr["visible"] = True;
	    row = line.split()
	    curr[row[0]] = row[1:len(row)]
	    line = file.readline()

	catalog["entries_per_page"] = 10 #to be selectable
	catalog["pages"] = math.ceil(len(catalog["entries"]) / catalog["entries_per_page"])
	catalog["curr_page"] = 1

	return catalog

cat = gen_catalog()
print(json.dumps(cat))