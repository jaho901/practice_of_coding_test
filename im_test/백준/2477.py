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

# 이 문제 또한 푸는데 조건을 찾는 것이 가장 중요하다!!!
# 참외밭은 항상 육각형이기 때문에 항상 문제에서의 그림과 같은 구조이다!!
# 나는 가장 큰 사각형의 넓이에서 작은 사각형의 넓이를 빼주었다.

# 동쪽, 서쪽에서 가장 큰 수를 x로
# 북쪽, 남쪽에서 가장 큰 수를 y로 지정해주었다.
# ==> x와 y의 곱은 가장 큰 정사각형의 넓이!
for i in data:
    if i[0] == 1 or i[0] == 2:
        if x < i[1]:
            x = i[1]
    else:
        if y < i[1]:
            y = i[1]

# 변의 방향을 나타내면 [4, 2, 3, 1, 3, 1]
# 하나만 존재하는 위치는 4와 2이다.
# 그 위치에서 인덱스를 3씩 빼준 위치에 있는 값들이 작은 사각형의 가로, 세로이다!!

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



