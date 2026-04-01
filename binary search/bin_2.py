"""
Given a sorted and rotated array arr[] of distinct elements, find the index of given key in the array. If the key is not present in the array, return -1.
Examples:  
Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
Output: 8
Explanation: 3 is present at index 8.
Input: arr[] = [3, 5, 1, 2], key = 6
Output: -1
Explanation: 6 is not present.
Input: arr[] = [33, 42, 72, 99], key = 42
Output: 1
Explanation: 42 is found at index 1.
"""
import sys
def solve():
    inp = list(map(int, sys.stdin.read().split()))
    key = inp[0]
    del inp[0:1]
    ans = sort_rot(key, inp)
    print(ans)
def sort_rot(key, inp):
    l = 0
    h = len(inp) - 1
    while l<=h:
        mid = (l+h)//2

        if inp[mid] == key:
            return (mid)
        if inp[l] <= inp[mid]:
            if inp[l] <= key < inp[mid]:
                h = mid - 1
            else:
                l = mid + 1
        else:
            if inp[mid] < key <=inp[h]:
                l = mid + 1
            else:
                h = mid - 1
    return -1
solve()

"""
def search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
        
        # Step 1: Identify which half is sorted
        if arr[low] <= arr[mid]:  # Left half is sorted
            # Step 2: Check if key is in this sorted half
            if arr[low] <= key < arr[mid]:
                high = mid - 1 # Go left
            else:
                low = mid + 1  # Go right
        else:  # Right half must be sorted
            # Step 2: Check if key is in this sorted half
            if arr[mid] < key <= arr[high]:
                low = mid + 1  # Go right
            else:
                high = mid - 1 # Go left
                
    return -1
"""
