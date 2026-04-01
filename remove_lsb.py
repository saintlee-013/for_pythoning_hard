#Given an integer n, remove/turn off the rightmost set bit in it.
n = int(input())
ans = n & (n-1)
print(bin(n)[2:])
print(bin(ans)[2:])
print(ans)
