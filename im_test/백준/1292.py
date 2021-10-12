import sys
sys.stdin = open('1292.txt')

a, b = map(int, sys.stdin.readline().split())
data = []
i = 1
k = 1
while i <= b:
    for _ in range(k):
        data.append(k)
        i += 1
        if i > b:
            break
    k += 1
print(sum(data[a-1:b]))