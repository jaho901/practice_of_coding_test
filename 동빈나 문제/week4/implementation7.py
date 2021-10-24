## 치킨 배달
import sys
sys.stdin = open('input.txt')
###
from itertools import combinations

N, M = map(int, input().split())
# 0:빈칸  1:집  2:치킨집
arr = [list(map(int, input().split())) for _ in range(N)]

index_2 = []
index_1 = []

for x in range(len(arr)):
    for y in range(len(arr[0])):
        if arr[x][y] == 2:
            index_2.append([x, y])
        if arr[x][y] == 1:
            index_1.append([x, y])
print(index_1)
print(index_2)
num = list(range(len(index_2)))
chi_list = []
sub = []


def choose(cur, cnt):
    global chi_list

    if cnt == M:
        chi = sub[:]
        chi_list.append(chi)
        return

    if cur == len(num):
        return

    sub.append(num[cur])
    choose(cur + 1, cnt + 1)
    sub.pop()
    choose(cur + 1, cnt)


choose(0, 0)
# chi_list = list(combinations(num, 2))
print(chi_list)

def distance(idx_1, chi):
    minimum_1 = 1e9
    for i in chi:
        minimum_1 = min(minimum_1, abs(idx_1[0] - index_2[i][0]) + abs(idx_1[1] - index_2[i][1]))
    return minimum_1


minimum = 1e9
for chi in chi_list:
    total = 0
    for idx in index_1:
        total += distance(idx, chi)
    minimum = min(minimum, total)
print(minimum)

