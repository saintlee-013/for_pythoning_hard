d = {'1':500, '3':800}
d1 = []
d1 = (d.keys())
d2 = []
for key in d.keys():
    d2.append(int(key.strip().strip("'").strip('"')))
print(d2)    
d3 = d.values()
print(d3)
