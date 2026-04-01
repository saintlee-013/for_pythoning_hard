"""
The Scenario:In a high-security network of N servers, there are M direct communication cables.
An agent wants to find the "Critical Hub".
A server is a Critical Hub if it is directly connected to every other server in the network.
Input:The first line contains two integers N (number of servers) and M (number of cables).
The next M lines each contain two integers u and v (a cable between server u and v).
Your Task:Represent the network using an Adjacency List.Identify the ID(s) of the Critical Hub(s).
If no such hub exists, print -1.Constraints: 2 <= N <= 10**5 and 1 <= M <= 2 * 10**5
All cables are bidirectional.
INPUT :
4 3
1 2
2 3
2 4
OUTPUT:
2
"""
# N vertices and M edges
# Central Hub => no. of edges == (N-1)
import sys
def solve():
    inp = list(map(int, sys.stdin.read().split()))
    N, M = inp[0], inp[1]
    Ans = []
    del inp[0:2]
    AList = [[] for _ in range(N+1)]
    for i in range(0, len(inp), 2):
        u = inp[i]
        v = inp[i+1]
        AList[u].append(v)
        AList[v].append(u)
    print(AList[1:])
    for j in range(len(AList)):
        if len(AList[j]) == (N-1):
            Ans.append(j)
    print(Ans)
solve()
