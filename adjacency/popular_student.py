"""
The Scenario:
You are given a social network of N students (numbered 1 to N). 
There are M friendships.

A student is "Super Popular" if they are friends with more than half of the people in the school.

Input: N (number of students) and M (number of friendships). M lines, each containing two integers u and v representing a friendship between student u and v.
Task : Represent this using an Adjacency List.
Output : the IDs of all "Super Popular" students in ascending order.
Constraints for your test:N = 10^5, M = 2*10^5.
Input :
5 6
1 2
1 3
2 3
2 4
2 5
4 5
Output: 2
"""
import sys

def solve():
    # 1. Get the data
    inp = list(map(int, sys.stdin.read().split()))
    if not inp: return
    
    N, M = inp[0], inp[1]
    edges = inp[2:] # Everything after N and M are the friendships
    
 
    AList = [[] for _ in range( N + 1)]
    
    # 3. Fill the list by jumping 2 at a time
    for i in range(0, len(edges), 2):
        u = edges[i]
        v = edges[i+1]
        
        # Add to BOTH because friendship is mutual
        AList[u].append(v)
        AList[v].append(u)
        
    print(AList[1:])
    # Assuming your list is called AList and N is the number of students
    threshold = (N - 1) / 2
    super_popular = []

    # Start from 1 to skip that empty 0 index
    for student_id in range(N + 1):
    # The number of friends is just the length of their list!
        num_friends = len(AList[student_id])
    
        if num_friends > threshold:
            super_popular.append(student_id)
    print(int(super_popular[0]))
    
    
    
# [[2, 3], [1, 3, 4, 5], [1, 2], [2, 5], [2, 4]]


solve()
"""
some wrong bs code: my attempt!
import sys
def solve():
    inp = list(map(int, sys.stdin.read().split()))
    N = inp[0]
    M = inp[1]
    del inp[0:2]
    t = ()
    AList = {}
    for i in inp:
        (u,v) = (i,i+1)
        i = i + 2
    for j in range(1, len(inp)):
        AList[j] = []
    for (k,l) in AList:
        AList[k].append(l)
    print(AList)
solve()
"""
"""  # 2. Initialize the Dictionary with N students
    AList = []
    for i in range(1, N + 1):
        AList[i] = []"""
