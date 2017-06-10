import json
from Catalog import gen_catalog

cat = gen_catalog()
print(json.dumps(cat))