n = 1234
count = 0
sum1 = 0
while(n!=0):
    rem = n%10
    count = count+1
    sum1 = sum1 + rem
    n = n//10
print(sum1)
print(count)
