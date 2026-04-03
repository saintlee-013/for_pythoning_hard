obs = input()
obsclean = obs.replace('\n',' ').replace(',',' ').replace('\r',' ').replace('\t',' ')
lobs = [ob for ob in obsclean.split(' ') if ob]
lobsf = [float(ob) for ob in lobs]

sumtotal = 0 
for number in lobsf:
    sumtotal = sumtotal + number
print(f"Sum Total: {sumtotal}")
count = len(lobsf)
if count!=0:
    avg = sumtotal/count
    print(f"The Mean is: {avg:.10f}")
else:
    print("some error dude")

