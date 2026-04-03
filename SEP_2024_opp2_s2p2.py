"""Given a sequence of n strings as input, create a final word by appending and prepending the strings alternately based on their order.
Strings at even indices (0-based) are appended to the end, while strings at odd indices are prepended to the beginning."""
n = int(input())
le=[]
lo=[]
for i in range(n):
    element = input()
    if(i%2==0):
        le.append(element)
    else:
        lo.append(element)
lr = []
lr = lo[::-1]
la = lr+le
str1 = "".join(la)
print(str1)
