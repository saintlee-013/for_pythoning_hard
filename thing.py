s = "ab cd ef"
o = (1,0,2)
ls = (s.split(" "))
d = { 0: ls[0], 1:ls[1], 2:ls[2]}
print(d)
d1 = {1:ls[0], 0:ls[1], 2:ls[2]}
print(d1)
l = []
l = list(d1.values())
print(l)
print(" ".join(l))
