## 치킨 배달
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
# 0:빈칸  1:집  2:치킨집
arr = [list(map(int, input().split())) for _ in range(N)]

# 예제 2번처럼
# 어떻게 M을 나눠서 가장 최단거리를 구하는지 모르겠다......

def chicken(arr):
    chicken_idx = []
    home_idx = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 2:
                chicken_idx.append([i, j])
            elif arr[i][j] == 1:
                home_idx.append([i, j])

    length = []
    for i in chicken_idx:
        minimum = N*N
        for j in home_idx:
            dis = abs(i[0] - j[0]) + abs(i[1] - j[1])
            if dis < minimum:
                minimum = dis
        length.append(minimum)
    # length.sort()
    # return sum(length[0:M])
    return length

print(chicken(arr))


