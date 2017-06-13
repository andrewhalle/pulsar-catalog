from Catalog import gen_catalog

cat = gen_catalog()
for entry in cat["entries"]:
	file = open("entries/" + entry["PSRJ"] + ".html", "w")
	html = "<!DOCTYPE html><html><head><title>" + entry["PSRJ"] + "</title></head><body>"
	html += "<h1>" + entry["PSRJ"] + "</h1>"  #JName header
	for item in entry["sources"]["ATNF"].keys():
		if item != "PSRJ":
			html += "<p>" + item + "    "
			for value in entry["sources"]["ATNF"][item]:
				html += value + "    "
			html += "</p>"
	html += "</body></html>"
	file.write(html)
	file.close()