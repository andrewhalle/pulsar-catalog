from Catalog import *
import sys

def search_bar_change(prestring):
	catalog = gen_catalog(prestring)
	render_catalog(catalog)
	save_catalog(catalog, "curr.cat")

def page_next():
	catalog = load_catalog("curr.cat")
	catalog["curr_page"] += 1
	render_catalog(catalog)
	save_catalog(catalog, "curr.cat")

def page_prev():
	catalog = load_catalog("curr.cat")
	catalog["curr_page"] -= 1
	render_catalog(catalog)
	save_catalog(catalog, "curr.cat")

if len(sys.argv) == 3:
	prestring = sys.argv[2]
	func = sys.argv[1]
	if func == "search_bar_change":
		search_bar_change(prestring)
	elif func == "page_next":
		page_next()
	elif func == "page_prev":
		page_prev()
else:
	func = sys.argv[1]
	if func == "search_bar_change":
		search_bar_change("")
	elif func == "page_next":
		page_next()
	elif func == "page_prev":
		page_prev()
