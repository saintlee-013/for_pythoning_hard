"""
Given a number n and a value k. From the right, set the kth bit in the binary representation of n. The position of LSB(or last bit) is 0, second last bit is 1 and so on.
Also, 0 <= k < x, where x is the number of bits in the binary representation of n.
Examples: 
Input : n = 10, k = 2
Output : 14
(10)10 = (1010)2
Now, set the 2nd bit from right.
(14)10 = (1110)2
2nd bit has been set.
Input : n = 15, k = 3
Output : 15
3rd bit of 15 is already set.
"""
import sys
inp = sys.stdin.read().split()
n = int(inp[0])
k = int(inp[1])
num_k = 1 << k
ans = n | num_k
print(bin(n)[2:])
print(bin(ans)[2:])
print(ans)
