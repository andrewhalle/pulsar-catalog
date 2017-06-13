from collections import OrderedDict

def gen_catalog():
	#build catalog dictionary
	catalog = {"entries":[]}
	entries = catalog["entries"]

	#ATNF Pulsar Database
	file = open("psrcat.db", "r")
	line = file.readline()
	curr = None
	while line:
	    if line[0] == "#":
	        line = file.readline()
	        continue
	    if line[0] == "@":
	        if "RAJ" in curr.keys():  #temp fix, will want to convert ecliptic coords to raj and decj
	        	new_curr = {"PSRJ":curr["PSRJ"][0], "RAJ":curr["RAJ"][0], "DECJ":curr["DECJ"][0], "visible": True, "sources": {"ATNF":curr}}
	        	entries.append(new_curr)
	        curr = None
	        line = file.readline()
	        continue
	    if curr == None:
	        curr = OrderedDict()
	    row = line.split()
	    curr[row[0]] = row[1:len(row)]
	    line = file.readline()
	file.close()


	# #RRATalog
	file = open("rratalog.txt", "r")
	line = file.readline()
	line = file.readline()
	while line:
		line = line.split()
		curr = OrderedDict()
		curr["Name"] = line[0]
		curr["P"] = line[1]
		curr["Pdot"] = line[2]
		curr["DM"] = line[3]
		curr["RA"] = line[4]
		curr["DEC"] = line[5]
		curr["l"] = line[6]
		curr["b"] = line[7]
		curr["Rate"] = line[8]
		curr["logB"] = line[9]
		curr["logts"] = line[10]
		curr["Dhat"] = line[11]
		curr["FluxD"] = line[12]
		curr["Pulse Width"] = line[13]
		curr["Survey"] = line[14]
		if curr["Name"] in [x["PSRJ"] for x in catalog["entries"]]:
			entry = [x for x in catalog["entries"] if x["PSRJ"] == curr["Name"]][0]
			entry["sources"]["RRATalog"] = curr
		else:
			catalog["entries"].append({"PSRJ":curr["Name"], "RAJ":curr["RA"], "DECJ":curr["DEC"], "visible":True, "sources":{"RRATalog":curr}})
		line = file.readline()
	file.close()

	catalog["entries"].sort(key=lambda x: x["PSRJ"])
	return catalog