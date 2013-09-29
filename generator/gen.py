import json
def htmlfromfile(fw, fileloc):
    ab = open(fileloc, "r")
    fw.write(ab.read())
    ab.close()
    
def parsor(x):
    if(x[0]!='['):
        return x[0:2] + u"<sup>" + x[2] + u"</sup>"
    ax = x.split()
    ans = ax[0]
    for i in ax[1:]:
        ans += u" " + i[0:2] + u"<sup>" + i[2:] + u"</sup>"
    return ans

datafile = open("data/elements.en.json")    
data = json.load(datafile)
f1 = open("../index.html", "w")
htmlfromfile(f1, "template/head.html")
group = [0,1,18,1,2,13,14,15,16,17,18,1,2,13,14,15,16,17,18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
period = [0,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
block =  [0,1,1,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,1,1,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,1,1,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2]
btrans = [u'l', u's', u'p', u'd', u'f']
for i in range(len(group)):
    group[i]=u""+str(group[i])
for i in range(len(period)):
    period[i]=u""+str(period[i])
for i in range(len(block)):
    block[i]=btrans[block[i]]
print(len(group))
print(len(period))
print(len(block))

a = [0]
for i in data.keys():
    a.append(int(i))
a=sorted(a)
for j in a[1:2]:
    i=u""+str(j)
    f1.write('''<div id="element'''+i+'''" class="element group'''+group[j]+''' period'''+period[j]+''' block'''+block[j]+'''">
            <div class="eatomicnumber">'''+i+'''</div>
            <div class="eelectronicconfig">'''+parsor(data[i]["electronic_configuration"])+'''</div>
            <div class="esymbol">'''+data[i]["symbol"]+'''</div>
            <div class="ename">'''+data[i]["name"]+'''</div>
            <div class="erelativeweight">'''+data[i]["atomic_weight"]+'''</div>
        </div>\n''')
f1.write('<div class="element blank">0</div>\n'*16)

for j in a[2:5]:
    i=u""+str(j)
    f1.write('''<div id="element'''+i+'''" class="element group'''+group[j]+''' period'''+period[j]+''' block'''+block[j]+'''">
            <div class="eatomicnumber">'''+i+'''</div>
            <div class="eelectronicconfig">'''+parsor(data[i]["electronic_configuration"])+'''</div>
            <div class="esymbol">'''+data[i]["symbol"]+'''</div>
            <div class="ename">'''+data[i]["name"]+'''</div>
            <div class="erelativeweight">'''+data[i]["atomic_weight"]+'''</div>
        </div>\n''')
f1.write('<div class="element blank">0</div>\n'*10)

for j in a[5:13]:
    i=u""+str(j)
    f1.write('''<div id="element'''+i+'''" class="element group'''+group[j]+''' period'''+period[j]+''' block'''+block[j]+'''">
            <div class="eatomicnumber">'''+i+'''</div>
            <div class="eelectronicconfig">'''+parsor(data[i]["electronic_configuration"])+'''</div>
            <div class="esymbol">'''+data[i]["symbol"]+'''</div>
            <div class="ename">'''+data[i]["name"]+'''</div>
            <div class="erelativeweight">'''+data[i]["atomic_weight"]+'''</div>
        </div>\n''')
f1.write('<div class="element blank">0</div>\n'*10)

for j in a[13:57]:
    i=u""+str(j)
    f1.write('''<div id="element'''+i+'''" class="element group'''+group[j]+''' period'''+period[j]+''' block'''+block[j]+'''">
            <div class="eatomicnumber">'''+i+'''</div>
            <div class="eelectronicconfig">'''+parsor(data[i]["electronic_configuration"])+'''</div>
            <div class="esymbol">'''+data[i]["symbol"]+'''</div>
            <div class="ename">'''+data[i]["name"]+'''</div>
            <div class="erelativeweight">'''+data[i]["atomic_weight"]+'''</div>
        </div>\n''')
f1.write('<div class="element blank">0</div>\n')

for j in a[72:89]:
    i=u""+str(j)
    f1.write('''<div id="element'''+i+'''" class="element group'''+group[j]+''' period'''+period[j]+''' block'''+block[j]+'''">
            <div class="eatomicnumber">'''+i+'''</div>
            <div class="eelectronicconfig">'''+parsor(data[i]["electronic_configuration"])+'''</div>
            <div class="esymbol">'''+data[i]["symbol"]+'''</div>
            <div class="ename">'''+data[i]["name"]+'''</div>
            <div class="erelativeweight">'''+data[i]["atomic_weight"]+'''</div>
        </div>\n''')
f1.write('<div class="element blank">0</div>\n')

for j in a[104:119]:
    i=u""+str(j)
    f1.write('''<div id="element'''+i+'''" class="element group'''+group[j]+''' period'''+period[j]+''' block'''+block[j]+'''">
            <div class="eatomicnumber">'''+i+'''</div>
            <div class="eelectronicconfig">'''+parsor(data[i]["electronic_configuration"])+'''</div>
            <div class="esymbol">'''+data[i]["symbol"]+'''</div>
            <div class="ename">'''+data[i]["name"]+'''</div>
            <div class="erelativeweight">'''+data[i]["atomic_weight"]+'''</div>
        </div>\n''')
f1.write('<div class="element blank">0</div>\n'*21)

for j in a[57:72]:
    i=u""+str(j)
    f1.write('''<div id="element'''+i+'''" class="element group'''+group[j]+''' period'''+period[j]+''' block'''+block[j]+'''">
            <div class="eatomicnumber">'''+i+'''</div>
            <div class="eelectronicconfig">'''+parsor(data[i]["electronic_configuration"])+'''</div>
            <div class="esymbol">'''+data[i]["symbol"]+'''</div>
            <div class="ename">'''+data[i]["name"]+'''</div>
            <div class="erelativeweight">'''+data[i]["atomic_weight"]+'''</div>
        </div>\n''')
f1.write('<div class="element blank">0</div>\n'*3)

for j in a[89:104]:
    i=u""+str(j)
    f1.write('''<div id="element'''+i+'''" class="element group'''+group[j]+''' period'''+period[j]+''' block'''+block[j]+'''">
            <div class="eatomicnumber">'''+i+'''</div>
            <div class="eelectronicconfig">'''+parsor(data[i]["electronic_configuration"])+'''</div>
            <div class="esymbol">'''+data[i]["symbol"]+'''</div>
            <div class="ename">'''+data[i]["name"]+'''</div>
            <div class="erelativeweight">'''+data[i]["atomic_weight"]+'''</div>
        </div>\n''')



htmlfromfile(f1, "template/foot.html")
f1.close()
