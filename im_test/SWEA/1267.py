import sys
sys.stdin = open('1267.txt')

T = 3
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    data = list(map(int, input().split()))
    for e in range(0, len(data), 2):
        arr[data[e]][data[e+1]] += 1

    

