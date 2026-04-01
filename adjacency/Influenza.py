"""
The Scenario: In a social media app, users can follow each other.
Following is one-way: If Alice follows Bob, it doesn't mean Bob follows Alice.
An Influencer is someone who is followed by everyone else in the app (N-1 people), but they follow nobody (0 people).
Input: Two integers N (number of users) and M (number of follow relationships).
M lines, each containing u and v, meaning user u follows user v.
Your Task:Represent this using an Adjacency List.
(Hint: Since it's one-way, only add v to u's list).
Find the ID of the Influencer.
If no such person exists, print -1.
INPUT:
3 2
1 3
2 3
OUTPUT:
3
"""
# N is the number of vertices and M is the number edges
import sys

def solve():
    inp = list(map(int, sys.stdin.read().split()))
    if not inp: return
    N, M = inp[0], inp[1]
    del inp[0:2]

    AList = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1) # New counter list

    for i in range(0, len(inp), 2):
        u = inp[i]
        v = inp[i+1]
        AList[u].append(v)
        in_degree[v] += 1 # v just gained a follower!

    # Search for the one person who fits both rules
    ans = -1
    for j in range(1, N + 1):
        # Rule 1: Follows nobody (len is 0)
        # Rule 2: Followed by everyone else (in_degree is N-1)
        if len(AList[j]) == 0 and in_degree[j] == N - 1:
            ans = j
            break # We found them, we can stop looking
            
    print(ans)

solve()

"""
why am i still coding after this bs?
import sys
def solve():
    Ans = []     
    inp = list(map(int, sys.stdin.read().split()))
    N, M = inp[0], inp[1]
    del inp[0:2]

    AList = [[] for _ in range(N+1)]

    for i in range(0 ,len(inp), 2):
        u = inp[i]
        v = inp[i+1]

        AList[u].append(v)
        
    print(AList[1:])

    for j in range(len(AList)):
        if len(AList[j]) == 0:
            Ans.append(j)
    print(Ans[0])
    
solve()
"""
