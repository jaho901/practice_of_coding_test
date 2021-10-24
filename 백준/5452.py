import sys
sys.stdin = open('5452.txt')
from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    node = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        node[s].append([w, e])
    print(node)
    INF = 1000000000
    heap = []
    visited = [INF] * (N+1)

    def dijkstra():
        heappush(heap, [0, 0])
        visited[0] = 0

        while heap:
            w, e = heappop(heap)

            for next_w, next_e in node[e]:
                nw = next_w + w
                if visited[next_e] > visited[e] + next_w:
                    visited[next_e] = nw
                    heappush(heap, [nw, next_e])
    
    dijkstra()
    print(visited)