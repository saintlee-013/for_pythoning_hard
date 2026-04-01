"""
Given a positive integer n, check whether it is a power of 2 or not.
Examples: 
Input : n = 16
Output :  true
Explanation: 24 = 16 
Input : n = 42
Output :  false
Explanation: 42 is not a power of 2
Input : n = 1
Output : true
Explanation: 20 = 1
"""
import sys
inp = sys.stdin.read().split()
n = int(inp[0])
bi = bin(n)[2:]
if n.bit_count() == 1:
    print("true")
else:
    print("false")

"""
if n>0 and n&(n-1)==0:
  true
"""
