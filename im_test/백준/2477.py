import sys
sys.stdin = open('2477.txt')

K = int(input())
data = []
idx = []
for i in range(6):
    a, b = map(int, input().split())
    data.append([a, b])
    idx.append(a)

x, y = 0, 0

for i in data:
    if i[0] == 1 or i[0] == 2:
        if x < i[1]:
            x = i[1]
    else:
        if y < i[1]:
            y = i[1]

if idx.count(1) > idx.count(2):
    sx = idx.index(2)
else:
    sx = idx.index(1)
if idx.count(3) > idx.count(4):
    sy = idx.index(4)
else:
    sy = idx.index(3)

nx, ny = data[sx-3][1], data[sy-3][1]


print(((x*y) - (nx*ny)) * K)



