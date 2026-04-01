"""
Given a 0 based sorted array arr[] of distinct integers and an integer k, find the index of k if it is present.
If not, return the index where k should be inserted to maintain the sorted order.
Examples: 
Input: arr[] = [1, 3, 5, 6], k = 5
Output: 2
Explanation: Since 5 is found at index 2 as arr[2] = 5, the output is 2.
Input: arr[] = [1, 3, 5, 6], k = 2
Output: 1
Explanation: The element 2 is not present in the array, but inserting it at index 1 will maintain the sorted order.
"""
import sys
import bisect 
def solve():
    inp = list(map(int,sys.stdin.read().split()))
    k = inp[0]
    del inp[0:1]
    BS(inp, k)
    print(inp)
    print(k)
def BS(L, k):
    idx = bisect.bisect_left(L,k)
    if idx < len(L) and L[idx] == k:
        print(idx)
solve()
s
