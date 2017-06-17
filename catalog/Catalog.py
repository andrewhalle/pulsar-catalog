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
	        	new_curr = {"Name":curr["PSRJ"][0], "RA":curr["RAJ"][0], "DEC":curr["DECJ"][0], "visible": True, "sources": {"ATNF":curr}}
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


	#RRATalog
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
		if curr["Name"] in [x["Name"] for x in catalog["entries"]]:
			entry = [x for x in catalog["entries"] if x["Name"] == curr["Name"]][0]
			entry["sources"]["RRATalog"] = curr
		else:
			catalog["entries"].append({"Name":curr["Name"], "RA":curr["RA"], "DEC":curr["DEC"], "visible":True, "sources":{"RRATalog":curr}})
		line = file.readline()
	file.close()

	#Parallaxes
	file = open("Parallaxes.txt", "r")
	line = file.readline()
	curr = None
	while line:
		if line[0] == "#":
			line = file.readline()
			continue
		elif line[0] == "!":
			if curr == None:
				curr = OrderedDict()
				line = file.readline()
			else:
				if curr["JName"] in [x["Name"] for x in catalog["entries"]]:
					entry = [x for x in catalog["entries"] if x["Name"] == curr["JName"]][0]
					entry["sources"]["Parallaxes"] = curr
				else:
					catalog["entries"].append({"Name":curr["JName"], "RA":"--", "DEC":"--", "visible":True, "sources":{"Parallaxes":curr}})
				line = file.readline()

		else:
			if line[0:5] == "JName":
				line = line.split(" = ")
				curr["JName"] = line[1].strip()
				line = file.readline()
				line = line.split(" = ")
				if len(line) == 1:
					curr["BName"] = "--"
				else:
					curr["BName"] = line[1].strip()
				curr["PIs"] = OrderedDict()
				line = file.readline()
			else:
				line = line.split(" = ")
				currPI = line[1].strip()
				curr["PIs"][currPI] = OrderedDict()
				line = file.readline()
				while line[0] != "#" and line[0:2] != "PI":
					line = line.split(" = ")
					curr["PIs"][currPI][line[0]] = line[1].strip()
					line = file.readline()
	file.close()


	#GCpsr
	file = open("GCpsr.txt", "r")
	line = file.readline()
	currGC = None
	while line:
		if line[0] == "#" or line == "\n":
			line = file.readline()
			continue
		elif line[0] == "J" or line[0] == "B":
			line = line.split()
			curr = OrderedDict()
			curr["Name"] = line[0]
			curr["Offset"] = line[1]
			curr["Period"] = line[2]
			curr["dP/dt"] = line[3]
			curr["DM"] = line[4]
			curr["Pb"] = line[5]
			curr["x"] = line[6]
			curr["e"] = line[7]
			curr["m2"] = line[8]
			curr["GC"] = currGC
			if curr["Name"] in [x["Name"] for x in catalog["entries"]]:
				entry = [x for x in catalog["entries"] if x["Name"] == curr["Name"]][0]
				entry["sources"]["GCpsr"] = curr
			else:
				catalog["entries"].append({"Name":curr["Name"], "RA":"--", "DEC":"--", "visible":True, "sources":{"GCpsr":curr}})
			line = file.readline()
		else:
			currGC = line
			line = file.readline()

	file.close()


	catalog["entries"].sort(key=lambda x: x["Name"])
	return catalog