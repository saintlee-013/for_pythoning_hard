"""
Given two numbers n and d where d is a power of 2 number, the task is to perform n modulo d without the division and modulo operators.
Input: 6 4
Output: 2 
Explanation: As 6%4 = 2
Input: 12 8
Output: 4
Explanation: As 12%8 = 4
Input: 10 2
Output: 0
Explanation: As 10%2 = 0
"""
import sys
inp = sys.stdin.read().split()
T = int(inp[0])
for i in range(1, len(inp)-1, 2):
    n  = int(inp[i])
    d  = int(inp[i+1])
    #make a sieve, which would be d-1
    #now use that sieve with &
    # remmber this works only because d is a power of 2
    ans = n & (d-1)
    print(ans)
    
"""
output:
3
6 4
12 8 
10 2
2
4
0
"""
