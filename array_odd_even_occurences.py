"""
Given an array arr[] of positive integers. All numbers occur an even number of times except one number which occurs an odd number of times.
Examples : 
Input : arr[]= [1, 2, 3, 2, 3, 1, 3]
Output : 3
Input : arr[] = [5, 7, 2, 7, 5, 2, 5]
Output : 5
"""
import sys
inp = sys.stdin.read().split()
arr = [int(x) for x in inp]
res = 0
for i in arr:
    res = res ^ i
print(res)
