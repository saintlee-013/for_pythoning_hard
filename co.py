#CoVariance
a1 = input()
b1 = a1.replace('\n',' ').replace(',',' ').replace('\t',' ').replace('\r',' ')
c1 = [s for s in b1.split() if s]
d1 = [float(s) for s in c1]
e1 = len(d1)
a2 = input()
b2 = a2.replace('\n',' ').replace(',',' ').replace('\t',' ').replace('\r',' ')
c2 = [s for s in b2.split() if s]
d2 = [float(s) for s in c2]
e2 = len(d2)
sum1 = 0
sum2 = 0
for s in d1:
    sum1 += s
avg1 = sum1/e1
for s in d2:
    sum2 += s
avg2 = sum2/e2

print(f"sum for 1st one is {sum1}")
print(f"sum for 2nd one is {sum2}")
print(f"avg for 1st one is {avg1}")
print(f"avg for 2st one is {avg2}")

m = 0
re = (1/e1)
for s in d1:
    for t in d2:
     m = m + ((s-avg1)*(t-avg2))

cov = re*m
print(cov)
