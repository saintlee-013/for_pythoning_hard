#Given a list of items, create a dictionary with the indices as keys and the items as items.
names1 = ["Alice", "Bob", "Charlie", "David"]
d : dict = {}
for i in range(len(names1)):
    d[i] = names1[i]
print(d)
#Remove First two and Last two Chars from a string
a = "sanchita" #nchi
a1 = a[2:-2]
print(a1)
