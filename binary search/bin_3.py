"""
Given a sorted array of distinct elements arr[] of size n that is rotated at some unknown point, the task is to find the minimum element in it. 
Examples: 
Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
Explanation: 1 is the minimum element present in the array.
Input: arr[] = [3, 1, 2]
Output: 1
Explanation: 1 is the minimum element present in the array.
Input: arr[] = [4, 2, 3]
Output: 2
Explanation: 2 is the only minimum element in the array.
"""
import sys
def solve():
    inp = list(map(int, sys.stdin.read().split()))
    ans =  min_sort_rot(inp)
    print(ans)
def min_sort_rot(inp):
    l = 0
    h = len(inp) - 1
    ans = 0
    if inp[l] <= inp[h]:
        return inp[l]
    while l<h:
        mid = (l+h)//2
        if inp[mid] > inp[h]:
            l = mid  + 1
        else:
            h = mid
    return inp[l]
            
solve()

"""
import sys

def min_sort_rot(inp):
    if not inp: return -1
    
    l = 0
    h = len(inp) - 1
    
    # If the array is NOT rotated at all, the first element is the min
    if inp[l] <= inp[h]:
        return inp[l]
    
    # Standard Binary Search for the "drop-off" point
    while l < h:
        mid = (l + h) // 2
        
        # If mid is bigger than the end, the drop-off is to the right
        if inp[mid] > inp[h]:
            l = mid + 1
        # Otherwise, mid could be the min, or the min is to the left
        else:
            h = mid # Notice: NOT mid - 1
            
    return inp[l]

def solve():
    # Example input: 5 6 1 2 3 4
    data = sys.stdin.read().split()
    if not data:
        return
    inp = list(map(int, data))
    
    ans = min_sort_rot(inp)
    print(ans)

if __name__ == "__main__":
    solve()
"""
