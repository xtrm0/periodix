import json
f1 = open("out.json", 'w')
datafile = open("data/source.json")
data = json.load(datafile)
f1.write("{")
for i in data.keys()[0:0]:
    f1.write('''
    "'''+ str(data[i]["atomic_number"]) + '''": {
        "name": "'''+ str(i) + '''",
        "symbol": "'''+ str(data[i]["symbol"]) + '''",
        "Z": "'''+ str(data[i]["atomic_number"]) + '''",
        "atomic_weight": "'''+ str(data[i]["atomic_weight"]) + '''",
        "atomic_radius": "'''+ str(data[i]["atomic_radius pm"]) + '''",
        "pauling_negativity": "'''+ str(data[i]["pauling_negativity"]) + '''",
        "electronic_configuration": "'''+ str(data[i]["electronic_configuration"]) + '''",
        "Default" : {
        
        },
        "Isotopes": {
        
        }
    }''')
    
for i in data.keys()[1:]:
    f1.write(''',
    "'''+ str(data[i]["atomic_number"]) + '''": {
        "name": "'''+ str(i) + '''",
        "symbol": "'''+ str(data[i]["symbol"]) + '''",
        "Z": "'''+ str(data[i]["atomic_number"]) + '''",
        "atomic_weight": "'''+ str(data[i]["atomic_weight"]) + '''",
        "atomic_radius": "'''+ str(data[i]["atomic_radius pm"]) + '''",
        "pauling_negativity": "'''+ str(data[i]["pauling_negativity"]) + '''",
        "electronic_configuration": "'''+ str(data[i]["electronic_configuration"]) + '''",
        "Default" : {
        
        },
        "Isotopes": {
        
        }
    }''')
    
f1.write("\n}");
data.close()