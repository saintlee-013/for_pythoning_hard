"""
Given a number n containing only 1 set bit in its binary representation, the task is to find the position of the only set bit. If there are 0 or more than 1 set bits, then return -1.
Note: Position of set bit '1' should be counted starting with 1 from the LSB side in the binary representation of the number.
Input: n = 2
Output: 2
Explanation: Binary representation of 2 is 10. We can observe that the only set bit is at position 2 from LSB.
Input: n = 5
Output: -1
Explanation: Binary representation of 5 is 101. There are 2 set bits, so return -1.
"""
import sys
inp = sys.stdin.read().split()
n = int(inp[0])

"""
my pathetic brute force attempt:
l = []
l = [int(x) for x in list(bin(n)[2:])]
res = 0
for ele in l:
    res ^= ele
# res is the thing repeated odd number of times
if res == 1:
    print("-1")
else:
"""
    
    
    
