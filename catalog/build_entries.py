from Catalog import gen_catalog

cat = gen_catalog()
for entry in cat["entries"]:
	file = open("entries/" + entry["Name"].replace("/", "-") + ".html", "w")
	html = "<!DOCTYPE html><html><head><title>" + entry["Name"] + "</title></head><body>"
	html += "<h1>Name: " + entry["Name"] + "</h1>"  #Name header
	html += "<h2>RA: " + entry["RA"] + "</h2>"    #RA header
	html += "<h2>DEC: " + entry["DEC"] + "</h2>"   #DEC header
	for source in sorted(list(entry["sources"].keys())):
		html += "<h3>Source: " + source + "</h3>"
		for item in sorted(list(entry["sources"][source].keys())):
			html += "<p>" + item + ": " + str(entry["sources"][source][item]) + "</p>"
	html += "</body></html>"
	file.write(html)
	file.close()