import json
from pprint import pprint
datafile = open("data/elements.en.json")
data = json.load(datafile)
pprint(data)
for i in data["elements"]:
    





data.close()