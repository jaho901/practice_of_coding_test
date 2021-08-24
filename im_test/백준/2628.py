## 종이자르기

import sys
sys.stdin = open('2628.txt')

w, h = map(int, input().split())
N = int(input())
dash_list = [list(map(int, input().split())) for _ in range(N)]
width = [0]
height = [0]

for i in dash_list:
    if i[0] == 0:    
       width.append(i[1])
    else:
        height.append(i[1])

width = sorted(width)
width.append(h)
height = sorted(height)
height.append(w)

max_w = width[1] - width[0]
max_h = height[1] - height[0]
for i in range(1, len(width)):
    n = width[i] - width[i-1]
    if max_w < n:
        max_w = n
for j in range(1, len(height)):
    m = height[j] - height[j-1]
    if max_h < m:
        max_h = m
print(max_w*max_h)





