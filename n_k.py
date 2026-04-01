"""
Given a number n and a bit position k, check if the kth bit of n is set or not. A bit is called set if it is 1 at that position. 
Note: Indexing starts with 0 from LSB (least significant bit) side in the binary representation of the number.
Examples: 
Input: n = 7, k = 2
Output: true
Explanation: 7 is represented as 111 in binary and bit at position 2 is set.
Input: n = 5, k = 1
Output:  false
Explanation: 5 is represented as 101 in binary and bit at position 1 is not set.
"""
import sys
inp = sys.stdin.read().split()

n = int(inp[0])
k = int(inp[1])
if ((n>>k)&1) == 1:
    print("true")
else:
    print("false")
