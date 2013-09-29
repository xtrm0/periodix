import json
def X(abc):
    return unicode(str(abc))
f1 = open("out.json", 'w')
datafile = open("data/source2.json")
data = json.load(datafile)
data=data["PERIODIC_TABLE"]["ATOM"]
a=[]
for i in range(0,len(data)):
    a.append([int(data[i]["ATOMIC_NUMBER"]), i])
a = sorted(a)
f1.write("{")
for j in a[0:1]:
    print j
    i = j[1]
    f1.write(u'''
    "'''+ data[i]["ATOMIC_NUMBER"] + u'''": {
        "name": "'''+ data[i]["NAME"] + u'''",
        "symbol": "'''+ data[i]["SYMBOL"] + u'''",
        "Z": "'''+ data[i]["ATOMIC_NUMBER"] + u'''",
        "atomic_weight": "'''+ data[i]["ATOMIC_WEIGHT"] + u'''",
        "atomic_radius": "'''+ data[i]["ATOMIC_RADIUS"]["VALUE"] + u'''",
        "pauling_negativity": "'''+ data[i]["ELECTRONEGATIVITY"] + u'''",
        "electronic_configuration": "'''+ data[i]["ELECTRON_CONFIGURATION"] + '''",
        "oxidation_states": "'''+ data[i]["BOILING_POINT"]["VALUE"] +'''",
        "density": "'''+ data[i]["DENSITY"]["VALUE"] +'''",
        "atomic_volume": "'''+ data[i]["ATOMIC_VOLUME"]["VALUE"] +'''",
        "specific_heat": "'''+ data[i]["SPECIFIC_HEAT_CAPACITY"]["VALUE"] +'''",
        "ionization_potential": "'''+ data[i]["IONIZATION_POTENTIAL"] +'''",
        "thermal_conductivity": "'''+ data[i]["THERMAL_CONDUCTIVITY"]["VALUE"] +'''",
        "Default": {
        
        },
        "Isotopes": {
        
        }
    }''')
    
for j in a[1:]:
    i=j[1]
    print j
    f1.write(u''',
    "'''+ data[i]["ATOMIC_NUMBER"] + u'''": {
        "name": "'''+ data[i]["NAME"] + u'''",
        "symbol": "'''+ data[i]["SYMBOL"] + u'''",
        "Z": "'''+ data[i]["ATOMIC_NUMBER"] + u'''",
        "atomic_weight": "'''+ data[i]["ATOMIC_WEIGHT"] + u'''",
        "atomic_radius": "'''+ (data[i]["ATOMIC_RADIUS"]["VALUE"] if "ATOMIC_RADIUS" in data[i] else "na")  + u'''",
        "pauling_negativity": "'''+ (data[i]["ELECTRONEGATIVITY"] if "ELECTRONEGATIVITY" in data[i] else "na") + u'''",
        "electronic_configuration": "'''+ data[i]["ELECTRON_CONFIGURATION"] + '''",
        "oxidation_states": "'''+ (data[i]["BOILING_POINT"]["VALUE"] if "BOILING_POINT" in data[i] else "na")  +'''",
        "density": "'''+ (data[i]["DENSITY"]["VALUE"]  if "DENSITY" in data[i] else "na") +'''",
        "atomic_volume": "'''+ (data[i]["ATOMIC_VOLUME"]["VALUE"]  if "ATOMIC_VOLUME" in data[i] else "na") +'''",
        "specific_heat": "'''+ (data[i]["SPECIFIC_HEAT_CAPACITY"]["VALUE"]  if "SPECIFIC_HEAT_CAPACITY" in data[i] else "na") +'''",
        "ionization_potential": "'''+ (data[i]["IONIZATION_POTENTIAL"]  if "IONIZATION_POTENTIAL" in data[i] else "na") +'''",
        "thermal_conductivity": "'''+ (data[i]["THERMAL_CONDUCTIVITY"]["VALUE"] if "THERMAL_CONDUCTIVITY" in data[i] else "na") +'''",
        "Default": {
        
        },
        "Isotopes": {
        
        }
    }''')
    
f1.write("\n}");
datafile.close()
f1.close()
