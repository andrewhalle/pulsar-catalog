from Catalog import gen_catalog

cat = gen_catalog()
for entry in cat["entries"]:
	file = open("entries/" + entry["PSRJ"][0] + ".html", "w")
	html = "<!DOCTYPE html><html><head><title>" + entry["PSRJ"][0] + "</title></head><body>"
	html += "<h1>" + entry["PSRJ"][0] + "</h1>"  #JName header
	for item in entry.keys():
		if item != "PSRJ" and item != "visible":
			html += "<p>" + item + "    "
			for value in entry[item]:
				html += value + "    "
			html += "</p>"
	html += "</body></html>"
	file.write(html)
	file.close()