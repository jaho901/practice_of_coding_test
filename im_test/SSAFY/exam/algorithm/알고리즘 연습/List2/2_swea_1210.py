import sys
sys.stdin = open('2_swea_1210.txt')

# 아래로 내려갈 일이 없기 때문에 방향벡터는 3개만 지정
dx = [-1, 0, 0]
dy = [0, -1, 1]

# 방향벡터와 조건문을 사용하면서 원하는 열의 인덱스를 추출하는 함수 생성
def search(x, y):
    visited = [[0]*100 for _ in range(100)]
    visited[x][y] = 1
    while x != 0:
        for i in range(3):
            # 이동한 위치를 nx, ny로 새롭게 지정해준다.
            nx = x + dx[i]
            ny = y + dy[i]
            if 100 > nx >= 0 and 100 > ny >= 0 and visited[nx][ny] == 0 and data[nx][ny] == 1:
                # 조건을 만족하면 이동한 위치를 1로 지정하며 현재위치로 갱신
                visited[nx][ny] = 1
                x = nx
                y = ny
    return y


for tc in range(10):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    start = []
    for i in range(100):
        if data[99][i] == 2:
            result = search(99, i)

    print('#{} {}'.format(tc, result))

