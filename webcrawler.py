import requests
import re

def get_ATNF_version():
	r = requests.get("http://www.atnf.csiro.au/people/pulsar/psrcat/")
	p = re.compile('name="version" value="([^"]+)')
	m = p.search(r.text)
	return m.group(1)