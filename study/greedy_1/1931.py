import sys
sys.stdin = open('1931.txt')

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
data = sorted(data, key=lambda x: x[0])
data = sorted(data, key=lambda y: y[1])

end = 0
result = 0

for s, e in data:
    if s >= end:
        end = e
        result += 1

print(result)



