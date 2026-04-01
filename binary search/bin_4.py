"""
Given an array arr[] where no two adjacent elements are same, find the index of a peak element.
An element is considered to be a peak element if it is strictly greater than its adjacent elements. If there are multiple peak elements, return the index of any one of them.
Note: Consider the element before the first element and the element after the last element to be negative infinity.
Examples:
Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 5
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
Input: arr[] = [10, 20, 15, 2, 23, 90, 80]
Output: 1
Explanation: Element 20 at index 1 is a peak since 10 < 20 > 15. Index 5 (value 90) is also a peak, but returning any one peak index is valid.
"""
import sys
def solve():
    inp = list(map(int, sys.stdin.read().split()))
    ans = peak(inp)
    print(ans)
def peak(inp):
    l = 0
    h = len(inp) - 1
    
    while l <= h:
        mid = (l + h) // 2
        
        # Check neighbors (using -infinity for out-of-bounds)
        left = inp[mid-1] if mid > 0 else float('-inf')
        right = inp[mid+1] if mid < len(inp)-1 else float('-inf')
        
        if left < inp[mid] > right:
            return mid # Found the peak!
            
        if inp[mid] < right:
            # The right neighbor is higher, so a peak MUST be to the right.
            # We jump our "low" pointer all the way to mid + 1.
            l = mid + 1
        else:
            # The left neighbor is higher (or equal), go left.
            h = mid - 1
            
    return l
solve()
"""
import sys
def solve():
    inp = list(map(int, sys.stdin.read().split()))
    ans = peak(inp)
    print(ans)
def peak(inp):
    l = 0
    h = len(inp) - 1
    c = True
    mid = (l+h)//2
    while c:
        
        if  mid <= l or mid >= h:
            c = False
        else:
            if inp[mid-1] < inp[mid]> inp[mid+1]:
                return mid
            elif inp[mid]<inp[mid+1]:
                mid = mid + 1
            else:
                mid = mid - 1
    return -1
solve()
"""
