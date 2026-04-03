#Standard Deviation
#for which we need the Variance
import math
a = input()
b = a.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ').replace(',', ' ')
c = [s for s in b.split() if s]
v = [float(s) for s in c]
d = len(c)
sum1 = 0
sum2 = 0
avg = 0
var = 0
std = 0

for s in v:
    sum1 += s
avg = sum1/d

for s in v:
    sum2 = sum2 + (s - avg)*(s - avg)

var = sum2/d
std = math.sqrt(var)

print(std)
