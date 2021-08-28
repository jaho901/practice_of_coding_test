import sys
sys.stdin = open('10163.txt')

n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for i in range(n):
    data = list(map(int, input().split()))
    lx, ly = data[:2]
    w = data[2]
    h = data[3]
    for j in range(lx, lx+w):
        for k in range(ly, ly+h):
            arr[j][k] = i + 1

result = []
for i in range(1, n + 1):
    sub = 0
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == i:
                sub += 1
    result.append(sub)

for a in result:
    print(a)









