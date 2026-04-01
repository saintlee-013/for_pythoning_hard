l = []
l2 = []
l3 = []

bi = 0
limit = int(input("Enter the number of elements in the list: "))
for i in range(limit):
    ele = int(input(f"Enter the {i+1}th element : "))
    l.append(ele)
    bi = f"{ele:08b}"
    l2.append((bi))
    l3.append(int(bi))
print(l)
print(l2)
print(*l2)
print(l3)
    




"""
n = int(input("Enter a numbe to be conveted to binary: "))
count = 1
bi = 0
rem = 0
while n!=0:
    rem = n%2
    bi = bi + rem*count
    count = count*10
    n = n//2
print(bi)
"""   
